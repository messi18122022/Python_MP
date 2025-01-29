import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("temperatur/temperatures.csv")

df = pd.DataFrame(data)

print(df["Temperature"].mean())
print(df["Temperature"].max())
print(df["Temperature"].min())

plt.hist(df["Temperature"])
plt.ylabel("Nutte")
plt.close()

plt.plot(df["Timestamp"],df["Temperature"])
plt.show()