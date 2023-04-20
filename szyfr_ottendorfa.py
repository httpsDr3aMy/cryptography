import string

# funkcja do kodowania tekstu za pomocą Szyfru Ottendorfa
def ottendorf_kodowanie(tekst, klucz):
    # usuwanie wszystkich spacji i innych znaków niebędących literami
    tekst = ''.join(litera for litera in tekst if litera.isalpha())

    # usuwanie liter "j" z klucza i zamiana go na "i"
    klucz = klucz.replace('j', '').lower() + string.ascii_lowercase.replace('j', '')

    zaszyfrowany_tekst = ""
    for slowo in [tekst[i:i+5] for i in range(0, len(tekst), 5)]:
        # zamiana każdej litery na odpowiadającą jej liczbę z zakresu 0-24
        slowo_liczby = [klucz.index(litera.lower()) for litera in slowo]

        # połączenie liczb w jedną ciągłą liczbę i dodanie do zaszyfrowanego tekstu
        zaszyfrowany_tekst += " ".join(str(liczba) for liczba in slowo_liczby) + " "
    return zaszyfrowany_tekst.strip()

# funkcja do dekodowania tekstu za pomocą Szyfru Ottendorfa
def ottendorf_dekodowanie(klucz, tekst):
    # usuwanie liter "j" z klucza i zamiana go na "i"
    klucz = klucz.replace('j', '').lower() + string.ascii_lowercase.replace('j', '')

    odszyfrowany_tekst = ""
    for slowo in tekst.split():
        # konwersja każdej liczby z zakresu 0-24 na odpowiadającą jej literę z klucza
        slowo_litery = [klucz[int(liczba)] for liczba in slowo.split()]

        # połączenie liter w jedno słowo i dodanie do odszyfrowanego tekstu
        odszyfrowany_tekst += ''.join(slowo_litery)
    return odszyfrowany_tekst

print('1. Koder\n'
      '2. Dekoder')
odpowiedz = int(input('Wybierz opcję: '))
if odpowiedz == 1:
    tekst_uzytkownika = str(input('Podaj tekst: '))
    klucz_uzytkownika = str(input('Podaj klucz: '))
    print('Zakodowana treść brzmi: '+'"' + str(ottendorf_kodowanie(tekst_uzytkownika, klucz_uzytkownika)) + '"' + '.')
elif odpowiedz == 2:
    tekst_uzytkownika = str(input('Podaj tekst: '))
    klucz_uzytkownika = str(input('Podaj klucz: '))
    print('Zdekodowana odpowiedź brzmi: '+'"' + str(ottendorf_dekodowanie(tekst_uzytkownika, klucz_uzytkownika)) + '"' + '.')
else:
    print('Zła odpowiedź.')
