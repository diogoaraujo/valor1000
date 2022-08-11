import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
 
data = load_iris()
df = pd.DataFrame(data.data,
                  columns = data.feature_names)
 
# The scope of these changes made to
# pandas settings are local to with statement.
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)