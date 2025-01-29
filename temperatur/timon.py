import pandas as pd
from matplotlib import pyplot as plt

df_csv = pd.read_csv("temperatur/temperatures.csv")
durchschnitt= df_csv["Temperature"].mean()
minimum=df_csv["Temperature"].min()
maximum=df_csv["Temperature"].max()

print(durchschnitt,minimum,maximum)


df_csv.hist()
plt.xlabel("nutte")
plt.show()
plt.close

plt.plot(df_csv["Timestamp"],df_csv["Temperature"])
plt.show()