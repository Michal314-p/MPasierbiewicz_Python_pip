class Osoba:
    def __init__(self, id_osoby, imie, nazwisko):
        self.id_osoby = id_osoby
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return str(self.id_osoby) + ', ' + str(self.imie) + ', ' \
               + str(self.nazwisko)
