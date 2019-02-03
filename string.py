import sys

# Строки представляют собой коллекции с последовательным доступом из нуля или более букв, чисел и прочих знаков.
my_string = "string"

# Доступ осуществляется по порядковому номеру элемента.
my_string[0]

# Строки не изменяемы.
# my_string[0] = 1 - вызовет ошибку.

# Размер пустой строки составляет 49 байт.
empty_string = ''
size_of_empty_string = sys.getsizeof(empty_string)

# Строки используются для различных манипуляций с символами.
