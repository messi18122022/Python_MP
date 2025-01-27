# Bibliotheken importieren
import matplotlib.pyplot as plt

# a) RNA einlesen und Verteilung berechnen
with open('rna/rna_sequence.txt', 'r') as file:
    rna = file.read().strip().replace('\n', '')

# Basen zählen
basen_count = {
    'A': rna.count('A'),
    'U': rna.count('U'),
    'G': rna.count('G'),
    'C': rna.count('C')
}

# Kreisdiagramm erstellen
plt.figure(figsize=(8, 8))
plt.pie(basen_count.values(), 
        labels=basen_count.keys(),
        autopct='%1.1f%%')
plt.title('RNA Basenverteilung')
plt.savefig('rna_verteilung.png')
plt.close()

# b) RNA in DNA umwandeln
dna = rna.replace('U', 'T')
with open('dna_output.txt', 'w') as file:
    file.write(dna)

# c) GC-Gehalt berechnen
gc_gehalt = (basen_count['G'] + basen_count['C']) / len(rna) * 100

# Balkendiagramm für GC-Gehalt
plt.figure(figsize=(10, 3))
plt.barh(['GC-Gehalt'], [gc_gehalt])
plt.xlim(0, 100)
plt.xlabel('Prozent')
plt.title(f'GC-Gehalt: {gc_gehalt:.1f}%')
plt.savefig('gc_gehalt.png')
plt.close()

# Ergebnisse ausgeben
print(f"Basenhäufigkeit: {basen_count}")
print(f"GC-Gehalt: {gc_gehalt:.1f}%")
print("DNA-Sequenz wurde in 'dna_output.txt' gespeichert")