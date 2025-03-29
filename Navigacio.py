# Navigacio.py
"""
Navigacio.py

Ez a modul tartalmazza a Navigacio osztályt, amely a sztring számoló programunk 
menürendszerét és fő vezérlését biztosítja.

Felhasználói választás alapján meghívja a számolási műveleteket és kezeli a 
bemeneteket és kimeneteket.
"""
from UserBevitel import FelhasznaloiBevitel
from Szamolo import SztringSzamolo

class Navigacio:
    """A program menüjét és futtatását vezérlő osztály."""

    def __init__(self):
        self.bevitel = FelhasznaloiBevitel()
        self.szamolo = SztringSzamolo()

    def menuKiirasa(self):
        print("\n--- Program menü, kérlek válassz ---")
        print("1. Összeadás")
        print("2. Kivonás")
        print("3. Összehasonlítás")
        print("4. Szorzás")
        print("5. Kilépés")

    def futtat(self):
        while True:
            self.menuKiirasa()
            valasztas = input("Válassz egy műveletet (1-5): ")

            if valasztas in ["1", "2", "3", "4"]:
                szam1, szam2 = self.bevitel.bekerKetSzamot()

                if valasztas == "1":
                    print("Eredmény:", self.szamolo.szamHozzaadas(szam1, szam2))
                elif valasztas == "2":
                    print("Eredmény:", self.szamolo.szamKivonas(szam1, szam2))
                elif valasztas == "3":
                    print("Eredmény:", self.szamolo.szamOsszehasonlitas(szam1, szam2))
                elif valasztas == "4":
                    print("Eredmény:", self.szamolo.szamSzorzas(szam1, szam2))
            elif valasztas == "5":
                print("Kilépés... Viszlát!")
                break
            else:
                print("Érvénytelen választás. Kérlek próbáld újra.")
