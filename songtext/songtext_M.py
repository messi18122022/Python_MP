# Benötigte Bibliotheken importieren
import matplotlib.pyplot as plt

# Datei einlesen
with open("songtext/songtext.txt","r") as file:
    wörter = []
    for line in file:
        wörter.append(line.strip())

längen = {}
for wort in wörter:
    if len(wort) not in längen.keys():
        längen[len(wort)] = 1
    else:
        längen[len(wort)] += 1

plt.bar(längen.keys(),längen.values())
plt.show()
