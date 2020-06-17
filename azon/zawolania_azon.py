import json
import urllib.parse
import urllib.request
from .osoba import Osoba
from .zasoby import Zasoby


class Zawolania_azon:

    def __init__(self, token):
        self.token = token

    def informacje_przez_id(self, id_osoby):
        url = 'https://api.e-science.pl/api/azon/author/' + \
              urllib.parse.quote(str(id_osoby)) + '/'
        wartosci = {'api_key': self.token}
        dane = urllib.parse.urlencode(wartosci, False, '', 'utf-8')
        url += '?' + dane
        f = urllib.request.urlopen(url)
        wynik = json.loads(f.read().decode('utf-8'))
        return wynik

    def znajdz_osobe(self, imie_nazwisko):

        url = 'https://api.e-science.pl/api/azon/persons/'
        wartosci = {'search': imie_nazwisko,'api_key': self.token,'limit': 1000,'offset': 1}
        dane = urllib.parse.urlencode(wartosci, False, '', 'utf-8')
        url += '?' + dane
        req = urllib.request.urlopen(url)
        zapytanie = json.loads(req.read().decode('utf-8'))
        osoby = {}
        for p in zapytanie['results']:
            osoby[p['id']] = Osoba(p['id'], p['first_name'], p['last_name'])
        return osoby

    def znajdz_zasoby(self, id_osoby):

        url = 'https://api.e-science.pl/api/azon/authors/entries/' + \
              id_osoby.__str__() + '/'
        wartosci = {'api_key': self.token,'limit': 1000,'offset': 1}
        dane = urllib.parse.urlencode(wartosci, False, '', 'utf-8')
        url += '?' + dane
        f = urllib.request.urlopen(url)
        zapytanie = json.loads(f.read().decode('utf-8'))
        zasoby = {}
        for r in zapytanie['results']:
            zasoby[r['pk']] = Zasoby(r['pk'], r['title'],[a['pk'] for a in r['authors']],'', r['entry_type_id'])
        return zasoby






