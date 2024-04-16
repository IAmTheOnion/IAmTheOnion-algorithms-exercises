def uniqueDigits(number):
    digits = set()

    for i in str(number):
        if i in digits:
            return False
        digits.add(i)
    print(number)
    return True

max_number = 428
count_unique = 0

for i in range(100, max_number):
    if uniqueDigits(i):
        count_unique += 1

print(count_unique)
