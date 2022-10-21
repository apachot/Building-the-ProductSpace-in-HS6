# Building the ProductSpace in HS6

Teams at Harvard University have been working on modeling the economic complexity of countries based on trade analysis (hidalgo_product_2007, bahar_neighbors_2012, hausmann_atlas_2011, hausmann_growth_2005). By observing the exports of each country, they address the question of what the country knows how to produce and thus trace the contours of its productive know-how. This productive know-how is the key to a country's economic prosperity and may require a complex network of specific skills acquired over several years. The indicator ECI is the indicator of the complexity of this country's productive know-how.

The computation of the proximity between two product classes starts with the intermediate calculation of the revealed competitive advantage (RCA) of each product *p* for each country *c*.

## Revealed Competitive Advantage (RCA)

If ![equation](https://latex.codecogs.com/gif.latex?X_{cp}) represents the exports of product *p* by country *c*, then the RCA (balassa_trade_1965) that country *c* has for product *p* can be expressed as a function of exports:

![equation](https://latex.codecogs.com/gif.latex?RCA_{cp}%20=%20\frac{X_{cp}}{\sum_c{X_{cp}}}%20/%20\frac{\sum_p{X_{cp}}}{\sum_{c,p}{X_{cp}}})

Note that a country *c* is con
dered to export a product *p* if and only if ![equation](https://latex.codecogs.com/gif.latex?RCA_{cp}) is greater than 1.

![equation](https://latex.codecogs.com/gif.latex?M_%7Bcp%7D%20%3D%20%5Cleft%20%5C%7B%20%5Cbegin%7Barray%7D%7Br%20c%20l%7D%201%20%26%20if%20%5C%3A%20%5Cmathit%7BRCA_%7Bcp%7D%7D%5Cgeq%201%3B%20%5C%5C%200%20%26%20else%20%5Cend%7Barray%7D%20%5Cright%20.)

For example, in 2019, wine accounted for *0.136%* of world trade (*$33.8* billion) with total world exports of *24795* billion.

Of this total, Georgia exported nearly $193 million worth of wine. Georgia's total exports for that year amounted to $7.81 billion, with wine accounting for 2.47% of Georgia's exports. Georgian wine represents 0.57% of wine exports in the world while Georgian exports of all products combined represent 0.03% of world exports.

We obtain a 18.12 for wine in Georgia which means that Georgia exports 18.12 times its fair share of wine exports, so we can say that Georgia has a significant RCA on wine.

## Measurement of proximities between products based on the analysis of co-exports

The analysis of the products exported by a country implicitly informs us about the proximity of the production know-how of these products. For example, if "beef" and "flour" products are more often co-exported than "beef" and "electronic cards" products, this indicates that the know-how needed to produce meat is closer to that of flour than to that of electronic cards. Based on the large-scale analysis of the types of products exported by country, the Harvard team was able to measure the proximity of productive know-how (also called "productive proximity") between each type of product and construct a graph of the productive space. The results obtained for each country in the world can be consulted on the website of the Economic Atlas of Complexity: https://atlas.cid.harvard.edu.

![Product Space in HS4 (hausmann_atlas_2011)](https://www.openstudio.fr/app/uploads/2020/11/Screenshot-2020-11-25-at-17.31.09.png)

The calculation of the productive proximity between each product is done by searching for each pair of products {*p<sub>1</sub>*;*p<sub>2</sub>*} the smallest percentage of times that *p<sub>1</sub>* is co-exported with *p<sub>2</sub>* :

![equation](https://latex.codecogs.com/gif.latex?%5Cphi_%7Bp_1%2Cp_2%7D%20%3D%20min%20%5Cleft%20%5C%7B%20%5Cfrac%7B%5Csum_cM_%7Bcp_1%7DM_%7Bcp_2%7D%7D%7B%5Csum_cM_%7Bcp_1%7D%7D%20%7E%5Cmiddle%7C%7E%20%5Cfrac%7B%5Csum_cM_%7Bcp_1%7DM_%7Bcp_2%7D%7D%7B%5Csum_cM_%7Bcp2%7D%7D%20%5Cright%20%5C%7D)

The concept of economic complexity is based on the idea that the evolution of a country's productive know-how takes place progressively by making "productive jumps" from the manufacture of one type of product to another type of product close to it in the productive space. 

You can find the datasets concerning the proximity measures between products and the network associated with the Product Space on the Harvard dataverse : https://dataverse.harvard.edu/dataverse/atlas

## Extension of the available data sets in HS1992 on 6 digits

We have built a full version of Product Space (on 6 digits) from the work of Haussman and Hidalgo on Economic Complexity presented above. It is an enriched version with more than 5000 product classes. 

For our research work and in particular the Atlas of Productive Synergies (https://atlas.productive-synergies.com), the switch to HS6 is important because we need precision to make recommendations to companies. All the credit obviously goes to Harvard, I only declined their equations on the complete data of foreign trade (https://dataverse.harvard.edu/file.xhtml?fileId=6402163&version=5.0). 

![Product Space in HS6](https://raw.githubusercontent.com/apachot/Building-the-ProductSpace-in-HS6/e857ca237197f384a9a41668321a61fdbbbe72da/gephi/HS6_proximities.svg)

## Download

Download available on https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/T9W75F

You can refer to this dataset:

```
@data{DVN/T9W75F_2022,
author = {PACHOT, Arnault},
publisher = {Harvard Dataverse},
title = {{Product Space Networks (6 digits)}},
year = {2022},
version = {V1},
doi = {10.7910/DVN/T9W75F},
url = {https://doi.org/10.7910/DVN/T9W75F}
}
```

## References

Hidalgo, C. A., Klinger, B., Barabasi, A.-L., & Hausmann, R. (2007). The Product Space Conditions the Development of Nations. Science, 317(5837), 482‑487. https://doi.org/10.1126/science.1144581

Bahar, D., Hausmann, R., & Hidalgo, C. A. (2014). Neighbors and the evolution of the comparative advantage of nations : Evidence of international knowledge diffusion? Journal of International Economics, 92(1), 111‑123. https://doi.org/10.1016/j.jinteco.2013.11.001

Hausmann, R., Hidalgo, C. A., Bustos, S., Coscia, M., Simoes, A., & Yildirim, M. A. (2013). The Atlas of Economic Complexity : Mapping Paths to Prosperity (2nd éd.). MIT Press. https://mitpress.mit.edu/index.php?q=books/atlas-economic-complexity

Hausmann, R., Rodrik, D., & Velasco, A. (2005). Growth Diagnostics.

Balassa, B. (1965). Trade Liberalisation and « Revealed » Comparative Advantage. The Manchester School, 33(2), 99‑123. https://doi.org/10.1111/j.1467-9957.1965.tb00050.x



