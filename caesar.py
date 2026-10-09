alphabet = "abcdefghijklmnopqrstuvwxyz"

text =  input("Text: ")
schluessel = int(input("Schlüssel: "))

ergebnis = ""

text = text.replace ("ä","ae")
text = text.replace ("ö","oe")
text = text.replace ("ü","ue")

text = text.replace ("Ä","Ae")
text = text.replace ("Ö","Oe")
text = text.replace ("Ü","Ue")

text = text.replace ("ß", "ss")

for zeichen in text:
    if zeichen.lower() in alphabet:
        zeichenIsLower = zeichen.isupper()
        position = alphabet.index(zeichen.lower())
        neu_position = (position + schluessel) %26
        neuer_buchstabe = alphabet[neu_position]
        if zeichenIsLower:
            neuer_buchstabe = neuer_buchstabe.upper()

        ergebnis = ergebnis + neuer_buchstabe
    else:
        ergebnis = ergebnis + zeichen
    
print(ergebnis)

#raute test
