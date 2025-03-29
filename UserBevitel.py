# UserBevitel.py
"""
UserBevitel.py

Ez a modul tartalmazza a FelhasznaloiBevitel osztályt, amely a sztring számoló programunkban 
a felhasználói bemenetek bekéréséért felel.

A bekért számok sztringként kerülnek feldolgozásra, és érvényesítésre kerülnek 
a SztringSzamolo osztály segítségével.
"""

from Szamolo import SztringSzamolo

class FelhasznaloiBevitel:
    """A felhasználói input kezelésére szolgáló osztály."""

    @staticmethod
    def bekerSzamot(felirat: str) -> str:
        while True:
            szam = input(felirat)
            if SztringSzamolo.ervenyesEgeszSzam(szam):
                return szam
            else:
                print("Érvénytelen szám. Kérlek adj meg egy egész számot (pl. -10 vagy 23).")

    def bekerKetSzamot(self) -> tuple[str, str]:
        szam1 = self.bekerSzamot("Kérem az első számot: ")
        szam2 = self.bekerSzamot("Kérem a második számot: ")
        return szam1, szam2
