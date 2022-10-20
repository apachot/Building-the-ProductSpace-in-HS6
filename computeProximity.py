import numpy as np
import pandas as pd
data = pd.read_csv('output/M_cp.csv', header=0, index_col=0)
print("data shape=", data.shape)

M = data.to_numpy()
print("M shape=", data.shape)

hs_product_code = pd.read_csv('output/hs_product_code.csv', header=0, index_col=0).values.tolist()

print("hs_product_code", hs_product_code)
#following https://www.openstudio.fr/2020/11/26/autour-des-concepts-de-complexite-economique/

#print(data)

Proximity = []

print("len(hs_product_code)", len(hs_product_code))
for i in range(0, len(hs_product_code)):
	for j in range (0, len(hs_product_code)):

		#Proximity_p1p2 = 	min(
		#						(\sum_c Mcp1Mcp2) / (\sum_c Mcp1)
		#					,
		#						(\sum_c Mcp1Mcp2) / (\sum_c Mcp2)
		#					)
	
		#print("i", i)
		#print("j", j)

		listMcp1 = M[:,i]
		listMcp2 = M[:,j]
		
		#print("listMcp1.shape", listMcp1.shape)
		#print("listMcp2.shape", listMcp2.shape)
		
		#print(listMcp1.shape)
		#print(listMcp2.shape)
		
		Mcp1Mcp2 = [x*y for x,y in zip(listMcp1,listMcp2)]
		#print("Mcp1Mcp2", Mcp1Mcp2)

		sum_c_Mcp1Mcp2 = int(pd.DataFrame(Mcp1Mcp2).sum())
		#print("sum_c_Mcp1Mcp2", sum_c_Mcp1Mcp2)

		sum_c_Mcp1 = int(pd.DataFrame(listMcp1).sum())
		#print("sum_c_Mcp1", sum_c_Mcp1)

		sum_c_Mcp2 = int(pd.DataFrame(listMcp2).sum())
		#print("sum_c_Mcp2", sum_c_Mcp2)

		if ((sum_c_Mcp1 > 0) and (sum_c_Mcp2 > 0) and (sum_c_Mcp1Mcp2 > 0)):
			P = np.minimum((sum_c_Mcp1Mcp2/sum_c_Mcp1) , (sum_c_Mcp1Mcp2/sum_c_Mcp2))
			hs1 = hs_product_code[i][0]
			hs2 = hs_product_code[j][0]
			
			Proximity.append([hs1, hs2, P])
			print(i)
			
		else:
			P = 0
	pd.DataFrame(Proximity).to_csv('output/HS6_Proximities.csv')


pd.DataFrame(Proximity).to_csv('output/HS6_Proximities.csv')

		
