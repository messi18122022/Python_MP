# Benötigte Bibliotheken importieren
import matplotlib.pyplot as plt
import string

# Teilaufgabe a)
# Datei einlesen
with open("songtext/songtext.txt","r") as file:
    wörter = []
    for line in file:
        wörter.append(line.strip())


# Längen zählen und in dict speichern
längen = {}
for wort in wörter:
    if len(wort) not in längen.keys():
        längen[len(wort)] = 1
    else:
        längen[len(wort)] += 1

# Plotten
plt.bar(längen.keys(),längen.values())
plt.xticks(range(2,12,1))
# plt.show()
plt.close()

# Teilaufgabe b)
with open("songtext/songtext.txt","r") as file:
    transformiert = file.read().replace("a","1").replace("e","5").replace("i","9").replace("o","15").replace("u","21")

# Teilaufgabe c)
transformiert = transformiert.replace("\n","")

alphabet = string.ascii_lowercase

Konsonanten_Counts = {}
for i in transformiert:
    if i  in alphabet:
        if i not in Konsonanten_Counts.keys():
            Konsonanten_Counts[i] = 1
        else:
            Konsonanten_Counts[i] += 1

plt.bar(Konsonanten_Counts.keys(),Konsonanten_Counts.values())
plt.show()

b = sorted(Konsonanten_Counts,reverse=True)
