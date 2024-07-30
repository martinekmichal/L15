# Úkol co jsem neodevzdal v čas. :)

class Restaurace:
    def __init__(self, nazev, specializace, adresa, webova_stranka, telefon):
        self.nazev = nazev
        self.specializace = specializace
        self.adresa = adresa
        self.webova_stranka = webova_stranka
        self.telefon = telefon
    def zobrazit_info(self):
        print(f"Restaurace: {self.nazev}")
        print(f"Specializace: {self.specializace}")
        print(f"Adresa: {self.adresa}")
        print(f"Webová stránka: {self.webova_stranka}")
        print(f"Telefon: {self.telefon}")
    def ulozit_do_souboru(self, soubor):
        with open(soubor, 'a') as f:
            f.write(f"Restaurace: {self.nazev}\n")
            f.write(f"Specializace: {self.specializace}\n")
            f.write(f"Adresa: {self.adresa}\n")
            f.write(f"Webová stránka: {self.webova_stranka}\n")
            f.write(f"Telefon: {self.telefon}\n")

restaurace = Restaurace(
    nazev="MM požranictví",
    specializace="Česká",
    adresa="Pod Mostem 15, Letohrad",
    webova_stranka="www.MMpozranictvi.cz",
    telefon="+420123456789"
)

restaurace.zobrazit_info()
restaurace.ulozit_do_souboru("L15_old_ukol_restaurace.info")