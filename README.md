# Building the ProductSpace in HS6

We propose a HS6 version of the famous Product Space developed by Harvard. If you want to know more about the Product Space, and the work on Economic Complexity, I invite you to visit https://atlas.cid.harvard.edu.

The version that can be found online is limited to product classes on 4 digits (about 1600 classes). Here we propose an enriched version with more than 5000 classes.

You can retrieve directly in the /output folder the proximity data between classes and the json network associated to the Product Space represented in 2D.

Proximity is defined as :

![equation](https://latex.codecogs.com/gif.latex?%5Cphi_%7Bp_1%2Cp_2%7D%20%3D%20min%20%5Cleft%20%5C%7B%20%5Cfrac%7B%5Csum_cM_%7Bcp_1%7DM_%7Bcp_2%7D%7D%7B%5Csum_cM_%7Bcp_1%7D%7D%20%7E%5Cmiddle%7C%7E%20%5Cfrac%7B%5Csum_cM_%7Bcp_1%7DM_%7Bcp_2%7D%7D%7B%5Csum_cM_%7Bcp2%7D%7D%20%5Cright%20%5C%7D)

![equation](https://latex.codecogs.com/gif.latex?%5Cmathit%7BRCA_%7Bcp%7D%7D%20%3D%20%5Cfrac%7BX_%7Bcp%7D%7D%7B%5Csum_c%7BX_%7Bcp%7D%7D%7D%20/%20%5Cfrac%7B%5Csum_p%7BX_%7Bcp%7D%7D%7D%7B%5Csum_%7Bc%2Cp%7D%7BX_%7Bcp%7D%7D%7D)

![equation](https://latex.codecogs.com/gif.latex?M_%7Bcp%7D%20%3D%20%5Cleft%20%5C%7B%20%5Cbegin%7Barray%7D%7Br%20c%20l%7D%201%20%26%20si%20%5C%3A%20%5Cmathit%7BRCA_%7Bcp%7D%7D%5Cgeq%201%3B%20%5C%5C%200%20%26%20else%20%5Cend%7Barray%7D%20%5Cright%20.)


The project is still under development, all data are not yet available.
