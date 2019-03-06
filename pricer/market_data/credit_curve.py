#!/usr/bin/env python

import numpy as np
from datetime import datetime
from tia.bbg import LocalTerminal
import QuantLib as ql

import yield_curve as yc


'''
Download BBG CDS curve
'''

altice = LocalTerminal.get_reference_data('YCCD2204 Index', 'CURVE_TENOR_RATES', ).as_frame()
curve = altice.iloc[0].loc['CURVE_TENOR_RATES']
memb = curve['Tenor Ticker'].tolist()
memb = memb[1:]
tenor = curve['Tenor'].tolist()
tenor =  tenor[1:]
tenor = ([int(z.strip('Y')) for z in tenor])
rates = []

for i in memb:
    z = LocalTerminal.get_reference_data(i, 'CDS_FLAT_SPREAD', ).as_frame()
    rates.append((z.loc[i].item()/10000))

cc_raw = dict(zip(tenor,rates)) 

'''
Build Quantlib Credit Curve
'''   

ql_rates = []
ql_dates = []

for i, j in cc_raw.items():
    ql_rates.append(ql.SimpleQuote(j))
    ql_dates.append(yc.calendar.advance(yc.todaysDate, ql.Period(i, ql.Years)))

spotCurve_credit = ql.SpreadedLinearZeroInterpolatedTermStructure(
    yc.spotCurveHandle,
   [ql.QuoteHandle(q) for q in ql_rates],
    ql_dates
)
spotCurve_credit_handle = ql.YieldTermStructureHandle(spotCurve_credit)
    
