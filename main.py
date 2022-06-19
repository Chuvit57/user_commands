# Task-1
print(" пользовательские команды ".upper().center(50, '='))
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

print()
print( " Меню команд ввода символов ".center(30, '#'))
print("----------------------------------------")
print("p - По номеру документа найти имя хозяина")
print("s - Выводит номер полки на которой находится документ")
print("l - Выведет список всех документов")
print("a - Добавит новый документ в каталог и в перечень полок")
print("----------------------------------------")




# list_menu = ['p', 's', 'l', 'a']
# letter_selection = input('Выберите нужную вам команду и введите букву : ')
# if list_menu.count(letter_selection) != 1:
#     print("Этой буквы нет в меню. Попробуйте снова!")
# else:
#   if letter_selection == 'p':
#     print("Ok")

def search_name():
  num_doc = input("Введите номер документа: ")
  for i in range(0, len(documents)):
    n = (num_doc in documents[i].values())
    if n == True:
      value_list = list(documents[i].values())
      print(f"Имя и Фамилия владельца: {value_list[2]}")
      break

  
  
    

search_name()

# for i in range(0, len(documents)):
#   print(i)
#   print(documents[i]['number'])
# print(len(documents))  

# print(documents[0].keys())
# print(documents[0].values())
# print(documents[0].values())
# print(type(documents[0].values()))
# value_list = list(documents[0].values())
# print(value_list[2])

# print(documents[0].items())



