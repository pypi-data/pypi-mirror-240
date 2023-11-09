# -*- coding: utf-8 -*-
import pdb
import pandas as pd
from jdw.kdutils.logger import kd_logger
from ultron.tradingday import *
from ultron.factor.data.transformer import Transformer
from ultron.factor.analysis.quantile_analysis import er_quantile_analysis
from ultron.factor.fitness.metrics import Metrics as FactorMetrics


class Base(object):

    def __init__(self,
                 yields_class,
                 factors_class,
                 universe_class,
                 industry_class,
                 universe,
                 offset,
                 horizon,
                 factor_columns,
                 industry_name,
                 industry_level,
                 factors_data=None,
                 yield_name='returns'):

        self._yields_class = yields_class
        self._factors_class = factors_class
        self._universe_class = universe_class
        self._industry_class = industry_class
        #self._factor_columns = factor_columns
        self._transformer = Transformer(factor_columns)
        self._universe = universe
        self._factors_data = factors_data
        self._yield_name = yield_name
        self._industry_name = industry_name
        self._industry_level = industry_level
        self._offset = offset
        self._horizon = horizon
        self._results = None
        self._total_data = None

    def industry_fillna(self, industry_data, factors_data):
        return factors_data

    def fetch_factors(self, begin_date, end_date, codes=None):
        kd_logger.info("start fetch factor data")
        factors = self._factors_class()
        if self._universe is not None:
            universe = self._universe_class(u_name=self._universe)
            factors_data = factors.universe_fetch(
                universe=universe,
                start_date=begin_date,
                end_date=end_date,
                columns=self._transformer.dependency)
        else:
            factors_data = factors.codes_fetch(
                codes=codes,
                start_date=begin_date,
                end_date=end_date,
                columns=self._transformer.dependency)
        return factors_data

    def fetch_yields(self, begin_date, end_date, codes=None):
        kd_logger.info("start create yields data")
        yields = self._yields_class()
        if self._universe is not None:
            universe = self._universe_class(u_name=self._universe)
            if self._yield_name == 'returns':
                closing_date = advanceDateByCalendar(
                    'china.sse', end_date,
                    "{}b".format(self._offset + self._horizon + 1),
                    BizDayConventions.Following)
                yields_data = yields.fetch_returns(universe=universe,
                                                   start_date=begin_date,
                                                   end_date=closing_date,
                                                   horizon=self._horizon,
                                                   offset=self._offset,
                                                   benchmark=None)
            else:
                yields_data = yields.universe_fetch(universe=universe,
                                                    start_date=begin_date,
                                                    end_date=end_date,
                                                    name=self._yield_name)
        else:
            yields_data = yields.codes_fetch(codes=codes,
                                             start_date=begin_date,
                                             end_date=end_date,
                                             name=self._yield_name)
        return yields_data

    def metrics(self, total_data):
        evaluate_res = []
        for f in self._transformer.names:
            res = []
            ms = FactorMetrics(returns=total_data['nxt1_ret'].unstack(),
                               factors=total_data[f].unstack())
            score = ms.fit_metrics()
            res.append(score.long_evaluate._asdict())
            res.append(score.short_evaluate._asdict())
            res.append(score.both_evaluate._asdict())
            evaluate_data = pd.DataFrame(res)
            evaluate_data['name'] = f
            evaluate_res.append(
                evaluate_data.set_index(['name', 'category', 'freq']))
        results = pd.concat(evaluate_res, axis=0)
        return results.reset_index()

    def industry_median(self, factors_data):

        def _industry_median(standard_data, factor_name):
            median_values = standard_data[[
                'trade_date', 'industry_code', 'code', factor_name
            ]].groupby(['trade_date', 'industry_code']).median()[factor_name]

            median_values.name = factor_name + '_median'
            factor_data = standard_data[[
                'trade_date', 'industry_code', 'code', factor_name
            ]].merge(median_values.reset_index(),
                     on=['trade_date', 'industry_code'],
                     how='left')
            factor_data['standard_' +
                        factor_name] = factor_data[factor_name].mask(
                            pd.isnull(factor_data[factor_name]),
                            factor_data[factor_name + '_median'])
            return factor_data.drop(
                [factor_name + '_median'],
                axis=1).set_index(['trade_date', 'code', 'industry_code'])

        res = []
        standarad_cols = [
            'standard_' + col for col in self._transformer.dependency
        ]
        kd_logger.info("start industry median data ...")

        for col in self._transformer.dependency:
            rts = _industry_median(factors_data, col)
            res.append(rts)

        factors_data = pd.concat(res, axis=1)

        factors_data = factors_data.fillna(0)
        factors_data = factors_data.reset_index().set_index(
            ['trade_date', 'code'])
        factors_data = factors_data.drop(
            self._transformer.dependency, axis=1).rename(columns=dict(
                zip(standarad_cols, self._transformer.dependency)))
        return factors_data.reset_index()

    def fetch_industry(self, begin_date, end_date, codes=None):
        kd_logger.info("start fetch industry data")
        industry = self._industry_class()
        if self._universe is not None:
            universe = self._universe_class(u_name=self._universe)
            industry_data = industry.universe_fetch(
                universe,
                start_date=begin_date,
                end_date=end_date,
                category=self._industry_name,
                level=self._industry_level)
        else:
            industry_data = industry.codes_fetch(codes=codes,
                                                 start_date=begin_date,
                                                 end_date=end_date,
                                                 category=self._industry_name,
                                                 level=self._industry_level)
        return industry_data

    def run(self, begin_date, end_date, codes=None):
        kd_logger.info("start service")
        yields_data = self.fetch_yields(begin_date=begin_date,
                                        end_date=end_date,
                                        codes=codes)
        if self._factors_data is None:
            factors_data = self.fetch_factors(begin_date=begin_date,
                                              end_date=end_date,
                                              codes=codes)
        else:
            factors_data = self._factors_data.copy()

        industry_data = self.fetch_industry(begin_date=begin_date,
                                            end_date=end_date,
                                            codes=codes)

        ## 中位数填充
        factors_data = self.industry_fillna(industry_data=industry_data,
                                            factors_data=factors_data)
        factors_data = factors_data.sort_values(by=['trade_date', 'code'])
        factors_data = self._transformer.transform(
            'code', factors_data.set_index('trade_date'))
        self._total_data = factors_data.reset_index().merge(
            yields_data, on=['trade_date', 'code'])
        self._results = self.metrics(
            self._total_data.set_index(['trade_date', 'code']))

    def filter(self, category, name, sort=False):
        name = [name] if not isinstance(name, list) else name
        return self._results[self._results['category'] ==
                             category].sort_values(by=name, ascending=sort)

    def quantile(self, name, bind, de_trend=True):
        df = pd.DataFrame(columns=['q' + str(i) for i in range(1, bind + 1)])
        total_data = self._total_data.copy()[[
            'trade_date', 'code', name, 'nxt1_ret'
        ]]
        grouped = total_data.groupby('trade_date')
        for k, g in grouped:
            er = g[name].values
            dx_return = g['nxt1_ret'].values
            res = er_quantile_analysis(er,
                                       n_bins=bind,
                                       dx_return=dx_return,
                                       de_trend=de_trend)
            df.loc[k, :] = res
        return df
