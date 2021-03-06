import sys

# Кортеж – это неизменяемый и более быстрый аналог списка.

# Создание пустого кортежа.
empty_tuple = ()
empty_tuple = tuple()

# Создание кортежа с данными.
my_tuple = (1, 2, 3)
my_tuple = tuple((1, 2, 3))

# Доступ к элементам кортежа осуществляется по порядковому номеру.
first_item = my_tuple[0]

# Кортеж это неизменяемый тип данных.
# my_tuple[0] = 1 - вызовет ошибку.

# Кортежи гетерогенны.
my_tuple = (1, "Hello", 2, 3.0, True)

# Размер пустого кортежа в моей 64-разрядной Ubuntu составляет 48 байт. 
my_tuple = ()

# Кортеж применяется для хранения данных вместо списка (если не предполагается изменений).
# Он защищает хранимые данные от непреднамеренных изменений и может использоваться в качестве ключа в словарях.

other_tuple = (3, 2, 1)

my_dict = {
    
    my_tuple: "Hello",
    other_tuple: "Goodbye"

}

