# Bibliotheken importieren
import matplotlib.pyplot as plt

# Sequenz einlesen
with open('sequence.txt', 'r') as file:
    protein = file.read().strip()

# a) Aminosäuren zählen
amino_count = {}
for amino in protein:
    if amino in amino_count:
        amino_count[amino] += 1
    else:
        amino_count[amino] = 1

# Balkendiagramm erstellen
plt.figure(figsize=(12, 6))
plt.bar(amino_count.keys(), amino_count.values())
plt.title('Häufigkeit der Aminosäuren')
plt.xlabel('Aminosäure')
plt.ylabel('Anzahl')
plt.savefig('amino_haeufigkeit.png')
plt.close()

# b) Hydrophob/Hydrophil Analyse
hydrophob = 'AILMFWV'
hydrophil = 'RNDCEQGHKPSTY'

hydrophob_count = sum(protein.count(amino) for amino in hydrophob)
hydrophil_count = sum(protein.count(amino) for amino in hydrophil)

# Kuchendiagramm erstellen
plt.figure(figsize=(8, 8))
plt.pie([hydrophob_count, hydrophil_count], 
        labels=['Hydrophob', 'Hydrophil'],
        autopct='%1.1f%%')
plt.title('Verteilung hydrophober/hydrophiler Aminosäuren')
plt.savefig('hydrophob_hydrophil.png')
plt.close()

# c) Motiv "RNM" suchen
motiv = "RNM"
positionen = []
for i in range(len(protein)-2):
    if protein[i:i+3] == motiv:
        positionen.append(i+1)  # +1 für 1-basierte Position

# Ergebnisse ausgeben
print(f"Aminosäure-Häufigkeiten: {amino_count}")
print(f"\nHydrophobe Aminosäuren: {hydrophob_count}")
print(f"Hydrophile Aminosäuren: {hydrophil_count}")
print(f"\nPositionen des Motivs '{motiv}': {positionen}")