# Benötigte Bibliotheken importieren
import matplotlib.pyplot as plt

# Teilaufgabe a)
# Datei einlesen
with open("protein/sequence_file.txt","r") as file:
    protein = file.read().strip().replace("\n","")

# Aminosäurenhäufigkeiten berechnen
amino_acid_counts = {}

for amino_acid in protein:
    if amino_acid not in amino_acid_counts:
        amino_acid_counts[amino_acid] = 1
    else:
        amino_acid_counts[amino_acid] += 1

# In Diagramm darstellen
plt.figure(figsize=(5,5))
plt.title("Aminosäuren-Häufigkeiten im Protein")
plt.bar(amino_acid_counts.keys(),amino_acid_counts.values())
plt.xlabel("Aminosäure")
plt.ylabel("absolute Häufigkeit")
plt.savefig("protein/output/AA_Häufigkeiten.png",dpi=300)
plt.close()

# Teilaufgabe b)
# Hydrophile und Hydrophobe Aminosäuren als Tuples definieren
hydrophobic_amino_acids = ("A","I","L","M","F","W","V")
hydrophilic_amino_acids = ("R","N","D","C","E","Q","G","H","K","P","S","T","Y")


hydrophobic_aa_counts = 0
hydrophilic_aa_counts = 0

for amino_acid in protein:
    if amino_acid in hydrophilic_amino_acids:
        hydrophilic_aa_counts += 1
    if amino_acid in hydrophobic_amino_acids:
        hydrophobic_aa_counts += 1

hydrophilic_aa_fraction = hydrophilic_aa_counts / len(protein) * 100
hydrophobic_aa_fraction = hydrophobic_aa_counts / len(protein) * 100

plt.figure(figsize=(5,5))
plt.title("Verteilung Polare vs Unpolare AA's im Protein")
plt.pie([hydrophobic_aa_counts,hydrophilic_aa_counts],labels=["polar","unpolar"],autopct='%1.1f%%')
plt.savefig("protein/output/AA_Häufigkeiten_Polarität.png",dpi=300)
plt.close()

# Teilaufgabe c)
motiv = "RNM"
motiv_count = 0
for motiv in protein:
    if motiv in protein:
        motiv_count += 1

print(motiv_count)