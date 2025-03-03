# Задание №1

# Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
# Условия:

#     Программа должна быть нечувствительна к регистру.
#     Игнорировать пробелы и знаки пунктуации.
# Пример использования:
#     isPalindrom("level") # True
#     isPalindrom("hello") # False

# Задание №2

# Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
# Условия:

#     Слова передаются в виде списка через ввод пользователя.
#     Программа должна вывести все палиндромы из списка.

# Пример использования:
#     isPalindromList(["hello", "list", "level"]) # ["level"]

# Задание №3

# Задание: Написать программу, которая ищет все палиндромы в строке текста.
# Условия:

#     Программа должна игнорировать регистр и знаки пунктуации.
#     Если палиндромы повторяются, выводить их только один раз.

# Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]

#№1
def polidrom(text):
    text_opt = text.lower().replace(" ", "").replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace("&", "").replace("-", "").replace("_", "")
    if text_opt == text_opt[::-1]:
        print ("Слово полидром")
    else:
        print("Слово не полидром")

# print(polidrom())

#№2
def isPalindromList(text):
    for word in text:
       print(word), polidrom(word)

# my_list = ["hello", "list", "level"]
# print(isPalindromList(my_list))

# #№3
def isPalindromString(string):
    string = string.split()
    for words in string:
        print(words), polidrom(words)

text = input("Введите текст: ")
print(isPalindromString(text))
