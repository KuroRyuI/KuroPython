from pola import *
from random import randint

class Mapa:
    def __init__(self, szerokosc: int, wysokosc: int):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

        self.mapa_info: list[list[Pola]]

        self.generator_mapy()
        #domyslnie przeniesc do main jako wybor uzytkownika
        self.generator_pol(gora, round(wysokosc/5), 1, int(self.szerokosc), int(self.wysokosc/2), True)
        self.generator_pol(woda, round(wysokosc/5), 1, int(self.szerokosc), int(self.wysokosc/2), True)
        self.generator_pol(las, round(wysokosc/5), 1, int(self.szerokosc), int(self.wysokosc/2), True)

    def generator_mapy(self) -> None:
        self.mapa_info = [[pole for _ in range(self.szerokosc)] for _ in range(self.wysokosc)]

    def generator_pol(self,
                      pola: Pola,
                      ilosc_terenow: int,
                      min_rozmiar: int,
                      max_rozmiar_x: int,
                      max_rozmiar_y: int,
                      nieregularnosc: bool=True) -> None:
        for _ in range(ilosc_terenow):
            szerokosc = randint(min_rozmiar, max_rozmiar_x)
            wysokosc = randint(min_rozmiar, max_rozmiar_y)
            start_x = randint(0, self.szerokosc-szerokosc)
            start_y = randint(0, self.wysokosc-wysokosc)
            n_start_x = start_x

            for i in range(wysokosc):
                if nieregularnosc:
                    szerokosc = randint(int(0.5*szerokosc), szerokosc)

                if n_start_x+2 < self.szerokosc-szerokosc and n_start_x-2 > 0:
                    n_start_x = n_start_x + randint(-2, 2)
                elif n_start_x-2 <= 0 and n_start_x+2 < self.szerokosc-szerokosc:
                    n_start_x = n_start_x + randint(0, 2)
                else:
                    n_start_x = n_start_x + randint(-2, 0)
                for j in range(szerokosc):
                    self.mapa_info[i+start_y][j+n_start_x] = pola

    def pokaz_mape(self) -> None:
        x = '# ' + self.szerokosc * '# ' + '#'
        print(x)
        for rzad in self.mapa_info:
            rzad_pol = [pola.symbol for pola in rzad]
            print('# '+" ".join(rzad_pol)+' #')
        print(x)
