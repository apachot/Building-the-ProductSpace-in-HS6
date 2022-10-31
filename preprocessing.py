import pandas as pd
import numpy as np
from pathlib import Path

class Pretraitement:

    def __init__(self):
        self.path_in = Path("input/")
        self.path_out = Path("output/")

    def read_data(self):
        exportation = pd.read_csv('input/country_hsproduct6digit_2019.csv')
        return exportation

    def sum_international_trade(data):
        total_export = data["export_value"].sum()
        total_import = data["import_value"].sum()
        sum_export_by_product = data.groupby(["product_id"])["export_value"].sum()
        sum_export_by_country = data.groupby(["location_id"])["export_value"].sum()
        export_by_product_by_country = data.groupby(["location_id","product_id"])["export_value"].sum()
        return total_export, total_import,sum_export_by_product,sum_export_by_country,export_by_product_by_country

    
    def get_rca(self,sum_export_by_product, sum_export_by_country, export_by_product_by_country, total_export):
        export_by_product_by_country.fillna(0)   
        final_data = pd.DataFrame(columns=["location_id", "product_id", "rca"], values=[export_by_product_by_country["location_id"], export_by_product_by_country["product_id"],np.nan])     
        rca_cp = final_data.apply(self.compute_rca(final_data,sum_export_by_product, sum_export_by_country, export_by_product_by_country, final_data["location_id"].unique(),final_data["product_id"].unique() ), axis=0)
        matrix = self.get_matrix(rca_cp)
        return rca_cp, matrix

    def compute_rca(self,final_data,sum_export_by_product, sum_export_by_country, export_by_product_by_country, total_export,i,j):
        try:
            final_data[(final_data["location_id"]==i) &(final_data["product_id"]==j),["rca"]] = (export_by_product_by_country[(export_by_product_by_country["location_id"]==i) & (export_by_product_by_country["location_id"]==j)] 
            / sum_export_by_product[sum_export_by_product["product_id"]==j]) / (sum_export_by_country[sum_export_by_country["country_id"]==i] /total_export)
        except ZeroDivisionError:
            final_data[(final_data["location_id"]==i) &(final_data["product_id"]==j),["rca"]] = 0
        return final_data


    @staticmethod
    def get_matrix(rca_cp):
        matrix =  pd.DataFrame(np.zeros((len((rca_cp["location_id"].unique.tolist()), len(rca_cp["product_code"].unique.tolist())))))
        
        
        # Au fait : 
        # Les petit suisses c'est bon pour la santé
        