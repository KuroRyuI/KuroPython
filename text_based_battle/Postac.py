from bron import *
from paski_hp import *

class postac:

    def __init__(self, imie: str, hp: int):
        self.imie = imie
        self.hp = hp
        self.hp_max = hp

        self.bron = rece

    def att(self, cel) -> None:
        cel.hp -= self.bron.dmg
        cel.hp = max(cel.hp, 0)
        cel.Pasek_hp.update()
        print(f"{self.imie} zadał {self.bron.dmg} obrażeń {cel.imie} uzywając {self.bron.nazwa}")

class bohater(postac):
    def __init__(self,
                 imie: str,
                 hp: int
                 ) -> None:
        super().__init__(imie=imie, hp=hp)

        self.domyslna_bron = self.bron
        self.Pasek_hp = Pasek_Hp(self, kolor="blue")

    def zaloz(self, bron) -> None:
        self.bron = bron
        print(f"{self.imie} założył a(n) {self.bron.nazwa}!")

    def schowaj(self) -> None:
        self.bron = self.domyslna_bron
        if self.bron == rece:
            print(f"{self.imie} jest uzbrojony tylko w swoje ręce, więc je opuścił :(")
        else:
            print(f"{self.imie} schował a(n) {self.bron.nazwa}")

class przeciwnik(postac):
    def __init__(self,
                 imie: str,
                 hp: int,
                 bron
                 ) -> None:
        super().__init__(imie=imie, hp=hp)
        self.bron = bron
        self.Pasek_hp = Pasek_Hp(self, kolor="red")