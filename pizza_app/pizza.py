class Pizza:
    def __init__(self, nazev, zakladni_cena):
        self.nazev = nazev
        self.zakladni_cena = zakladni_cena
        self.prisady = []

    def pridat_prisadu(self, prisada):
        self.prisady.append(prisada)

    def ziskat_cenu(self):
        return self.zakladni_cena + sum(prisada.cena for prisada in self.prisady)

    def __str__(self):
        prisady_str = ", ".join(prisada.nazev for prisada in self.prisady)
        return f"Pizza: {self.nazev}, Přísady: [{prisady_str}], Cena: {self.ziskat_cenu()}"