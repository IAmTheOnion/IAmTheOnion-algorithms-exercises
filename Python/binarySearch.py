def binarySearch(array, target):
    for i in range(0, len(array)):
        for j in range(1, len(array)):
                if array[j - 1] > array[j]:
                    array[j - 1], array[j] = array[j], array[j - 1]
    print(array)
    min = 0
    max = len(array)-1
    while max >= min:
        print("min", min, "max", max)
        guess = ((min + max) // 2)
        print(guess)
        if array[guess] == target:
            print("Szukana znajduje sie na pozycji", guess)
            return guess
        elif array[guess] < target:
            min = guess + 1
        else:
            max = guess - 1

array = [16,4,5,1,6,3,7]

binarySearch(array,3)
