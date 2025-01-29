# Songtext-Analyse

Die Datei "songtext.txt" enthält einen deutschen Songtext, bei dem jedes Wort in einer neuen Zeile steht.

a) Eingabe: Lies die Datei ein und analysiere die Länge jedes Wortes.
   Erstelle ein Balkendiagramm, das zeigt, wie viele Wörter es mit jeder Länge gibt.
   Beispiel: 
   - 5 Wörter mit Länge 2
   - 12 Wörter mit Länge 3
   - usw.

b) Transformation:
   - Ersetze alle Vokale durch ihre Position im Alphabet:
     * a → 1
     * e → 5
     * i → 9
     * o → 15
     * u → 21
   - Konsonanten bleiben unverändert
   - Beispiel: "Hallo" wird zu "H1ll15"
   - Gib den transformierten Text in der Konsole aus

c) Analyse:
   - Zähle, wie oft jeder Konsonant im transformierten Text vorkommt
   - Stelle dies in einem Balkendiagramm dar
   - Sortiere die Konsonanten nach Häufigkeit absteigend

Zusätzliche Anforderungen:
- Ignoriere Satzzeichen und Zahlen im ursprünglichen Text
- Wandle alle Wörter in Kleinbuchstaben um, bevor du sie verarbeitest
- Behandle 'y' als Konsonant

Beispielausgabe für c):
- n: 45 mal
- r: 38 mal
- t: 32 mal
usw.

Hilfestellung:
- Nutze matplotlib für die Visualisierung
- Die Datei enthält nur ASCII-Zeichen (keine Umlaute)
- Leerzeichen am Anfang und Ende der Zeilen sollen ignoriert werden