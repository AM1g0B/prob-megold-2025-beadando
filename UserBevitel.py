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
        """Egyetlen érvényes egész szám bekérése a felhasználótól."""
        while True:
            szam = input(felirat).strip()
            if SztringSzamolo.ervenyesEgeszSzam(szam):
                return szam
            print("Érvénytelen szám. Kérlek adj meg egy egész számot (pl. -10 vagy 23).")

    @staticmethod
    def bekerKetSzamot() -> tuple[str, str]:
        """Két érvényes egész szám bekérése a felhasználótól."""
        szam1 = FelhasznaloiBevitel.bekerSzamot("Kérem az első számot: ")
        szam2 = FelhasznaloiBevitel.bekerSzamot("Kérem a második számot: ")
        return szam1, szam2
