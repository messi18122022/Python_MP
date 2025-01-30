def primfaktorzerlegung(n):
    faktoren = []
    teiler = 2
    
    while n > 1:
        while n % teiler == 0:
            faktoren.append(teiler)
            n = n // teiler
        teiler += 1
        if teiler * teiler > n:
            if n > 1:
                faktoren.append(n)
            break
            
    return faktoren

# Beispiel zur Verwendung:
zahl = 84
ergebnis = primfaktorzerlegung(zahl)
print(f"Die Primfaktoren von {zahl} sind: {ergebnis}")