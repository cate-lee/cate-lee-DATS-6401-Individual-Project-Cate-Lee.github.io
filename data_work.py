# %%
import pandas as pd
import numpy as np
# %%
data=pd.read_csv('/Users/catelee/Desktop/countries_project/raw_data_world_bank.csv', names=['country','code','param','param_code','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','average'], skiprows=1)
data.head()
# %%
##Sheet for bubble chart
data_bubble=data[['code','param','2018']]
data_bubble=data_bubble.query('param=="GDP (constant 2010 US$)" or param =="Adjusted savings: education expenditure (current US$)" or param =="Population, total"')
data_bubble.head()
# %%
data_bubble=data_bubble.pivot(index='code', columns='param', values='2018')
#%%
region_dict={'USA':'North America','MEX':'North America','CAN':'North America','EUU':'Europe','FRA':'Europe','GBR':'Europe','DEU':'Europe','ITA':'Europe','TUR':'Middle East','ARG':'South America','BRA':'South America',
'ZAF':'Africa','SAU':'Middle East','KOR':'Asia','IDN':'Asia','JPN':'Asia','IND':'Asia','CHN':'China','AUS':'Australia','RUS':'Asia'}
data_bubble['region'] = data_bubble.index.map(region_dict)
# %%
data_bubble.to_csv(r'/Users/catelee/Desktop/countries_project/bubble_data.csv')
# %%
#Sheet for military expenditure(USD)
data_military=data.query('param=="Military expenditure (current USD)"')
data_military=data_military[['code','param','2018']]
#%%
#sheet for military expenditure (% of GDP)
data_military_2=data.query('param=="Military expenditure (percent of GDP)"')
data_military_2=data_military_2[['code','param','2018']]
data_military_2.head()
#%%Sheet for health expenditure (% of GDP)
data_military_2=data.query('param=="Military expenditure (percent of GDP)"')
data_military_2=data_military_2[['code','param','2018']]
data_military_2.head()
# %%
data_health_share=data[['code','param','2017']]
data_health_share=data_health_share.query(('param=="Current health expenditure (percent of GDP)"'))
data_health_share.pivot(index="code",columns="param",values='2017')
# %%
#gdp per capita and health spending per capita
data_health_capita=data[['code','param','2017']]
data_health_capita=data_health_capita.query(('param=="Current health expenditure per capita (current US$)" or param=="GDP per capita (constant 2010 US$)"'))
data_health_capita.pivot(index="code",columns="param",values='2017')

# %%
#military spending per capita and education spending per capita
data_capita=data[['code','param','2017']]
data_capita=data_capita.query(('param=="Military expenditure (current USD)" or param=="Population, total"'))
data_capita.pivot(index="code",columns="param",values='2017')
data_capita['mil_spend_cap']=data_capita['Military expenditure (current USD)']/data_capita['Population, total']
# %%
#sheets for change in healthcare expenditure
change_values=data.query('param=="Current health expenditure per capita (current US$)" or param=="Military expenditure (current USD)"')
change_values=change_values[['code','param','2009','2017']]
change_percent=data.query('param=="Military expenditure (percent of GDP)" or param=="Current health expenditure (percent of GDP)"')
change_values.pivot(index="code",columns="param",values='2017')
#%%
#sheets for change in education expenditure
