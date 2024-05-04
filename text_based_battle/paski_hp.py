import os

os.system("")

class Pasek_Hp:
    symbol_pozostalo: str = "█" # alt+219
    symbol_brak: str = '_'
    krawedz: str = '|'

    kolory: dict = {
        'red': "\033[91m",
        'green': "\033[95m",
        'blue': "\033[34m",
        'yellow': "\033[93m",
        'grey': "\033[37m",
        'domyslny': "\033[0m"
    }

    def __init__(self,
                 jednostka,
                 dlugosc: int = 20,
                 k: bool = True,
                 kolor: str = "") -> None:
        self.jednostka = jednostka
        self.hp_max = jednostka.hp_max
        self.hp = jednostka.hp

        self.dlugosc = dlugosc
        self.k = k
        self.kolor = self.kolory.get(kolor) or self.kolory['domyslny']

    def update(self) -> None:
        self.hp = self.jednostka.hp

    def rysuj(self) -> None:
        pozostalo = round(self.hp / self.hp_max * self.dlugosc)
        brakujace = self.dlugosc - pozostalo

        print(f'{self.jednostka.imie} hp: {self.jednostka.hp}/{self.jednostka.hp_max}')
        print(f"{self.krawedz}"
        f"{self.kolor if self.k else ''}" 
        f"{pozostalo * self.symbol_pozostalo}"
        f"{brakujace * self.symbol_brak}"
        f"{self.kolory['domyslny'] if self.k else ''}"
        f"{self.krawedz}")