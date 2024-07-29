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
