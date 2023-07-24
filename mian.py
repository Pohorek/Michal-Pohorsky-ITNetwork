import sqlite3
from Novy_pojisteny import novy_pojisteny
from zobraz_pojistence import pojistenci
from hledani import hledani

con = sqlite3.connect("pojistenci.db")
cursor = con.cursor()

print("-----------------------------")
print("Evidence pojištěných")
print("-----------------------------")
print()
print("Vyberte si akci:")
print("1 - Přidat nového pojištěného")
print("2 - Vypsat všechny pojištěné")
print("3 - Vyhledat pojištěného")
print("4 - Konec")
vlkad = int(input())

if vlkad == 1:
    novy_pojisteny.novy(novy_pojisteny)

if vlkad == 2:
    pojistenci.seznam_pojistencu(pojistenci)

if vlkad == 3:
    hledani.hledat(hledani)

if vlkad == 4:
    print("Pokračujte libovolnou klávesou...")
    input()

else:
    print("Zadali jste neplatnou volbu, pokračujte libovolnou klávesou...")
    input()
