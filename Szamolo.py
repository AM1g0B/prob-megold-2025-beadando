# Szamolo.py
"""
Szamolo.py

Ez a modul tartalmazza a SztringSzamolo osztályt, amely a sztring számoló programunk 
számítási műveleteit végzi el: összeadás, kivonás, szorzás, összehasonlítás.

A bemenetek és a visszatérési értékek sztringként megadott egész számokat reprezentálnak.
A program negatív számokat is képes kezelni.
"""

class SztringSzamolo:
    """Számoló osztály, amely sztringként megadott egész számokkal végez műveleteket."""

    @staticmethod
    def ervenyesEgeszSzam(szam: str) -> bool:
        """Ellenőrzi, hogy egy sztring érvényes egész szám-e (negatív is lehet)."""
        return szam.lstrip('-').isdigit() and szam not in ('-', '')

    @staticmethod
    def _ellenoriz(szam1: str, szam2: str):
        """Belső segédfüggvény, amely ellenőrzi a két számot."""
        if not (SztringSzamolo.ervenyesEgeszSzam(szam1) and SztringSzamolo.ervenyesEgeszSzam(szam2)):
            raise ValueError("Hibás bemenet. Egész számokat adj meg sztringként.")

    @staticmethod
    def szamHozzaadas(szam1: str, szam2: str) -> str:
        SztringSzamolo._ellenoriz(szam1, szam2)
        return str(int(szam1) + int(szam2))

    @staticmethod
    def szamKivonas(szam1: str, szam2: str) -> str:
        SztringSzamolo._ellenoriz(szam1, szam2)
        return str(int(szam1) - int(szam2))

    @staticmethod
    def szamSzorzas(szam1: str, szam2: str) -> str:
        SztringSzamolo._ellenoriz(szam1, szam2)
        return str(int(szam1) * int(szam2))

    @staticmethod
    def szamOsszehasonlitas(szam1: str, szam2: str) -> int:
        SztringSzamolo._ellenoriz(szam1, szam2)
        int1 = int(szam1)
        int2 = int(szam2)
        if int1 < int2:
            return -1
        elif int1 > int2:
            return 1
        return 0
