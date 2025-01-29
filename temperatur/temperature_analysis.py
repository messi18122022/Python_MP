import pandas as pd
import matplotlib.pyplot as plt

# Daten einlesen
df = pd.read_csv("temperatures.csv", parse_dates=["Timestamp"])

# a) Berechnungen
avg_temp = df["Temperature"].mean()
min_temp = df["Temperature"].min()
max_temp = df["Temperature"].max()

print(f"Durchschnittstemperatur: {avg_temp:.2f}°C")
print(f"Minimale Temperatur: {min_temp:.2f}°C")
print(f"Maximale Temperatur: {max_temp:.2f}°C")

# Histogramm der Temperaturverteilung
plt.figure()
plt.hist(df["Temperature"], bins=10, edgecolor="black")
plt.xlabel("Temperatur (°C)")
plt.ylabel("Häufigkeit")
plt.title("Histogramm der Temperaturverteilung")
plt.show()

# b) Temperaturverlauf über die Zeit
plt.figure()
plt.plot(df["Timestamp"], df["Temperature"], marker="o", linestyle="-", label="Temperatur")
plt.scatter(df["Timestamp"][df["Temperature"].idxmax()], df["Temperature"].max(), color="red", label="Max Temp")
plt.scatter(df["Timestamp"][df["Temperature"].idxmin()], df["Temperature"].min(), color="blue", label="Min Temp")
plt.xlabel("Zeit")
plt.ylabel("Temperatur (°C)")
plt.title("Temperaturverlauf über die Zeit")
plt.legend()
plt.show()

# c) Temperatur-Kategorisierung
def categorize_temp(temp):
    if temp < 10:
        return "Kalt"
    elif temp <= 25:
        return "Mild"
    else:
        return "Heiß"

df["Kategorie"] = df["Temperature"].apply(categorize_temp)
category_counts = df["Kategorie"].value_counts()

# Kreisdiagramm
plt.figure()
category_counts.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Temperatur-Kategorien")
plt.show()
