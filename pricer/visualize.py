#!/usr/bin/env python

import QuantLib as ql
from tia.bbg import LocalTerminal
from datetime import datetime
import plotly
import plotly.plotly as py #for plotting
import plotly.graph_objs as go
import plotly.dashboard_objs as dashboard
import plotly.tools as tls
import plotly.figure_factory as ff

import credentials
import pricer as pc


'''
Collect Market Data
'''

# set dates, securities, and fields
start_date = '01/01/2005'
end_date = "{:%m/%d/%Y}".format(datetime.now())
IDs = ['EK179454 CORP']

fields = ['LAST PRICE']

df = LocalTerminal.get_historical(IDs, fields, start_date, end_date, period = 'DAILY').as_frame()
df.columns = df.columns.droplevel()
df['ret'] = df.pct_change()


'''
Build graphs
'''

trace_price = go.Scatter(
                x = df.index,
                y = df['LAST PRICE'].values,
                xaxis = 'x1',
                yaxis = 'y1',
                mode = 'lines',
                line = dict(width=2, color= 'blue'),
                name = 'Price Performance',
                )

layout = go.Layout(title = 'High Yield Price Performance',
                   xaxis=dict(title = 'Date',
                              fixedrange = True),
                   yaxis=dict(title = 'Price',
                              fixedrange = True),
                   showlegend=False, hovermode='closest')

fig = go.Figure(data=[trace_price], layout=layout)

py.iplot(fig, filename = 'HighYieldPricer/Price_performance')


trace_returns = go.Histogram(
            x = df['ret'].values,
            histnorm = 'probability'
        )

layout = go.Layout(title = 'High Yield Returns',
                   xaxis=dict(title = 'returns',
                              fixedrange = True),
                   yaxis=dict(title = 'Count',
                              fixedrange = True),
                   showlegend=False, hovermode='closest')

fig = go.Figure(data=[trace_returns], layout=layout)

py.iplot(fig, filename = 'HighYieldPricer/Return_performance')


'''
Build Pricing Dashboard
'''

#build data matrix
data_matrix = [['Altice 7.25% 5/15/2022', ''],
               ['Issue Date', pc.call_bond.issueDate()] ,
               ['Maturity Date', pc.call_bond.maturityDate()],
               ['Coupon', pc.call_bond.nextCouponRate()],
               ['Settlement Days', pc.call_bond.settlementDays()],
               ['Fixed Rate Bond - no calls/no credit', pc.fixedRateBond.cleanPrice()],
               ['Callable Bond - no credit', pc.call_bond.cleanPrice()],
               ['Risky Callable Bond', pc.risky_call_bond.cleanPrice()],
               ['Yield - Callable', pc.call_bond.bondYield(pc.accrual_daycount, pc.compounding, pc.compoundingFrequency)],
               ['Yield - Risky Callable', pc.risky_call_bond.bondYield(pc.risky_call_bond.cleanPrice(),pc.accrual_daycount, pc.compounding, pc.compoundingFrequency)],
               ]
                       
table = ff.create_table(data_matrix, height_constant = 10) 
#table.layout.xaxis.update({'fixedrange': True})
#table.layout.yaxis.update({'fixedrange': True})
py.iplot(table, filename='HighYieldPricer/HighYieldBond')

dboard = dashboard.Dashboard()

box_1 = {
        'type' : 'box',
        'boxType':'plot',
        'fileId': 'dpsugasa:3952',
        'shareKey': None,
        #'title': 'Macro Expected Ranges'
}

box_2 = {
        'type' : 'box',
        'boxType':'plot',
        'fileId': 'dpsugasa:3954',
        'shareKey': None,
        #'title': 'Macro Trend Signals'
}

box_3 = {
        'type' : 'box',
        'boxType':'plot',
        'fileId': 'dpsugasa:3956',
        'shareKey': None,
        #'title': 'Macro Trend Signals'
}
        

dboard.insert(box_1)
#dboard['settings']['title'] = 'High Yield'
#dboard['layout']['size'] = 600
#dboard['layout']['height'] = 800
dboard.insert(box_2, 'right', 1, fill_percent = 70)
dboard.insert(box_3, 'below', 2, fill_percent = 30)#, fill_percent=40)
py.dashboard_ops.upload(dboard, 'High Yield') #uncomment to create dashboard




