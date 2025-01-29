import matplotlib.pyplot as plt
from collections import Counter

# Datei einlesen
woerter = []
with open('songtext/songtext.txt', 'r') as file:
    # Jeden Zeile einzeln einlesen
    for line in file:
        # Leerzeichen entfernen und zur Liste hinzufügen
        wort = line.strip()
        woerter.append(wort)

# Länge jedes Wortes berechnen
wortlaengen = []
for wort in woerter:
    laenge = len(wort)
    wortlaengen.append(laenge)

# Häufigkeiten zählen
laengen_haeufigkeit = Counter(wortlaengen)

# Daten für das Diagramm vorbereiten
laengen = list(laengen_haeufigkeit.keys())
laengen.sort()  # Sortieren für bessere Darstellung

# Häufigkeiten in der richtigen Reihenfolge
haeufigkeiten = []
for laenge in laengen:
    haeufigkeit = laengen_haeufigkeit[laenge]
    haeufigkeiten.append(haeufigkeit)

# Balkendiagramm erstellen
plt.figure(figsize=(10, 6))
plt.bar(laengen, haeufigkeiten)
plt.title('Verteilung der Wortlängen')
plt.xlabel('Wortlänge')
plt.ylabel('Anzahl der Wörter')

# Werte über den Balken anzeigen
for i in range(len(laengen)):
    x_position = laengen[i]
    y_value = haeufigkeiten[i]
    plt.text(x_position, y_value, str(y_value), 
             ha='center', va='bottom')

plt.show()

# Zur Kontrolle auch als Text ausgeben
print("Wortlängen-Statistik:")
for laenge in laengen:
    anzahl = laengen_haeufigkeit[laenge]
    print(f"Länge {laenge}: {anzahl} Wörter")