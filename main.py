from azon.zawolania_azon import Zawolania_azon


class Test:
    def __init__(self, token):
        self.token = token
        self.zawolania_az = Zawolania_azon(token)

        self.method_names = {
            0: 'wyjdz',
            1: 'znajdz_osobe',
            2: 'informacje_id',
            3: 'zasoby'
        }

    def wyjdz(self):
        exit(0)

    def informacje_id(self):
        print('Podaj id osoby:')
        id = int(input())
        osoba = self.zawolania_az.informacje_przez_id(id)
        print('Dane osoby:')
        print(osoba)

    def start(self):
        wybor = 1
        while wybor != 0:
            print('Menu:\n'
                  '0: Wyjscie\n'
                  '1: Wyszukaj osobe\n'
                  '2: Wyszukaj informacje o osobie przez id\n'
                  '3: Znajdz zasoby poprzez odpowiednie id osoby\n'
                  'Podaj numer funkcji: ')
            wybor = int(input())
            nazwa_metody = self.method_names[wybor]
            metoda = getattr(self, nazwa_metody, lambda: "Invalid type")
            metoda()

    def znajdz_osobe(self):
        print('Wpisz imie lub nazwisko:')
        nazwa = input()
        osoby = self.zawolania_az.znajdz_osobe(nazwa)
        print('Znalezione osoby:')
        for key in osoby:
            print(osoby[key].__str__())

    def zasoby(self):
        print('Podaj id osoby:')
        id = int(input())
        zasoby = self.zawolania_az \
            .znajdz_zasoby(id)
        print('Znalezione zasoby:')
        for key in zasoby:
            print(zasoby[key].__str__())


if __name__ == '__main__':
    app = Test("klucz_azon")
    app.start()
