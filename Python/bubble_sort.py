import random


def bubble_sort(numbers, type):
    for i in range (0,len(numbers)):
        for j in range(1, len(numbers)):
            if type == 1:
                if numbers[j-1] > numbers[j]:
                    numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
            elif type == 0:
                if numbers[j-1] < numbers[j]:
                    numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
            else:
                print("Nieprawidlowy typ sortowania (0-1)")
    return numbers


list = []

for i in range (0, 10):
    list.append(random.randint(0, 100))

bubble_sort(list, 0)

for i in list:
    print(i)
