import rechnen

def hauptfunktion (h):
    print ("Mir übergeben wurde ", h)
    erg = rechnen.addieren (5,6)
    print ("Errechnet habe ich ", erg)

if __name__ == '__main__':
    print('Dies ist das Main-Module')

    ergebnis = rechnen.addieren(3,4)
    print ("3+4 = ", ergebnis)

    ergebnis = rechnen.multiplizieren(5,6)
    print ("5*6 = ", ergebnis)

    hauptfunktion("Aufrufen tut main.py")