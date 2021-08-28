import pandas as pd
df=pd.read_csv("surveys.csv")
print (df.head)
print(df.shape)
df.info()
grupo_datos = df.groupby('sex')
print (grupo_datos.describe())
conteo_especies = df.groupby('species_id')['record_id'].count()
print(conteo_especies)
import matplotlib.pyplot as pl
print (conteo_especies.plot(kind='bar'));