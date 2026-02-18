#Q11_Reshape data from wide to long format using melt().

import pandas as pd
Datasets = pd.DataFrame({
        "City": ["Bhopal","New York","London"],
        "January":[56,18,34],
        "Febuary":[34,56,23]
    })
print(Datasets)
reshape = Datasets.melt(
                   id_vars= "City",
                   value_vars=["January","Febuary"],
                   var_name="Month",
                   value_name="Temperture"
        )
print("Dataset after reshape using melt():\n",reshape)
