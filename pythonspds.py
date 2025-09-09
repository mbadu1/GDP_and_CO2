import pandas as pd
file = pd.read_csv('https://github.com/nickeubank/MIDS_Data/raw/refs/heads/master/World_Development_Indicators/wdi_small_tidy_2015.csv')
file.head()
file[["Mortality rate, infant (per 1,000 live births)", "GDP per capita (constant 2010 US$)", "Country Name"]]
file.plot(kind="scatter", x="Mortality rate, infant (per 1,000 live births)", y="GDP per capita (constant 2010 US$)", alpha=0.7, title="Mortality rate, infant (per 1,000 live births) vs GDP per capita (constant 2010 US$)")
