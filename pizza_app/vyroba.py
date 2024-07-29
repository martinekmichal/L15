from pizza import Pizza

class PizzaTovarna:
    @staticmethod
    def vytvorit_pizzu(recept):
        recepty = {
            "Salamova": Pizza("Salamova", 149),
            "Bananova": Pizza("Bananova", 199),
            "Mimozemska": Pizza("Mimozemska", 250),
            "Vegetarianska": Pizza("Vegetarianska", 220),
            "Chilli": Pizza("Chilli", 180)
        }
        return recepty.get(recept, None)