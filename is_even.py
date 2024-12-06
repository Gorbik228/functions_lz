#задаем функцию
def proverka(a):
    if a % 2 == 0:
         print('четное:' , a)
    else:
        print('нечетное:', a)
b=int(input('введите число: ')) #вводим число
proverka(b) #вызываем функцию 