import json
import urllib.parse
import urllib.request
from .osoba import Osoba


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
        req_rs = json.loads(f.read().decode('utf-8'))
        return req_rs

    def find_person(self, name,):

        url = 'https://api.e-science.pl/api/azon/persons/'
        values = {'search': name,
                  'api_key': self.token,
                  'limit': 1000,
                  'offset': 1}
        data = urllib.parse.urlencode(values, False, '', 'utf-8')
        url += '?' + data
        req = urllib.request.urlopen(url)
        req_rs = json.loads(req.read().decode('utf-8'))
        persons = {}
        for p in req_rs['results']:
            persons[p['id']] = Osoba(p['id'], p['first_name'], p['last_name'])
        return persons







