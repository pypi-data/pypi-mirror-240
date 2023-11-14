from __future__ import annotations

import functools
import http
import logging
from pathlib import Path
from typing import cast

import xnat
import xnat.search
from textual import on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer
from textual.widgets import Button, Header, Footer, SelectionList, RadioSet, RichLog
from textual_fspicker import FileOpen, Filters, FileSave
from xnat.core import XNATBaseObject
from xnat.exceptions import XNATResponseError

from src import io
from src.app_base import XnatBase, Loading
from src.constants import SEARCH_BASE_BUTTONS, QUERY_SELECTIONS
from src.io import QueryProtocol
from src.search_entry import get_select_fields, get_search_terms, SearchEntry, SearchConstraintError
from src.sortable_data_table import SortableDataTable
from src.xnat_tree import _get_http_status_code


class XnatQuery(XnatBase):
    CSS_PATH = 'query.tcss'
    BINDINGS = [
        Binding('a', 'add_constraint', 'Add Constraint'),
        Binding('r', 'remove_constraint', 'Remove Constraint'),
        Binding('f2', 'load_search', 'Load Search'),
        Binding('f3', 'save_search', 'Save Search'),
        Binding('s', 'save_result', 'Save Result'),
        Binding('ctrl+s', 'show_selections', 'Root/Fields'),
    ]

    def __init__(self, server: str, log_level: int = logging.INFO, search: Path | None = None) -> None:
        super().__init__(server, log_level)
        self.fields = get_select_fields(get_search_terms(self._get_classes([x.value for x in QUERY_SELECTIONS])))
        self._search = search

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id='horizontal'):
            with ScrollableContainer(id='query_input'):
                with Horizontal(id='search_base_fields', classes='remove'):
                    yield RadioSet(*SEARCH_BASE_BUTTONS, id='root_element')
                    yield SelectionList[str](*QUERY_SELECTIONS, id='selections')
                yield Button(label='Run Query...', id='query_button')
                yield SearchEntry(fields=self.fields)
            yield SortableDataTable(self.logger, id='data_table')
        yield self._setup_logging()
        yield Footer()

    async def on_mount(self) -> None:
        self.query_one('#selections', SelectionList).border_title = 'Search Fields'
        self.query_one('#root_element', RadioSet).border_title = 'Root Element'
        data_table = self.query_one('#data_table', SortableDataTable)
        data_table.border_title = 'Results'
        data_table.zebra_stripes = True
        self.query_one('#query_input', ScrollableContainer).border_title = 'Input'
        self.query_one('#rich_log', RichLog).border_title = 'Log'

        if self._search is not None:
            await io.load_search(self._search, cast(QueryProtocol, self))
            self._run_query()

    def get_query_constraints(self) -> list[xnat.search.Constraint]:
        constraints = []
        entries = self.query('SearchEntry').results(SearchEntry)
        for entry in entries:
            constraints.append(entry.constraint)
        return constraints

    async def set_query_constraints(self, constraints: list[xnat.search.Constraint]) -> None:
        entries = list(self.query(SearchEntry).results(SearchEntry))

        diff = len(constraints) - len(entries)
        if diff > 0:
            parent = self.query_one('#query_input', ScrollableContainer)
            for _ in range(diff):
                await parent.mount(SearchEntry(fields=self.fields))
            entries = list(self.query(SearchEntry).results(SearchEntry))

        for index, constraint in enumerate(constraints):
            try:
                entries[index].constraint = constraint
            except SearchConstraintError as e:
                self.logger.error(e)

    def update_fields(self) -> None:
        search_fields = self.query_one('#selections', SelectionList)
        self.fields = get_select_fields(get_search_terms(self._get_classes(search_fields.selected)))
        entries = self.query(SearchEntry).results(SearchEntry)
        for entry in entries:
            entry.update_fields(self.fields)

    @on(SelectionList.SelectedChanged, '#selections')
    def fields_changed(self, _: SelectionList.SelectedChanged) -> None:
        self.update_fields()

    def _get_classes(self, selected: list[str]) -> list[XNATBaseObject]:
        classes: list[XNATBaseObject] = []
        for data_type in selected:
            classes.append(getattr(self.session.classes, data_type))
        return classes

    def _get_root_element_name(self) -> xnat.search.Query | None:
        button = self.query_one('#root_element', RadioSet).pressed_button
        if button is None:
            return None

        return cast(xnat.search.Query, getattr(self.session.classes, str(button.label) + 'Data').query())

    def _get_query(self) -> xnat.search.Query | None:
        query = self._get_root_element_name()
        if query is not None:
            for constraint in self.get_query_constraints():
                query = query.filter(constraint)

        return query

    @work(thread=True)
    def _run_query(self) -> None:
        data_table = self.query_one('#data_table', SortableDataTable)
        with Loading(data_table):
            query = self._get_query()
            if query is None:
                self.logger.error('No search base specified.')
                return

            # fields = [xnat.search.SearchField(self.session.classes.SubjectData,
            #                                   'MR_COUNT',
            #                                   'integer')]
            # query = query.view(*fields)
            # val = query.to_string()

            try:
                query_result = query.tabulate_pandas().dropna(axis='columns', how='all')
                # self.query_result = (query.tabulate_pandas().dropna(axis='columns', how='all').
                #                      drop(columns=['project', 'quality', 'uid', 'quarantine_status'], errors='ignore'))
            except XNATResponseError as e:
                query_result = None
                status = _get_http_status_code(e)
                if status == http.HTTPStatus.FORBIDDEN:
                    self.logger.error('Server returned a "forbidden" error.')

        data_table.set_data(query_result)

    @on(Button.Pressed, '#query_button')
    def run_query(self, _: Button.Pressed) -> None:
        self._run_query()

    def action_add_constraint(self) -> None:
        new_entry = SearchEntry(fields=self.fields)
        self.query_one('#query_input').mount(new_entry)
        new_entry.scroll_visible()

    def action_remove_constraint(self) -> None:
        search_entries = self.query(SearchEntry)
        if search_entries:
            search_entries.last().remove()

    def action_load_search(self) -> None:
        self.push_screen(
            FileOpen('.', filters=Filters(('Searches', lambda p: p.suffix.lower() == '.json'))),
            callback=functools.partial(io.load_search, app=self))

    def action_save_search(self) -> None:
        self.push_screen(
            FileSave(filters=Filters(('Searches', lambda p: p.suffix.lower() == '.json'))),
            callback=functools.partial(io.save_search, app=self))

    def action_save_result(self) -> None:
        data_table = self.query_one('#data_table', SortableDataTable)
        self.push_screen(
            FileSave(),
            callback=functools.partial(io.save_result, query_result=data_table.data))

    def action_show_selections(self) -> None:
        self.query_one('#search_base_fields', Horizontal).toggle_class('remove')
