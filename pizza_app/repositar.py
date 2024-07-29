import objednavka

class ObjednavkaRepozitar:
    def __init__(self):
        self.objednavky = []
        self.zisk = 0
        self.vraceni = 0
    def pridat_objednavku(self, objednavka):
        self.objednavky.append(objednavka)
        self.zisk += objednavka.pizza.ziskat_cenu()
    def vratit_objednavku(self, objednavka):
        self.objednavky.remove(objednavka)
        self.vraceni += 1
        self.zisk -= objednavka.pizza.ziskat_cenu()
    def ziskat_statistiku(self):
        return len(self.objednavky), self.vraceni, self.zisk