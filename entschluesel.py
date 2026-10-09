alphabet = "abcdefghijklmnopqrstuvwxyz"

text =  input("Verschlüsselter Text: ")
schluessel = int(input("Schlüssel: "))

ergebnis = ""

for zeichen in text:
    if zeichen.lower() in alphabet:
        zeichenIsUpper = zeichen.isupper()
        position = alphabet.index(zeichen.lower())
        neu_position = (position - schluessel) % 26
        neuer_buchstabe = alphabet[neu_position]
        
        if zeichenIsUpper:
            neuer_buchstabe = neuer_buchstabe.upper()

        ergebnis = ergebnis + neuer_buchstabe
    else:
        ergebnis = ergebnis + zeichen

ergebnis = ergebnis.replace("ae", "ä")
ergebnis = ergebnis.replace("oe", "ö")
ergebnis = ergebnis.replace("ue", "ü")

ergebnis = ergebnis.replace("Ae", "Ä")
ergebnis = ergebnis.replace("Oe", "Ö")
ergebnis = ergebnis.replace("Ue", "Ü")

ergebnis = ergebnis.replace("ss", "ß")

print(ergebnis)