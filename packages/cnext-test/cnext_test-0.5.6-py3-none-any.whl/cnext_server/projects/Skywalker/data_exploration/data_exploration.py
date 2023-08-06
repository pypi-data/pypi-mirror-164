import cnextlib.dataframe as cd
df_housing = cd.DataFrame("data/housing_data/data.csv")
df_housing['LotFrontage'] = df_housing['LotFrontage'].fillna(method='ffill')
df_antibiotics = cd.DataFrame("data/bokeh/antibiotics.csv")