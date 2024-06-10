a = int (input ())
b = int (input ())

print('Простые ')
for i in range(a, b + 1):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0 and i !=1:
        print(i)

print('Не простые')
for i in range(a, b + 1):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count != 0:
        print(i)
