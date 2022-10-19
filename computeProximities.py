import math 
import pandas as pd
data = pd.read_csv('output/country_hsproduct6digit_2019.csv')

hs_product_code = pd.unique(data['hs_product_code'])
location_code = pd.unique(data['location_code'])
location_id = pd.unique(data['location_id'])
print(data.head(30))
print(hs_product_code)
total_export = pd.DataFrame(data['export_value']).sum()
total_import = pd.DataFrame(data['import_value']).sum()


for i in range(0, len(location_id)):
	for j in range(0, len(hs_product_code)):
		print("i", location_id[i], "j", hs_product_code[j])
		print("line", data[(data['location_id'] == location_id[i]) & (data['hs_product_code'] == hs_product_code[j])])
		X_cp = data[(data['location_id'] == location_id[i]) & (data['hs_product_code'] == hs_product_code[j])]['export_value']
		if math.isnan(X_cp):
			X_cp = 0
		else:
			X_cp = int(X_cp)

		print("X_cp", X_cp)
		#RCA_cp =	X_cp / (\sum_c X_cp)			
		#			/
		#			(\sum_p X_cp) / \sum_cp X_cp
		#X_cp = pd.DataFrame(data['export_value']).sum()



print("total_export", total_export)
print("total_import", total_import)
for i in range(0, len(hs_product_code)):
	#print("Processing", hs_product_code[i], "...")
	test=1
