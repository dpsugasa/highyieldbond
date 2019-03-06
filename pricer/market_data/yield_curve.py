#!/usr/bin/env python

import numpy as np
from datetime import datetime
from tia.bbg import LocalTerminal
import QuantLib as ql

'''
Build Yield Curve
retrieve USD curve; S23 USD Swaps (30/360, S/A)
'''
today = datetime.date(datetime.now())
td = datetime.strftime(today, "%d,%m,%Y")
todaysDate = ql.Date(td, "%d,%m,%Y")
ql.Settings.instance().evaluationDate = todaysDate
usd = LocalTerminal.get_reference_data('YCSW0023 Index', 'par_curve', ).as_frame()
s23 = usd.iloc[0].loc['par_curve']

###pull dates
dates = s23['Date'].tolist()
dates = [datetime.strftime(i, "%d,%m,%Y") for i in dates]
ql_dates = [ql.Date(i, "%d,%m,%Y") for i in dates]
ql_dates = [todaysDate] + ql_dates
###pull rates
rates = s23['Rate'].tolist()
on = LocalTerminal.get_reference_data('US00O/N Index', 'PX_LAST').as_frame()
on = on.at['US00O/N Index','PX_LAST']
rates = [np.round(on,decimals = 5)] + rates
rates = [i*.01 for i in rates]
###build yield curve
spotDates = ql_dates
spotRates = rates
dayCount = ql.Actual360()
calendar = ql.UnitedStates()
interpolation = ql.Linear()
compounding = ql.Compounded
compoundingFrequency = ql.Annual
#########################################
spotCurve = ql.ZeroCurve(spotDates, spotRates, dayCount, calendar, interpolation,
                             compounding, compoundingFrequency)
                             
spotCurveHandle = ql.YieldTermStructureHandle(spotCurve)