import os
import sys

import pandas as pd
from tia.bbg import LocalTerminal
import numpy as np
from datetime import datetime
import QuantLib as ql
#import plotly
#import plotly.plotly as py #for plotting
#import plotly.offline as offline
#import plotly.graph_objs as go
#import plotly.dashboard_objs as dashboard
#import plotly.tools as tls
#import plotly.figure_factory as ff
#import credentials

__version__ = "0.1.0"

print ("Market Data Loading....")