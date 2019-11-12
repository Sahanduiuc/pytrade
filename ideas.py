#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- partner with hosting
- create marketplace with monthly plans
- sell data (eodhistoricaldata.com whitelabel?)
- offer online research environment recipes for AWS/GCP
- offer web-based IDE?
- write core components in cython

framework = pytrade
saas = quantual.com

https://quantual.com/user/ranaroussi
https://quantual.com/research
https://quantual.com/posts/92b6b3693e4c4a4d86693ba57ec9b3fb
https://quantual.com/about
https://quantual.com/docs
https://quantopian.com/opensource

https://status.quantual.com

"""

from dataclasses import dataclass


from pytrade import Pipeline, Universe

# from pytrade.feeds import (
#     ibgw, ibws, quandl, iex, yahoo, alpaca, iqfeed, bitmex
# )

from pytrade import feeds, brokers, portfolio
from pytrade.pipelines import SP500
from pytrade.calendars import earnings, splits, holidays
from pytrade.plugins import stocktwits

# custom contributors
from pytrade.contrib.pipelines import rans_daily_picks
from pytrade.contrib.plugins import portfolio


def make_pipeline():
    universe = SP500(feeds.alpaca)

    prices = universe.get_history(interval="1d", period=100, adjusted=True)
    premarket = universe.get_premarket()

    gap = premarket > prices['close']
    bullish = prices['close'] > prices['close'].mean()

    # Return Pipeline containing latest closing price
    return Pipeline(
        data={
            'price': premarket,
            'bullish': bullish
        },
        screen=gap
    )

if __name__ == "__main__":
    pass
@dataclass
class universe:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
