def szyfruj_cezar(text, klucz):

    """Funkcja szyfrująca tekst za pomocą szyfru Cezara dla polskich znaków."""
    szyfrogram = ""
    alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"
    szyfr_list = []



    for znak in text:
        pozycja = alfabet.index(znak.upper())
        print(alfabet.index(znak.upper()))
        nowa_pozycja = (pozycja + klucz) % len(alfabet)
        if znak.upper() in alfabet:
            if znak.isupper():
                szyfrogram += alfabet[nowa_pozycja]
            else:
                szyfrogram += alfabet[nowa_pozycja].lower()
        else:
            szyfrogram += znak
    shifted_alfabet = alfabet[klucz:] + alfabet[:klucz]
    splited_text = list(text)
    for i in range(len(splited_text)):
        splited_text[i] = splited_text[i].upper()
    print(splited_text)
    aha = ''
    for i in splited_text:
        for x in shifted_alfabet:
            if i == x:
                aha += '1'
            else:
                aha += '0'
    czesci = []
    for i in range(0, len(aha), 4):
        czesci.append(aha[i:i+4])

    czesci = [item for item in czesci if item != '0000' and item != '000']
    print(czesci)
    return szyfrogram




text = "Paweł"
klucz = 8

szyfrogram = szyfruj_cezar(text, klucz)
print(szyfrogram)
