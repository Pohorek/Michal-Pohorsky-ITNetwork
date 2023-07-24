import sqlite3
con = sqlite3.connect("pojistenci.db")
cursor = con.cursor()


class pojistenci:

    def seznam_pojistencu(self):
        zobraz = con.execute("select id, jmeno, prijmeni, telefonni_cislo, vek from uzivatele")
        for row in zobraz:
            print("ID = ", row[0])
            print("Jméno = ", row[1])
            print("Příjmení = ", row[2])
            print("Telefon = ", row[3])
            print("Věk = ", row[4])
            print()

            print("Pokračujte libovolnou klávesou...")
            input()
