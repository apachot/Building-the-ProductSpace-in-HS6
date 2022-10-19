import pandas as pd
data = pd.io.stata.read_stata('input/country_hsproduct6digit_year.dta')
data = data[data['year'] == 2019]
data.to_csv('input/country_hsproduct6digit_2019.csv')