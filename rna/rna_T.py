from matplotlib import pyplot as plt

with open("rna/rna_sequence.txt") as file:
    rna=file.read().strip().replace("\n","")

print(rna)

A=rna.count("A")
U=rna.count("U")
G=rna.count("G")
C=rna.count("C")

plt.pie([A,U,G,C],labels=["A","U","G","C"],autopct='%1.1f%%')
plt.show()


with open("rna/dna_output.txt", "w") as file:
    file.write(rna.replace("U","T"))
    file.close

GC_gehalt=((C+G)/(A+U+G+C))*100

plt.figure(figsize=(10, 6))

# Balkendiagramm
plt.bar("GC in %", GC_gehalt)

# Y-Achsenbereich anpassen
plt.ylim(0, 100)  # Bereich der y-Achse von 0 bis 20

# Titel und Achsenbeschriftung
#plt.title("Beispiel-Balkendiagramm mit angepasster Höhe")
#plt.xlabel("Kategorien")
#plt.ylabel("Werte")

# Grafik anzeigen
plt.show()