from mapa import Mapa

def run() -> None:
    x = int(input('Wybierz szerokość mapy: '))
    y = int(input('Wybierz wysokość mapy: '))
    Moja_mapa = Mapa(x, y)
    Moja_mapa.pokaz_mape()


if __name__ == '__main__':
    while True:
        run()
        print('kolejna: ')
