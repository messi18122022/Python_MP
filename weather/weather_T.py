import pandas as pd

df_table = pd.read_csv("weather/weather_data.txt",sep=";",header=None)
print(df_table.head())

print(df_table[2].mean())
print(df_table[3].mean())


Berlin=[]
# Iteration über die Zeilen des DataFrames
for _, row in df_table.iterrows():  # Verwende iterrows(), um Zeilen durchzugehen
    if row[0] == "Berlin":  # Prüfe die erste Spalte (Index 0)
        Berlin.append(row[2])  # Füge den Wert der dritten Spalte (Index 2) zur Liste hinzu

print(Berlin)

