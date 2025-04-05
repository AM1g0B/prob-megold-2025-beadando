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
        self.muveletek = {
            "1": ("Összeadás", self.szamolo.szamHozzaadas),
            "2": ("Kivonás", self.szamolo.szamKivonas),
            "3": ("Összehasonlítás", self.szamolo.szamOsszehasonlitas),
            "4": ("Szorzás", self.szamolo.szamSzorzas),
            "5": ("Kilépés", None),
        }

    def menuKiirasa(self):
        print("\n--- Program menü, kérlek válassz ---")
        for kulcs, (nev, _) in self.muveletek.items():
            print(f"{kulcs}. {nev}")

    def futtat(self):
        while True:
            self.menuKiirasa()
            valasztas = input("Válassz egy műveletet (1-5): ").strip()

            if valasztas in self.muveletek:
                muvelet_nev, muvelet_fv = self.muveletek[valasztas]

                if valasztas == "5":
                    print("Kilépés... Viszlát!")
                    break

                try:
                    szam1, szam2 = self.bevitel.bekerKetSzamot()
                    eredmeny = muvelet_fv(szam1, szam2)
                    print(f"Eredmény ({muvelet_nev}):", eredmeny)
                except Exception as e:
                    print("Hiba történt a művelet során:", e)
            else:
                print("Érvénytelen választás. Kérlek próbáld újra.")
