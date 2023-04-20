def generate(key, tab):
    kontrolny = ""
    alfabet = "abcdefghiklmnopqrstuvwxyz"

    x = 0
    y = 0
    pozycja = 0

    for znak in key:  # Korzystajac z petli przechodzimy przez kolejne znaki w kluczu
        pozycja = kontrolny.find(znak)  # Sprawdzamy czy dodany znak  znajduje się już w tablicy
        if pozycja == -1:  # Jesli nie dodajemy do tablicy i stringa kontrolnego
            if y == 5:  # Jesli tekscie jawnym znajduja sie inne znaki oprocz liter
                print("BLAD PODCZAS SZYFROWANIA! - Za duza ilosc znakow w tablicy")
                return  # wielkosc tablicy zostanie przekroczona - program nie moze wykonac swojego dzialania
            kontrolny += znak
            tab[x][y] = znak
            x += 1
            if x == 5:
                x = 0
                y += 1
    for znak in alfabet:
        pozycja = kontrolny.find(znak)
        if pozycja == -1:
            if y == 5:
                print("BLAD PODCZAS SZYFROWANIA! - Za duza ilosc znakow w tablicy")
                return
            kontrolny += znak
            tab[x][y] = znak
            x += 1
            if x == 5:
                x = 0
                y += 1
    print("Tablica szyfrowania:")
    print(tab)