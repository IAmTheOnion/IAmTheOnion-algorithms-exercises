def binarySearch(array, target):
    porownania = 0
    for i in range(0, len(array)):
        for j in range(1, len(array)):
                if array[j - 1] > array[j]:
                    array[j - 1], array[j] = array[j], array[j - 1]
    print(array)
    min = 0
    max = len(array)-1
    while max >= min:
        porownania += 1
        guess = ((min + max) // 2)
        print("Sprawdzana liczba", guess)
        if array[guess] == target:
            print("Szukana znajduje sie na pozycji", guess, "ilosc porownan", porownania)
            return guess
        elif array[guess] < target:
            min = guess + 1
        else:
            max = guess - 1
    print("Liczba nie została odnaleziona")
    return False

array = [16,4,5,1,6,3,7,13,56,42,75,17,46,23,73,12]
array_posortowany = [3,5,8,9,12,18,21,43,52,71,183,967]

binarySearch(array,12)
