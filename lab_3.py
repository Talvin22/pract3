#вариант 9
intt = []
floatt = []
strr = ''
booll = True

for i in range(0, 4):
    intt.append(int(input('Целое трехзначное число #{}: '.format(i+1))))

    while len(str(intt[i])) != 3 :
        intt[i]=int(input('Введи целое ТРЁХЗНАЧНОЕ число #{}: '.format(i+1)))


for i in range(0, 2):
    floatt.append(float(input('Число с плавающей точкой #{}: '.format(i+1))))

    while len(str(floatt[i])) != 9 :
        floatt[i]=float(input('Введи целое ВОСЬМИЗНАЧНОЕ число #{}: '.format(i+1)))


strr = input('Напишите строку длинной в 2 символа: ')
while len(strr) != 2:
    strr = input('Длинна строки не равна 2, введите новую: ')


print('целые числа:')
for number in intt:
    print('Intt: %d ', {number})

print('действительные числа: ')
for number in floatt:
    print('плавающая точка : ' + str("%.2f"% (number))[-6:])

print('Отформатированная строчка:{}'.format(strr))
print('Отформатированное значение бул:')

print(booll)
