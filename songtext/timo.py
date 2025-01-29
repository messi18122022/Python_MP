from matplotlib import pyplot as plt
import string


alle_wort=[]
with open("songtext/songtext.txt", "r") as file:
    for line in file:
        for wort in line.strip().split():  # Entfernt Leerzeichen & teilt die Zeile in Wörter
            alle_wort.append(wort)   # Speichert jedes Wort mit seiner Länge

print(alle_wort)  # Debugging: Zeigt die Wörter und ihre Längen

# Wörter nach Länge zählen
menge_wort = dict()
for i in alle_wort:
    if len(i) in menge_wort:
        menge_wort[len(i)]+=1
    else:
        menge_wort[len(i)] =1

print(menge_wort)  # Gibt die Anzahl der Wörter nach Länge aus


plt.figure(figsize=(8, 5))
plt.bar(menge_wort.keys(), menge_wort.values(), color="orange")
plt.show()




#b) Transformation:
   #- Ersetze alle Vokale durch ihre Position im Alphabet:
    # * a → 1
     #* e → 5
#     * i → 9
 #    * o → 15
  #   * u → 21
   #- Konsonanten bleiben unverändert
 #  - Beispiel: "Hallo" wird zu "H1ll15"
  # - Gib den transformierten Text in der Konsole aus

with open("songtext/songtext.txt", "r") as file:
    transformieren=file.read().strip().replace("a","1").replace("e","5").replace("i","9").replace("o","15").replace("u","21")
    print(transformieren)


    alphabet=" " + string.ascii_lowercase
    print(alphabet)
    
    konsonant=transformieren.replace("\n","")
    print(konsonant)
    menge_konso=dict()
    for konso in transformieren:
        if konso in alphabet:
            if konso in menge_konso:
                menge_konso[konso]+=1
            else:
                menge_konso[konso]=1
    print(menge_konso)


plt.figure(figsize=(8, 5))
plt.bar(menge_konso.keys(), menge_konso.values(), color="orange")
plt.show()

konsonanten_sortiert=sorted(menge_konso.items())
print(konsonanten_sortiert)