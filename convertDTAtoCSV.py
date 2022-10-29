import pandas as pd
dta_file = "country_hsproduct6digit_year.dta"
print("loading ", dta_file, "...")
data = pd.io.stata.read_stata('input/'+dta_file)
print("...Done")
years = pd.unique(data['year'])
print(years)


for i in years:
	#range(1995, 2020):
	print("Processing year", i)
	data_year = data[data['year'] == int(i)]
	data_year.to_csv('input/country_hsproduct6digit_'+str(i)+'.csv')
	print("...Done")

	