#задаем функцию
def proverka(a):
    
    n = 0

    for i in range(2, int( a// 2 + 1)):
        if (a % i == 0):
                    n = n+1
    if (n <= 0):
        print('Число простое')
    else:
        print('Число не простое')

b=float(input('введите число: ')) #ввод числа
proverka(b) #вызываем функцию 