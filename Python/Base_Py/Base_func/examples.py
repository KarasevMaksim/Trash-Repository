# Функция bin() преобразует целое число в двоичную строку с префиксом 0b
print(bin(13)) # str: 0b1101

#==============================================================================
# Функция oct() преобразует целое число в восьмеричную строку с префиксом 0o
print(oct(44)) # str: 0o54

#==============================================================================
# Функция round() используется для округления чисел. Она принимает два аргумента:
# number — округляемое число
# ndigits — количество знаков после запятой
print(round(3.4)) # 3
print(round(3.7)) # 4
print(round(3.48, 1)) # 3.5
print(round(3.41, 1)) # 3.4
print(round(3.376, 2)) # 3.38
print(round(3.371, 2)) # 3.37
# округление выполняется до ближайшего четного (банковское округление)
print(round(3.5)) # 4
print(round(4.5)) # 4

#==============================================================================
# Функция pow() используется для возведения чисел в произвольную степень.
#Она может принимать три аргумента:
# base — возводимое число
# exp — число, являющееся степенью
# mod — необязательный аргумент, число, на которое требуется произвести деление с
# остатком
print(pow(3, 4)) # 81
print(pow(2, 5, 30)) # 2

#==============================================================================
# Функция int('1001', base=2) возвращет значение в десятичной сс
print(int('1001', base=2)) # 9

#==============================================================================
# Функция ord() возвращает число символа из таблицы Unicode
print(ord('a')) # 97
#Функция chr() возвращает символ которому соответствует число в таблице Unicode
print(chr(97)) # a

#==============================================================================
# Функция callable() принимает объект и возвращает True если данный объект
# является вызываемым, иначе False
def func():
    pass
print(callable(func)) # True
print(callable(list)) # True
print(callable(100)) # False

#==============================================================================
# Функция hasatte() проверяет есть ле в объекте данный метод (атрибут)
print(hasattr([1, 2, 3], 'sort')) # True
print(hasattr(13, 'to_str')) # False

#==============================================================================
# Функция eval() выполняет строку-выражение, переданную ей в качестве
# обязательного аргумента, и возвращает результат выполнения этой строки
print(eval("'Senko' + 'Sun'")) # str: SenkoSun
# Операторами, которые нельзя использовать в качестве выражений, являются,
# например, while, for, if, def, import, class, raise и т.д.

#==============================================================================
# Функция exec() , в отличие от eval() , принимает блок кода и выполняет его,
# возвращая значение None. Аргумент функции:
#               code — строка, представляющая собой корректный блок кода
code = '''a = 10 
b = 20 
print(a + b)''' 
exec(code) # Напечатет в консоле 30
