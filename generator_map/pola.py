kolory: dict = {
    'red': "\033[91m",
    'green': "\033[32m",
    'blue': "\033[34m",
    'yellow': "\033[93m",
    'grey': "\033[37m",
    'domyslny': "\033[0m"
}

class Pola:
    def __init__(self, symbol: str, kolor: str = kolory['domyslny'], k: bool = True):
        self.symbol = f"{kolor}{symbol}{kolory['domyslny']}" if k else symbol


pole = Pola('.', kolory['yellow'])
las = Pola("Y", kolory['green'])
gora = Pola('A', kolory['grey'])
woda = Pola('~', kolory['blue'])