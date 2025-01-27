# Benötigte Bibliotheken importieren
import pandas as pd
import matplotlib.pyplot as plt

# Datei einlesen
df = pd.read_csv("weather/weather_data.txt", header=None, sep=";")

df.columns = ["Stadt", "Datum", "Temperatur", "Luftfeuchtigkeit", "Luftdruck", "Windgeschwindigkeit"]

# Durchschnittswerte pro Stadt berechnen
durchschnitt = df.groupby('Stadt')[['Temperatur', 'Luftfeuchtigkeit']].mean()


# Balkendiagramm erstellen
ax = durchschnitt.plot(kind='barh', figsize=(10, 6))
plt.show()