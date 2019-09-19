import pandas as pd
import numpy as np
from datetime import datetime

df = pd.DataFrame.from_dict(weather['forecasts'][0], orient='index').transpose()
for forecast in weather['forecasts'][1:]:
    df = pd.concat([df, pd.DataFrame.from_dict(forecast, orient='index').transpose()])

# extract time and use it as index
time = np.array(df['fcst_valid_local'])
for row in range(len(time)):
    time[row] = datetime.strptime(time[row], '%Y-%m-%dT%H:%M:%S+0100')

df = df.set_index(time)

list(df)