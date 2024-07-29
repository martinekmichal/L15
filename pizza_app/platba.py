class PlatebniStrategie:
    def zaplatit(self, castka):
        raise NotImplementedError
class HotovostniPlatba(PlatebniStrategie):
    def zaplatit(self, castka):
        print(f"Zaplaceno {castka} v hotovosti.")
class PlatbaKartou(PlatebniStrategie):
    def zaplatit(self, castka):
        print(f"Zaplaceno {castka} kartou.")