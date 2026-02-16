import numpy as np
import pandas as pd
import matplotlib.pyplot as ply

df=pd.read_csv("Titanic.csv")

df.head()

df.isna().any()

df.info()

df.describe()

df.groupby('sex')['age']
