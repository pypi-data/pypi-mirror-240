# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sqlalchemy import select, and_, outerjoin, join
from jdw.data.SurfaceAPI.engine import FetchKDEngine
from ultron.factor.data.transformer import Transformer
from jdw.data.SurfaceAPI.universe import BaseUniverse


class Factors(object):

    def __init__(self, name, tables=None):
        self._engine = FetchKDEngine()
        mapping = self._engine._base.classes.keys(
        ) if tables is None else tables
        self._factor_tables = [
            self._engine._base.classes[k] for k in mapping if name in k
        ]

    def _map_factors(self,
                     factors,
                     used_factor_tables,
                     diff_columns={'trade_date', 'code'}):
        factor_cols = {}
        factors = set(factors).difference({'trade_date', 'code'})
        to_keep = factors.copy()
        for f in factors:
            for t in used_factor_tables:
                if f in t.__table__.columns:
                    factor_cols[t.__table__.columns[f]] = t
                    to_keep.remove(f)
                    break

        if to_keep:
            raise ValueError("factors in <{0}> can't be find".format(to_keep))

        return factor_cols

    def category(self, universe, category, start_date, end_date, columns=None):
        factor_model = self._engine.table_model(category)
        if columns is not None:
            cols = [factor_model.trade_date, factor_model.code]
            for col in columns:
                cols.append(factor_model.__dict__[col])
        else:
            cols = [factor_model]

        if isinstance(universe, BaseUniverse):
            cond = universe._query_statements(start_date, end_date)
            universe_model = universe._table_model
            big_table = join(
                factor_model, universe_model,
                and_(factor_model.trade_date == universe_model.trade_date,
                     factor_model.code == universe_model.code,
                     factor_model.flag == 1, cond))
            query = select(cols).select_from(big_table)\
            .order_by(factor_model.trade_date, factor_model.code)
        elif isinstance(universe, list):
            query = select(cols).where(
                and_(factor_model.trade_date.between(start_date, end_date),
                     factor_model.code.in_(universe))).order_by(
                         factor_model.trade_date, factor_model.code)
        else:
            query = select(cols).where(
                and_(factor_model.trade_date.between(start_date, end_date),
                     )).order_by(
                         factor_model.trade_date, factor_model.code)
        df = pd.read_sql(query, self._engine.client())
        if 'id' in df.columns:
            df.drop('id', axis=1, inplace=True)
        if 'flag' in df.columns:
            df.drop('flag', axis=1, inplace=True)
        if 'timestamp' in df.columns:
            df.drop('timestamp', axis=1, inplace=True)
        df.replace([-np.inf, np.inf], np.nan, inplace=True)
        return df

    def fetch(self, universe, start_date, end_date, columns):
        if isinstance(columns, Transformer):
            transformer = columns
        else:
            transformer = Transformer(columns)
        dependency = transformer.dependency
        universe_model = universe._table_model if isinstance(
            universe, Universe) else None
        factor_cols = self._map_factors(dependency, self._factor_tables)
        joined_tables = set()
        factor_tables = list(set(factor_cols.values()))
        if len(factor_cols) <= 0:
            raise ValueError("factor_tables len({0})".format(
                len(factor_tables)))

        one_table = factor_tables[0]
        big_table = factor_tables[0]
        joined_tables.add(big_table.__table__.name)
        if isinstance(universe, Universe):
            cond = universe._query_statements(start_date, end_date)
            for t in set(factor_cols.values()):
                if t.__table__.name not in joined_tables:
                    big_table = outerjoin(
                        big_table, t,
                        and_(one_table.trade_date == t.trade_date,
                             one_table.code == t.code, one_table.flag == 1))
                    joined_tables.add(t.__table__.name)

            big_table = join(
                big_table, universe_model,
                and_(one_table.trade_date == universe_model.trade_date,
                     one_table.flag == 1,
                     one_table.code == universe_model.code, cond))

            query = select([one_table.trade_date, one_table.code] +
                           list(factor_cols.keys())).select_from(big_table)
        else:
            for t in set(factor_cols.values()):
                if t.__table__.name not in joined_tables:
                    big_table = outerjoin(
                        big_table, t,
                        and_(one_table.trade_date == t.trade_date,
                             one_table.code == t.code, t.flag == 1))
                    joined_tables.add(t.__table__.name)
            clause_list = and_(
                factor_tables[0].flag == 1,
                factor_tables[0].code.in_(universe),
                factor_tables[0].trade_date.between(start_date, end_date))

            query = select(
                [factor_tables[0].trade_date, factor_tables[0].code] +
                list(factor_cols.keys())).select_from(big_table).where(
                    clause_list)

        df = pd.read_sql(query, self._engine.client()) \
            .replace([-np.inf, np.inf], np.nan) \
            .sort_values(['trade_date', 'code']) \
            .drop_duplicates(["trade_date", "code"]) \
            .set_index('trade_date')

        res = transformer.transform('code', df).replace([-np.inf, np.inf],
                                                        np.nan)
        res = res.reset_index()
        res["trade_date"] = pd.to_datetime(res["trade_date"])
        return res

    def universe_fetch(self, universe, start_date, end_date, columns):
        universe_model = universe._table_model
        factor_cols = self._map_factors(columns, self._factor_tables)
        joined_tables = set()
        factor_tables = list(set(factor_cols.values()))
        if len(factor_cols) <= 0:
            raise ValueError("factor_tables len({0})".format(
                len(factor_tables)))

        cond = universe._query_statements(start_date, end_date)
        one_table = factor_tables[0]
        big_table = factor_tables[0]
        joined_tables.add(big_table.__table__.name)
        for t in set(factor_cols.values()):
            if t.__table__.name not in joined_tables:
                big_table = outerjoin(
                    big_table, t,
                    and_(one_table.trade_date == t.trade_date,
                         one_table.code == t.code, one_table.flag == 1))
                joined_tables.add(t.__table__.name)

        big_table = join(
            big_table, universe_model,
            and_(one_table.trade_date == universe_model.trade_date,
                 one_table.flag == 1, one_table.code == universe_model.code,
                 cond))

        query = select([one_table.trade_date, one_table.code] +
                       list(factor_cols.keys())).select_from(big_table)

        return pd.read_sql(query, self._engine.client()).drop_duplicates(
            subset=['trade_date', 'code']).replace(
                [-np.inf, np.inf],
                np.nan).sort_values(by=['trade_date', 'code'])

    def codes_fetch(self, codes, start_date, end_date, columns):
        factor_cols = self._map_factors(columns, self._factor_tables)
        joined_tables = set()
        factor_tables = list(set(factor_cols.values()))
        if len(factor_cols) <= 0:
            raise ValueError("factor_tables len({0})".format(
                len(factor_tables)))

        big_table = factor_tables[0]
        joined_tables.add(big_table.__table__.name)
        for t in set(factor_cols.values()):
            if t.__table__.name not in joined_tables:
                big_table = outerjoin(
                    big_table, t,
                    and_(big_table.trade_date == t.trade_date,
                         big_table.code == t.code, t.flag == 1))
                joined_tables.add(t.__table__.name)

        clause_list = and_(
            factor_tables[0].flag == 1, factor_tables[0].code.in_(codes),
            factor_tables[0].trade_date.between(start_date, end_date))

        query = select([factor_tables[0].trade_date, factor_tables[0].code] +
                       list(factor_cols.keys())).select_from(big_table).where(
                           clause_list)
        return pd.read_sql(query, self._engine.client()).drop_duplicates(
            subset=['trade_date', 'code']).replace(
                [-np.inf, np.inf],
                np.nan).sort_values(by=['trade_date', 'code'])