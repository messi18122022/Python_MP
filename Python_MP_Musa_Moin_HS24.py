import matplotlib.pyplot as plt
import pandas as pd

test = {"3":10, "4":20}
def increase(wert,dict):
    if wert in dict.keys():
        dict[wert] += 1
    else:
        dict[wert] = 1
    return dict


satz = "ich bin musa"

def count_characters(str):
    dict = {}
    for buchstabe in str:
        increase(buchstabe,dict)
    return dict

character_count = count_characters(satz)

plt.figure(figsize=(8, 5))
plt.bar(character_count.keys(), character_count.values(), color="orange")
plt.title("Balkendiagramm")
#plt.show()
plt.close()

df = pd.read_table("compounds.tsv")



grösste_molmasse = df["Mass"].max()
kleinste_molmasse = df["Mass"].min()
durch_molmasse = df["Mass"].mean()


gefiltert = df[df["Mass"] > 0]
kleinste_molmasse = gefiltert["Mass"].min()
print(kleinste_molmasse)

gefiltert2 = gefiltert[df["Mass"] < 2000]


plt.figure(figsize=(8, 5))
plt.hist(gefiltert2["Mass"], bins=100, color="green", edgecolor="black")
plt.title("Histogramm")
plt.xlabel("Werte")
plt.ylabel("Häufigkeit")
#plt.show()





print(df[df["Formula"].duplicated()==True])

