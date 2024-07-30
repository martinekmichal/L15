import os
from vyroba import PizzaTovarna
from prisady import Prisada
from objednavka import Objednavka
from platba import HotovostniPlatba, PlatbaKartou
from repositar import ObjednavkaRepozitar
from pizza import Pizza




prisady = [
    Prisada("Cibule", 30),
    Prisada("Jalapeños", 45),
    Prisada("Chilli", 30),
    Prisada("Okurky", 25),
    Prisada("Sýr", 30),
    Prisada("Prosciutto", 30)
]

pizza_tovarna = PizzaTovarna()
objednavka_repo = ObjednavkaRepozitar()

def vytvorit_objednavku():
    print("1. Pizza z menu")
    print("2. Vlastní pizza")
    volba = input("Vyberte možnost: ")

    if volba == "1":
        recept = input("Zadejte název pizzy z menu (Salamova, Bananova, Mimozemska, Vegetarianska, Chilli): ")
        pizza = pizza_tovarna.vytvorit_pizzu(recept)
        if pizza is None:
            print("Recept nenalezen!")
            return None
    elif volba == "2":
        nazev = input("Zadejte název vlastní pizzy: ")
        zakladni_cena = float(input("Zadejte základní cenu: "))
        pizza = Pizza(nazev, zakladni_cena)
    else:
        print("Neplatná volba")
        return None

    while True:
        print("Dostupné přísady:")
        for i, prisada in enumerate(prisady):
            print(f"{i + 1}. {prisada.nazev} - {prisada.cena}")
        volba_prisady = input("Vyberte přísadu (nebo 'k' pro dokončení): ")
        if volba_prisady == "k":
            break
        try:
            index = int(volba_prisady) - 1
            if 0 <= index < len(prisady):
                pizza.pridat_prisadu(prisady[index])
            else:
                print("Neplatný výběr")
        except:
            print("Neplatný výběr")

    objednavka = Objednavka(pizza)
    objednavka.zobrazit()
    objednavka.ulozit_do_souboru()
    return objednavka


def zaplatit_objednavku(objednavka):
    if objednavka is None:
        print("Neexistuje žádná objednávka!")
        return

    print("1. Hotovost")
    print("2. Karta")
    volba = input("Vyberte platební metodu: ")

    if volba == "1":
        platebni_strategie = HotovostniPlatba()
    elif volba == "2":
        platebni_strategie = PlatbaKartou()
    else:
        print("Neplatná volba")
        return

    objednavka.zaplatit(platebni_strategie)
    objednavka_repo.pridat_objednavku(objednavka)

def admin_menu():
    heslo = input("Zadejte administrátorské heslo: ")
    if heslo != "admin":
        print("Neplatné heslo")
        return

    statistika = objednavka_repo.ziskat_statistiku()
    print(f"Počet objednávek: {statistika[0]}")
    print(f"Počet vrácení: {statistika[1]}")
    print(f"Celkový zisk: {statistika[2]}")


def main():
    while True:
        print("Hlavní menu")
        print("1. Vytvoření objednávky")
        print("2. Zaplatit objednávku")
        print("3. Admin menu")
        print("4. Konec")
        volba = input("Vyberte možnost: ")

        if volba == "1":
            global objednavka
            objednavka = vytvorit_objednavku()
        elif volba == "2":
            zaplatit_objednavku(objednavka)
        elif volba == "3":
            admin_menu()
        elif volba == "4":
            break
        else:
            print("Neplatná volba")

if __name__ == "__main__":
    objednavka = None
    main()


