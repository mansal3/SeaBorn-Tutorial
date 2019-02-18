                          # -----Seaborn-----#
# It is one of the python data visualization library which is based on matplotlib.
# Used for and which will provide high interactive for drawing attractive and informative graphs.
# Seaborn library is used for making statistical graphics in Python. 
  # It is built on top of matplotlib and closely integrated with pandas data structures.
# Its main aim is to make visualization on data by eploring the data & understanding the data.
# to make understand and produce informative plots.  

     #  https://seaborn.pydata.org/introduction.html
     

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
iris = pd.read_csv('/home/karthik/Downloads/iris.csv')
iris.head()
print(iris.shape)
print(iris.describe)
iris.plot(kind='box', sharex=False, sharey=False)
 
import pandas as pd
