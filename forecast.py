import matplotlib.pyplot as plt
import matplotlib
% matplotlib inline

df['rain'] = df['pop'].as_matrix()
df = df.drop('pop', 1)

tmean = pd.rolling_mean(df['temp'], window=4, center=True)
rhmean = pd.rolling_mean(df['rh'], window=4, center=True)
cldsmean = pd.rolling_mean(df['clds'], window=4, center=True)
wspdmean = pd.rolling_mean(df['wspd'], window=4, center=True)
rainmean = pd.rolling_mean(df['rain'], window=4, center=True)

matplotlib.style.use('bmh')

fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(8, 10))

df['temp'].plot(ax=axes[0], color='dodgerblue', sharex=True)
tmean.plot(ax=axes[0], kind='line', color='darkorchid', sharex=True)
axes[0].set_ylabel('temperature [$^o$C]')

df['rain'].plot(ax=axes[1], color='dodgerblue', sharex=True)
axes[1].set_ylabel('chance of rain [%]')

df['rh'].plot(ax=axes[2], color='dodgerblue', sharex=True)
rhmean.plot(ax=axes[2], kind='line', color='darkorchid', sharex=True)
axes[2].set_ylabel('humidity [%]')

df['clds'].plot(ax=axes[3], color='dodgerblue', sharex=True)
cldsmean.plot(ax=axes[3], kind='line', color='darkorchid', sharex=True)
axes[3].set_ylabel('clouds [%]')

df['wspd'].plot(ax=axes[4], color='dodgerblue', sharex=False)
wspdmean.plot(ax=axes[4], kind='line', color='darkorchid', sharex=True)
axes[4].set_ylabel('wind [m s$^{-1}$]')