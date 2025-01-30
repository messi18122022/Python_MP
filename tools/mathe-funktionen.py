# Funktion zur Prüfung, ob eine Zahl eine Primzahl ist
def ist_primzahl(zahl):
    # Wenn die Zahl kleiner als 2 ist, ist sie keine Primzahl
    if zahl < 2:
        return False
    
    # Wir prüfen, ob die Zahl durch irgendeine Zahl bis zur Wurzel teilbar ist
    # Wir müssen nur bis zur Wurzel prüfen, da größere Teiler redundant sind
    for teiler in range(2, int(zahl ** 0.5) + 1):
        if zahl % teiler == 0:
            return False
    
    return True

# Funktion zur Berechnung der Fibonacci-Folge bis zur n-ten Stelle
def fibonacci(n):
    # Die ersten beiden Zahlen der Fibonacci-Folge sind 0 und 1
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Liste mit den ersten zwei Fibonacci-Zahlen
    fib_liste = [0, 1]
    
    # Berechne die weiteren Zahlen durch Addition der zwei vorherigen
    while len(fib_liste) < n:
        nächste_zahl = fib_liste[-1] + fib_liste[-2]
        fib_liste.append(nächste_zahl)
    
    return fib_liste

# Funktion zur Berechnung des größten gemeinsamen Teilers (ggT)
def ggt(a, b):
    # Verwende den Euklidischen Algorithmus
    while b != 0:
        # Speichere b temporär, da wir es noch brauchen
        temp = b
        # Neues b ist der Rest der Division a/b
        b = a % b
        # Neues a ist das alte b
        a = temp
    return a

# Funktion zur Faktorisierung einer Zahl
def faktorisiere(zahl):
    faktoren = []
    teiler = 2
    
    # Teile die Zahl solange durch mögliche Primfaktoren
    while teiler <= zahl:
        if zahl % teiler == 0:
            # Füge den Faktor zur Liste hinzu
            faktoren.append(teiler)
            # Teile die Zahl durch den gefundenen Faktor
            zahl = zahl // teiler
        else:
            # Wenn die aktuelle Zahl kein Teiler ist, erhöhe den Teiler
            teiler += 1
            
    return faktoren

# Beispiele zur Verwendung der Funktionen:
if __name__ == "__main__":
    # Teste Primzahl-Funktion
    zahl = 17
    print(f"Ist {zahl} eine Primzahl? {ist_primzahl(zahl)}")
    
    # Teste Fibonacci-Funktion
    n = 8
    print(f"Die ersten {n} Fibonacci-Zahlen sind: {fibonacci(n)}")
    
    # Teste GGT-Funktion
    a, b = 48, 36
    print(f"Der GGT von {a} und {b} ist: {ggt(a, b)}")
    
    # Teste Faktorisierungs-Funktion
    zahl = 84
    print(f"Die Primfaktoren von {zahl} sind: {faktorisiere(zahl)}")
