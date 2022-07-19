import random

count_decimals = [1] * 10
numbers = [i * 10 + random.randint(0, 9) for i in range(0, 9)]
if numbers.count(0) == 1:
    numbers[numbers.index(0)] = random.randint(1, 9)
while len(numbers) < 15:
    num = random.randint(1, 89)
    if num not in numbers:
        count_decimals[num // 10] += 1
    if (num not in numbers) and (count_decimals[num // 10] in (1, 2)):
        numbers.append(num)


numbers = sorted(numbers)
print(numbers)

temp = numbers.copy()
for row in range(0, 3):
    line = temp[::3 - row]
    for i in line:
        temp.remove(i)
    str1 = ''
    for col in range(0, 10):
        for i in line:
            if i // 10 == col:
                str1 += str(i)
            else:
                str1 += ' '
    print(str1)
