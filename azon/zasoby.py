class Zasoby:

    def __init__(self, id_zasob, tytul, autorzy, sciezka, typ):

        self.id_zasob = id_zasob
        self.tytul = tytul
        self.autorzy = autorzy
        self.typ = typ
        self.sciezka = sciezka

    def __str__(self):
        return str(self.id_zasob) + ', ' + str(self.tytul) + ', ' + \
               str(self.autorzy) + ', ' + str(self.typ) + ', ' + \
               str(self.sciezka)
