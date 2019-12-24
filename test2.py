import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(5).reshape(5,1))

# 删除第3行
backup = df.loc[2][0]
df.loc[2][0]= 10
print(df.head(10))
print('backup',backup)
df.drop([2], inplace=True)
#df = df.reset_index(drop=True)
print(df.head(10))
print('backup',backup)