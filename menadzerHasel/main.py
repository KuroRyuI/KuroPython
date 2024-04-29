from cryptography.fernet import Fernet

"""
def stworz_klucz():
    klucz = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(klucz)"""

def load_key():
    file = open('key.key', 'rb')
    klucz = file.read()
    file.close()
    return klucz

def dodaj():
    name = input('Użytkownik: ')
    pasw = input('Hasło: ')

    with open('hasla.txt', 'a') as f:
        f.write(name + " | " + fer.encrypt(pasw.encode()).decode() + "\n")

def zobacz():
    with open('hasla.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            nazwa, haslo = data.split('|')
            print('Uzytkownik: ', nazwa, ' Hasło: ', fer.decrypt(haslo.encode()).decode())
def zmien_haslo():
    pas = input('Podaj nowe hasło główne: ')
    with open('masterkey.txt', 'w') as f:
        f.write(fer.encrypt(pas.encode()).decode() + "\n")



pas = input('Podaj hasło główne: ')
key = load_key() + pas.encode()
fer = Fernet(key)
with open('masterkey.txt', 'r') as f:
    x = f.read()
    x = fer.decrypt(x.encode()).decode()
    if pas == x:
        while True:
            mod = int(input('zmień hasło główne (1) \n dodaj nowe hasło (2) \n zobacz wpisane (3) \n  wyjdź (4)'))

            if mod == 4:
                break
            elif mod == 2:
                dodaj()

            elif mod == 3:
                zobacz()
            elif mod == 1:
                zmien_haslo()
            else:
                print('spróbuj ponownie')
                continue
    else:
        print("podałeś złe hasło!")
        exit()
