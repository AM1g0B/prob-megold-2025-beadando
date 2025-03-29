# main.py
""" 
main.py

A program belépési pontja. Itt indul a sztring számoló programunk.
Ez a fájl meghívja a Navigacio osztályt, amely megjeleníti a menüt 
és kezeli a felhasználó választásait.

Dokumentációs célból docstring formátumot használunk a fájl elején.
"""

from Navigacio import Navigacio

if __name__ == "__main__":
    print("\n--- Üdv a sztring számolós programunkban ---")
    program = Navigacio()
    program.futtat()

