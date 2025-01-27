# Benötigte Bibliotheken importieren
import matplotlib.pyplot as plt

# Teilaufgabe a)
# Datei einlesen
with open("rna/rna_sequence.txt","r") as file:
    rna = file.read().strip().replace("\n","")  # Zeilenumbrüche entfernen

# Basen zählen und in dict speichern
base_count = {"A": rna.count("A"),
              "G": rna.count("G"),
              "U": rna.count("U"),
              "C": rna.count("C")}

# Plot erstellen
plt.pie(base_count.values(),labels=base_count.keys(),autopct='%1.1f%%')
plt.savefig("rna/output/pie-plot_base_rna.png")
plt.close()

# Teilaufgabe b)
# alle U in rna mit T ersetzen und als dna speichern
dna = rna.replace("U","T")

# in Datei abspeichern
with open("rna/output/dna_output.txt","w") as file:
    file.write(dna)

# Teilaufgabe c)
# GC-Anteil berechnen
gc_anteil = (dna.count("G") + dna.count("C")) / len(dna) * 100

# Als horizontalen Balken darstellen
plt.figure(figsize=(10,3))
plt.barh("GC-Anteil",gc_anteil)
plt.xlim(0,100)
plt.savefig("rna/output/bar-plot_gc.png")

