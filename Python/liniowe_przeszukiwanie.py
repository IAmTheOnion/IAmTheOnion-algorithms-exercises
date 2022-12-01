import random

def podzielna_przez_7(liczby):
    for i in range(0, len(liczby)):
        if liczby[i] % 7 == 0:
            print("Liczba na pozycji", i + 1, "jest podzielna przez 7")
            return True
    print("Żadna z liczb nie jest podzielna przez 7")
    return False

def wszystkie_wieksze_od_5(liczby):
    for i in range(0, len(liczby)):
        if liczby[i] < 5:
            print("Liczba na pozycji", i + 1, "nie jest większa od 5")
            return False
    print("Wszystkie liczby są podzielne przez 5")
    return True

def rozna_od_2_n_elementowa(ilosc_elementow):
    liczby = []
    for i in range(0, ilosc_elementow):
        liczby.append(random.randint(1, 100))
    print(liczby)
    for j in range(0, len(liczby)):
        if liczby[j] != 2:
            print("W tablicy znajduje się liczba inna od 2")
            return True
    print("Wszystkie liczby są podzielne przez 5")
    return False

def nie_podzielna_przez_4_mniejsze_niz_033():
    liczby = []
    for i in range(0, 11):
        liczby.append(random.randint(0, 32))
    print(liczby)
    for j in range(0, len(liczby)):
        if liczby[j] % 4 == 0:
            print("W tablicy na pozycji", j+1, "znajduje się liczba podzielna przez 4")
            return True
    print("Wszystkie liczby nie są podzielne przez 4")
    return False

def przeszukiwanie_z_wartownikiem(liczby):
    for j in range(0, len(liczby) - 1):
        if liczby[j] == liczby[-1]:
            print("W tablicy na pozycji", j+1, "znajduje się liczba równa", liczby[-1])
            return True
    print("W tablicy nie ma liczby równej", liczby[-1])
    return False


liczby = []

for i in range(0, 10):
    liczby.append(random.randint(1,100))

print(liczby)

podzielna_przez_7(liczby)
wszystkie_wieksze_od_5(liczby)
rozna_od_2_n_elementowa(20)
nie_podzielna_przez_4_mniejsze_niz_033()

liczby.append(6)

print(liczby)

przeszukiwanie_z_wartownikiem(liczby)
