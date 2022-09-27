#%%
from tracemalloc import start
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
register_matplotlib_converters()

#%%
def read_data():
    return pd.read_csv('ice_cream.csv')

df_ice= read_data()
# %%
df_ice.head() # IPN31152N => higher the number, more the production 
# %%
df_ice.rename(columns={'DATE':'date','IPN31152N':'production'},inplace=True)
#convert date column to datetime type
df_ice['date']=pd.to_datetime(df_ice.date)

# %%
#setting index as date to make plotting easier
df_ice.set_index('date',inplace=True)

# %%
#subsetting data and getting from 2010 01 01 for clean analysis
start_date =pd.to_datetime('2010-01-01')
df_ice = df_ice[start_date:]
# %%
df_ice.head()
# %%
def plot_xdate(col,title,ylab):
    plt.figure(figsize=(10,4))
    plt.plot(col)
    plt.title(title,fontsize=20)
    plt.ylabel(ylab,fontsize=16)
    for year in range(2011,2021):
        plt.axvline(pd.to_datetime(str(year)+'-01-01'),color='k', linestyle='--',alpha=0.2)
plot_xdate(df_ice.production,'Ice Cream Production over Time','Production')
# %%
#acf plot -auto corelation

acf_plot = plot_acf(df_ice.production, lags=100)
#decaying

#pacfx
pacf_plot = plot_pacf(df_ice.production)

# %%
