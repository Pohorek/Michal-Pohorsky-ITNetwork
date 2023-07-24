import sqlite3

con = sqlite3.connect("pojistenci.db")
cursor = con.cursor()


class hledani:
    def hledat(self):
        print("Zadejte jméno pojištěného:")
        hledani_jmeno = input()
        print("Zadejte příjmení pojištěného:")
        hledani_prijmeni = input()

        hledani = con.execute("select * from uzivatele where jmeno = ? and prijmeni = ?",
                              (hledani_jmeno, hledani_prijmeni))
        for row in hledani:
            print("ID = ", row[0])
            print("Jméno = ", row[1])
            print("Příjmení = ", row[2])
            print("Telefon = ", row[3])
            print("Věk = ", row[4])
            print()

            print("Pokračujte libovolnou klávesou...")
            input()
