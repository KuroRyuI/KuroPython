import os

from Postac import przeciwnik, bohater
from bron import *


x = input('podaj swoje imię dzielny bohaterze: ')
bohater = bohater(imie=x, hp=100)
przeciwnik = przeciwnik(imie='Goblin', hp=100, bron=miecz_1)
print('Na twojej drodze pojawił się dziki goblin!')
input('continue...')
while True:
    os.system("cls")
    turn = int(input('Co robisz? \n1 - zaatakuj \n2 - zmien bron \n3 - uciekaj '))
    if turn == 1:
        bohater.att(przeciwnik)
    elif turn == 2:
        os.system("cls")
        bronie = int(input('wybierz broń: \n 1 - wyrzuć broń z ręki, walcz jak mężczyzna na ręce! \n 2 - mieczyk \n 3 - legendarna wykałaczka'))
        if bohater.bron == 'rece':
            print('nie masz broni!')
            continue
        elif bronie == 1:
            bohater.schowaj()
        elif bronie == 2:
            bohater.zaloz(miecz_1)
        elif bronie == 3:
            bohater.zaloz(miecz_2)
        elif bronie == 4:
            pass
        else:
            print('Spróbuj jeszcze raz')
    else:
        print("ty tchórzu! Przeciwnik wbił ci miecz w d. Umarłeś.")
        bohater.hp = 0
        bohater.Pasek_hp.update()
        bohater.Pasek_hp.rysuj()
        break

    przeciwnik.Pasek_hp.rysuj()

    if przeciwnik.hp <= 0:
        print('Wygrałeś z Goblinem! +10 exp')
        break

    przeciwnik.att(bohater)
    bohater.Pasek_hp.rysuj()

    if bohater.hp <= 0:
        print('You died.')
        break
    input('continue...')



