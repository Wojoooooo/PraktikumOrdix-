"""
Kleine Python-Demos für Einsteiger.
Start: python python_demos.py

WICHTIG: Diese Datei nicht "turtle.py", "qrcode.py" o.ä. nennen!
"""


def turtle_spirale():
    import turtle

    # Erlaubt mehrfaches Starten, auch wenn das Fenster vorher geschlossen wurde
    turtle.TurtleScreen._RUNNING = True

    winkel = input("Winkel eingeben (Enter = 59, probier auch 91 oder 121): ").strip()
    winkel = int(winkel) if winkel.isdigit() else 59

    screen = turtle.Screen()
    screen.title("Turtle-Spirale – Fenster anklicken zum Schließen")
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    farben = ["red", "orange", "yellow", "green", "blue", "purple"]

    try:
        for i in range(300):
            t.pencolor(farben[i % 6])
            t.forward(i)
            t.left(winkel)
        screen.exitonclick()
    except turtle.Terminator:
        pass  # Fenster wurde während des Zeichnens geschlossen


def qr_code():
    try:
        import qrcode
    except ImportError:
        print("Bibliothek fehlt. Installieren mit:  pip install qrcode[pil]")
        return

    import os
    import tkinter as tk

    text = input("Text oder Link für den QR-Code (Enter = python.org): ").strip()
    if not text:
        text = "https://www.python.org"

    dateiname = "mein_qr.png"
    qrcode.make(text).save(dateiname)
    print(f"QR-Code gespeichert unter: {os.path.abspath(dateiname)}")

    fenster = tk.Tk()
    fenster.title("QR-Code – mit dem Handy scannen")
    bild = tk.PhotoImage(file=dateiname)
    tk.Label(fenster, image=bild).pack(padx=10, pady=10)
    tk.Button(fenster, text="Schließen", command=fenster.destroy).pack(pady=(0, 10))
    fenster.mainloop()


def sprechen():
    try:
        import pyttsx3
    except ImportError:
        print("Bibliothek fehlt. Installieren mit:  pip install pyttsx3")
        return

    name = input("Wie heißt du? ").strip() or "Unbekannter"
    satz = f"Hallo {name}, ich bin dein erstes Python-Programm!"
    print(satz)

    stimme = pyttsx3.init()
    stimme.say(satz)
    stimme.runAndWait()


def hallo_welt_vergleich():
    beispiele = {
        "Python": 'print("Hallo Welt")',
        "JavaScript": 'console.log("Hallo Welt");',
        "Java": (
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            '        System.out.println("Hallo Welt");\n'
            "    }\n"
            "}"
        ),
        "C": (
            "#include <stdio.h>\n\n"
            "int main() {\n"
            '    printf("Hallo Welt\\n");\n'
            "    return 0;\n"
            "}"
        ),
    }

    for sprache, code in beispiele.items():
        print(f"\n--- {sprache} ---")
        print(code)
    print("\nWelche Sprache sieht am einfachsten aus? ;)")


def browser_trick():
    import webbrowser

    print("JavaScript-Trick im Browser:")
    print("1. Eine beliebige Website öffnen")
    print("2. F12 drücken und den Tab 'Konsole' wählen")
    print("3. Einen dieser Befehle eintippen und Enter drücken:\n")
    print("   document.body.contentEditable = true")
    print("   -> Jetzt kannst du den Text der Seite direkt bearbeiten.\n")
    print('   document.body.style.transform = "rotate(180deg)"')
    print("   -> Die Seite steht auf dem Kopf.\n")
    print("Nach dem Neuladen (F5) ist alles wieder normal.")

    if input("\nBeispielseite jetzt öffnen? (j/n): ").strip().lower() == "j":
        webbrowser.open("https://de.wikipedia.org/wiki/Python_(Programmiersprache)")


DEMOS = {
    "1": ("Bunte Turtle-Spirale", turtle_spirale),
    "2": ("QR-Code erstellen", qr_code),
    "3": ("Python spricht", sprechen),
    "4": ("Hallo Welt in 4 Sprachen", hallo_welt_vergleich),
    "5": ("JavaScript-Trick im Browser", browser_trick),
}


def main():
    while True:
        print("\n========== Python-Demos ==========")
        for nummer, (titel, _) in DEMOS.items():
            print(f"  {nummer}) {titel}")
        print("  0) Beenden")

        wahl = input("\nDeine Wahl: ").strip()

        if wahl == "0":
            print("Tschüss!")
            break
        elif wahl in DEMOS:
            titel, funktion = DEMOS[wahl]
            print(f"\n>>> {titel}\n")
            funktion()
        else:
            print("Ungültige Eingabe, bitte eine Zahl aus dem Menü wählen.")


if __name__ == "__main__":
    main()