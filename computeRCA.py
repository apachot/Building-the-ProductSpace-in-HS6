import math 
import numpy as np
import pandas as pd
data = pd.read_csv('input/country_hsproduct6digit_2019.csv')

hs_product_code = pd.unique(data['hs_product_code'])
product_id = pd.unique(data['product_id'])
location_code = pd.unique(data['location_code'])
location_id = pd.unique(data['location_id'])
print(data.head(30))
#print(hs_product_code)
total_export = int(pd.DataFrame(data['export_value']).sum())
total_import = pd.DataFrame(data['import_value']).sum()


M = pd.DataFrame(np.zeros((len(location_id), len(hs_product_code))))
RCA = pd.DataFrame(np.zeros((len(location_id), len(hs_product_code))))

#print(M.head())


print("preprocessing")
tab_sum_c_X_cp = [int(pd.DataFrame(data[data['product_id'] == product_id[j]]['export_value']).sum()) for j in range(0, len(product_id))]
tab_sum_p_X_cp = [int(pd.DataFrame(data[data['location_id'] == location_id[i]]['export_value']).sum()) for i in range(0, len(location_id))]
print(tab_sum_c_X_cp)		
print("tab_sum_p_X_cp=")
print(tab_sum_p_X_cp)		
print("end preprocessing")

for i in range(0, len(location_id)):
	for j in range(0, len(product_id)):
		#print("line", data[(data['location_id'] == location_id[i]) & (data['hs_product_code'] == hs_product_code[j])])
		
		#RCA_cp =	X_cp / (\sum_c X_cp)			
		#			/
		#			(\sum_p X_cp) / \sum_cp X_cp
		#X_cp = pd.DataFrame(data['export_value']).sum()
		# https://www.openstudio.fr/2020/11/26/autour-des-concepts-de-complexite-economique/

		X_cp = data[(data['location_id'] == location_id[i]) & (data['product_id'] == product_id[j])]['export_value']
		if math.isnan(X_cp):
			X_cp = 0
		else:
			X_cp = int(X_cp)

		#print("X_cp", X_cp)

		#sum_c_X_cp = int(pd.DataFrame(data[data['hs_product_code'] == hs_product_code[j]]['export_value']).sum())
		sum_c_X_cp = tab_sum_c_X_cp[j]
		#print("sum_c_X_cp", sum_c_X_cp)

		#sum_p_X_cp = int(pd.DataFrame(data[data['location_id'] == location_id[i]]['export_value']).sum())
		sum_p_X_cp = tab_sum_p_X_cp [i]
		#print("sum_p_X_cp", sum_p_X_cp)

		sum_cp_X_cp = total_export
		#print("sum_cp_X_cp")

		if (sum_c_X_cp>0 and sum_cp_X_cp>0):
			RCA_cp = (X_cp / sum_c_X_cp) / (sum_p_X_cp / sum_cp_X_cp)
		else:
			RCA_cp = 0
		#print("RCA_cp", RCA_cp)
		RCA[i][j] = RCA_cp

		if (RCA_cp >= 1):
			M_cp = 1

			print("i", i, "j", j)
			print("location_id[i]", location_id[i], "product_id[j]", product_id[j])
			print("RCA_cp", RCA_cp)
			print("M_cp", M_cp)
			M[i][j] = 1
			
			M.to_csv('output/M_cp.csv')
			RCA.to_csv('output/RCA_cp.csv')
		else:
			M_cp = 0


