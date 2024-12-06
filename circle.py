#задаем функцию
def ploshad(a):
    return a * a * 3.14
def dlina(a):
    return a * 2 * 3.14 
r=float(input('Введите радиус:'))
resultat = ploshad(r)  #вызываем функцию
print('Площадь круга равна:',resultat) #результат площади круга 
resultat1 = dlina(r) #вызываем функцию
print('Длина окружности равна:', resultat1) #резултат длины окружности