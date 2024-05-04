class bron:
    def __init__(self, nazwa: str, typ: str, dmg: int, wartosc: int) -> None:
        self.nazwa = nazwa
        self.typ = typ
        self.dmg = dmg
        self.wartosc = wartosc


rece = bron(nazwa='nagie kule zniszczenia - gołe ręce', typ='obuchowy', dmg=3, wartosc=0)
miecz_1 = bron(nazwa='żelazny miecz', typ='tnący', dmg=10, wartosc=10)
miecz_2 = bron(nazwa='legendarny miecz zagłady goblinów', typ='święty', dmg=100, wartosc=1000)
