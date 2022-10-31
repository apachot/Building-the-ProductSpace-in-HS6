from preprocessing import Pretraitement

if __name__ == "__main__":
    hs_code = Pretraitement.read_data()
    total_export, total_import,sum_export_by_product,sum_export_by_country,export_by_product_by_country = Pretraitement.sum_international_trade(hs_code)
    rca, matrix = Pretraitement.get_rca(sum_export_by_product, sum_export_by_country, export_by_product_by_country, total_export)