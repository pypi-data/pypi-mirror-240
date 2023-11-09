# -*- coding: utf-8 -*-
from typing import Optional

from pip_services4_components.context import IContext
from pip_services4_data.query import FilterParams, PagingParams, DataPage

from data.Dummy import Dummy


class IDummyService:
    def get_page_by_filter(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams) -> DataPage:
        raise NotImplementedError()

    def get_one_by_id(self, context: Optional[IContext], id: str) -> Dummy:
        raise NotImplementedError()

    def create(self, context: Optional[IContext], entity: Dummy) -> Dummy:
        raise NotImplementedError()

    def update(self, context: Optional[IContext], entity: Dummy) -> Dummy:
        raise NotImplementedError()

    def delete_by_id(self, context: Optional[IContext], id: str) -> Dummy:
        raise NotImplementedError()
