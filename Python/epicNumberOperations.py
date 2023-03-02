def czy_jest_pierwsza(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def rozklad_na_czynniki_pierwsze(n):
    czynniki = []
    i = 2
    while n > 1:
        if n % i == 0 and czy_jest_pierwsza(i):
            czynniki.append(i)
            n = n / i
            i = 2
        else:
            i += 1
    print(czynniki)


def czy_bliznacze(n1, n2):
    if czy_jest_pierwsza(n1) and czy_jest_pierwsza(n2):
        if n1 - n2 == 2 or n2 - n1 == 2:
            return True
        else:
            return False
    else:
        return False


def bliznacze(n):
    pierwsze = []
    for i in range(2, n):
        if czy_jest_pierwsza(i):
            pierwsze.append(i)
    for i in range(1,len(pierwsze)):
        if pierwsze[i] - pierwsze[i-1] == 2:
            print(pierwsze[i], " ", pierwsze[i-1])

def czy_doskonala(n):
    dzielniki = []
    for i in range (1, n):
        if n % i == 0:
            dzielniki.append(i)
    sum = 0
    for i in range(0, len(dzielniki)):
        sum = sum + dzielniki[i];
    print(dzielniki)
    if n == sum:
        return True
    else:
        return False


