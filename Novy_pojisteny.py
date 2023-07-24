import sqlite3
con = sqlite3.connect("pojistenci.db")
cursor = con.cursor()


class novy_pojisteny:
    def novy(self):
        print("Zadejte jméno pojišteného:")
        jmeno = input()
        print("Zadejte příjmení pojišteného:")
        prijmeni = input()
        print("Zadejte telefonní číslo:")
        telefon = input()
        print("Zadejte věk:")
        vek = input()
        print()
        print("Data byla uložena pokračujte libovolnou klávesou...")

        con.execute("INSERT INTO uzivatele(jmeno,prijmeni,telefonni_cislo,vek)\
                    VALUES (?,?,?,?)", (jmeno, prijmeni, telefon, vek))
        con.commit()
        con.close()
        input()