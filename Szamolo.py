# Szamolo.py
"""
Szamolo.py

Ez a modul tartalmazza a SztringSzamolo osztályt, amely a sztring számoló programunk 
számítási műveleteit végzi el: összeadás, kivonás, szorzás, összehasonlítás.

A bemenetek és a visszatérési értékek sztringként megadott egész számokat reprezentálnak.
A program negatív számokat is képes kezelni.
"""

class SztringSzamolo:
#    """Számoló osztály, amely sztringként megadott egész számokkal végez műveleteket."""

    @staticmethod
    def ervenyesEgeszSzam(szam: str) -> bool:
        """Ellenőrzi, hogy egy sztring érvényes egész szám-e (és az negatív is lehet)."""
        if szam.startswith('-'):
            return szam[1:].isdigit()
        return szam.isdigit()

    @staticmethod
    def szamHozzaadas(szam1: str, szam2: str) -> str:
        if not (SztringSzamolo.ervenyesEgeszSzam(szam1) and SztringSzamolo.ervenyesEgeszSzam(szam2)):
            raise ValueError("Hibás bemenet. Egész számokat adj meg sztringként.")
        return str(int(szam1) + int(szam2))

    @staticmethod
    def szamKivonas(szam1: str, szam2: str) -> str:
        if not (SztringSzamolo.ervenyesEgeszSzam(szam1) and SztringSzamolo.ervenyesEgeszSzam(szam2)):
            raise ValueError("Hibás bemenet. Egész számokat adj meg sztringként.")
        return str(int(szam1) - int(szam2))

    @staticmethod
    def szamSzorzas(szam1: str, szam2: str) -> str:
        if not (SztringSzamolo.ervenyesEgeszSzam(szam1) and SztringSzamolo.ervenyesEgeszSzam(szam2)):
            raise ValueError("Hibás bemenet. Egész számokat adj meg sztringként.")
        return str(int(szam1) * int(szam2))

    @staticmethod
    def szamOsszehasonlitas(szam1: str, szam2: str) -> int:
        if not (SztringSzamolo.ervenyesEgeszSzam(szam1) and SztringSzamolo.ervenyesEgeszSzam(szam2)):
            raise ValueError("Hibás bemenet. Egész számokat adj meg sztringként.")
        int1 = int(szam1)
        int2 = int(szam2)
        if int1 < int2:
            return 1
        elif int1 > int2:
            return -1
        else:
            return 0
