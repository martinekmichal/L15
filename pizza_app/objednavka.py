class Objednavka:
    def __init__(self, pizza):
        self.pizza = pizza
    def zobrazit(self):
        print(self.pizza)
    def ulozit_do_souboru(self):
        with open("obj_pizza.ord", "a") as soubor:
            soubor.write(str(self.pizza) + "\n")
    def zaplatit(self, platebni_strategie):
        castka = self.pizza.ziskat_cenu()
        platebni_strategie.zaplatit(castka)