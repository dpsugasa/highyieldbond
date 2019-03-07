#!/usr/bin/env python

import QuantLib as ql
import plotly
import plotly.plotly as py #for plotting
import plotly.graph_objs as go
import plotly.dashboard_objs as dashboard
import plotly.tools as tls
import plotly.figure_factory as ff

import credentials
import pricer as pc

#build data matrix
data_matrix = [['Altice 7.25% 5/15/2022, ''],
               ['Fixed Rate Bond - no calls/no credit', pc.pricer.fixedRateBond.cleanPrice()],
               ['Callable Bond - no credit', fin_mando_px],
               ['Delta', np.round((put_d + call_d),3)],
               ['Parity', np.round(current_parity(),3)],
               ['Points Above Parity', parity_points],
               ['Carry to Mat.', carry_mat],
               ['Points Cheap', points_cheap],
               ['Pts. Cheap Per Year', pts_cheap_year],
               ]
                       
colorscale = 'Greys' #[[0, '#4d004c'],[.5, '#f2e5ff'],[1, '#ffffff']]
table = ff.create_table(data_matrix, height_constant = 15, colorscale=colorscale) #height_constant = 20
table.layout.xaxis.update({'fixedrange': True})
table.layout.yaxis.update({'fixedrange': True})
py.iplot(table, filename='Expected_Range/Macro_Expected_Ranges')

dboard = dashboard.Dashboard()

box_1 = {
        'type' : 'box',
        'boxType':'plot',
        'fileId': 'dpsugasa:2504',
        'shareKey': None,
        'title': 'Macro Expected Ranges'
}

box_2 = {
        'type' : 'box',
        'boxType':'plot',
        'fileId': 'dpsugasa:1126',
        'shareKey': None,
        'title': 'Macro Trend Signals'
}
        

dboard.insert(box_1)
dboard['settings']['title'] = 'Expected Range'
dboard['layout']['size'] = 600
#dboard.insert(box_2, 'right', 1, fill_percent=60)
py.dashboard_ops.upload(dboard, 'Macro Expected Ranges') #uncomment to create dashboard



