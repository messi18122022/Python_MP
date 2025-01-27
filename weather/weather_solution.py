# Bibliotheken importieren
import matplotlib.pyplot as plt

# Daten einlesen und verarbeiten
data = {}  # Dictionary für die Daten jeder Stadt

with open('weather/weather_data.txt', 'r') as file:
    for line in file:
        # Zeile aufteilen nach Semikolon
        stadt, datum, temp, feuchte, druck, wind = line.strip().split(';')
        
        # Werte in float umwandeln
        temp = float(temp)
        feuchte = float(feuchte)
        wind = float(wind)
        
        # Daten der Stadt hinzufügen
        if stadt not in data:
            data[stadt] = {
                'temp': [],
                'feuchte': [],
                'datum': [],
                'wind': []
            }
        
        data[stadt]['temp'].append(temp)
        data[stadt]['feuchte'].append(feuchte)
        data[stadt]['datum'].append(datum)
        data[stadt]['wind'].append(wind)

# a) Durchschnitte berechnen und Balkendiagramm erstellen
plt.figure(figsize=(10, 6))

staedte = list(data.keys())
x = range(len(staedte))

# Durchschnittstemperaturen
temp_mittel = [sum(data[stadt]['temp'])/len(data[stadt]['temp']) for stadt in staedte]
# Durchschnittsfeuchtigkeit
feuchte_mittel = [sum(data[stadt]['feuchte'])/len(data[stadt]['feuchte']) for stadt in staedte]

# Zwei Balken pro Stadt
plt.bar([i-0.2 for i in x], temp_mittel, width=0.4, label='Temperatur')
plt.bar([i+0.2 for i in x], feuchte_mittel, width=0.4, label='Luftfeuchtigkeit')

plt.xticks(x, staedte)
plt.legend()
plt.title('Durchschnittswerte pro Stadt')
plt.savefig('durchschnitt.png')
plt.close()

# b) Temperaturverlauf
plt.figure(figsize=(10, 6))
for stadt in data:
    plt.plot(data[stadt]['datum'], data[stadt]['temp'], label=stadt, marker='o')

plt.title('Temperaturverlauf')
plt.xlabel('Datum')
plt.ylabel('Temperatur (°C)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperatur_verlauf.png')
plt.close()

# c) Extreme finden
max_temp = -float('inf')
min_temp = float('inf')
max_wind = -float('inf')
max_temp_info = ''
min_temp_info = ''
max_wind_info = ''

for stadt in data:
    for i in range(len(data[stadt]['temp'])):
        # Höchste Temperatur
        if data[stadt]['temp'][i] > max_temp:
            max_temp = data[stadt]['temp'][i]
            max_temp_info = f"{stadt} am {data[stadt]['datum'][i]}: {max_temp}°C"
        
        # Niedrigste Temperatur
        if data[stadt]['temp'][i] < min_temp:
            min_temp = data[stadt]['temp'][i]
            min_temp_info = f"{stadt} am {data[stadt]['datum'][i]}: {min_temp}°C"
        
        # Höchste Windgeschwindigkeit
        if data[stadt]['wind'][i] > max_wind:
            max_wind = data[stadt]['wind'][i]
            max_wind_info = f"{stadt} am {data[stadt]['datum'][i]}: {max_wind} m/s"

# Ergebnisse ausgeben
print("Extreme Werte:")
print(f"Höchste Temperatur: {max_temp_info}")
print(f"Niedrigste Temperatur: {min_temp_info}")
print(f"Höchste Windgeschwindigkeit: {max_wind_info}")