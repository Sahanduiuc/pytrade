#!/usr/bin/env python

from scipy.ndimage.interpolation import shift as _shift
import math as _math
import numpy as _np
cimport numpy as _np


cpdef double round_to_fraction(double val, double res=0.01, decimals=None):
    """
    round to closest resolution
    round_to_fraction(val, res=0.01, decimals=None)
    """
    if decimals is None and "." in str(res):
        decimals = len(str(res).split('.')[1])

    return round(_math.floor(val / res) * res, decimals)


cdef _np.ndarray _moving_average(_np.ndarray data, int lookback):
    data = _np.cumsum(_np.nan_to_num(data), dtype=float)
    data[lookback:] = data[lookback:] - data[:-lookback]
    return data[lookback - 1:] / lookback


cpdef tuple atr_bracket(ohlc, double entry, int lookback=14, int multiplier=3):
    """ upper, lower = atr_bracket(ohlc, entry, lookback=14, multiplier=3) """

    cdef _np.ndarray atr, openp, highp, lowp, closep, _
    cdef _np.ndarray close_shift, tr

    ohlc = ohlc[-lookback*2:]
    openp, highp, lowp, closep, _ = ohlc.T.values

    # calculate atr
    close_shift = _shift(closep, 1, cval=_np.nan)
    atr = _moving_average(_np.max(_np.array([
        openp - lowp, abs(highp - close_shift), abs(lowp - close_shift)
    ]), axis=0), lookback)

    cdef double upper = max([
        entry + atr[-1] * multiplier,
        entry + max(atr[-lookback:]) * multiplier,
        max(highp[-lookback:])
    ])

    cdef double lower = min([
        entry - atr[-1] * multiplier,
        entry - min(atr[-lookback:]) * multiplier,
        min(lowp[-lookback:])
    ])

    return round(upper, 2), round(lower, 2)


cpdef tuple position_sizer(double balance, double entry, double stop,
                          double max_risk_pct=0.01, double tick_size=0.01,
                          double tick_value=0.01, int share_block_size=1):
    """
    position_dollars, shares = position_sizer(
        balance, entry, stop, max_risk_pct=0.01,
        tick_size=0.01, tick_value=0.01, share_block_size=1)
    """

    cdef double dollars_to_risk = balance * max_risk_pct
    cdef double risk_ticks = abs(entry - stop) / tick_size
    cdef double risk_tick_value = risk_ticks * tick_value
    cdef double shares = int(dollars_to_risk / risk_tick_value)
    cdef double position_dollars = 0

    if tick_size == 0.01 and tick_value == 0.01:
        # shares
        position_dollars = min([balance, entry * shares])
        shares = round_to_fraction(position_dollars / entry, share_block_size)
        position_dollars = entry * shares
        return position_dollars, shares

    else:
        # futures
        position_dollars = 0. if shares == 0 else max(
            [balance, entry * shares])

    return position_dollars, shares
