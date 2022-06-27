# Task-1

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

# ----------- Menu Command --------------------
print(" пользовательские команды ".upper().center(50, '='))
print()
print( " Меню команд ввода символов ".center(30, '#'))
print("----------------------------------------")
print("p - По номеру документа найти имя хозяина")
print("s - Выводит номер полки на которой находится документ")
print("l - Выведет список всех документов")
print("a - Добавит новый документ в каталог и в перечень полок")
print("----------------------------------------")

def search_name():
  num_doc = input("Введите номер документа: ")
  for i in range(0, len(documents)):
    if num_doc in documents[i].values():
      value_list = list(documents[i].values())
      print(f"И.Ф владельца: {value_list[2]}")


def search_shelf():
  num_doc = input("Введите номер документа: ")
  for key, value in directories.items():
    if (num_doc in value) == True:
      print(f"Номер полки: {key}")
      
def list_all_documents():
  for i in range(0, len(documents)):
    print(f'{documents[i]["type"] } "{documents[i]["number"]}" "{documents[i]["name"]}"' )

def document_add():
  type_doc = input("Введите тип документа: ")
  num_doc = input("Введите номер документа: ")
  name_person = input("Введите свое имя и фамилию: ")
  new_dict = {f'"type": "{type_doc}", "number": "{num_doc}", "name": "{name_person}"'}
  documents.append(new_dict)
  print("Ваш документ успешно добавлен!!!")
  print("----------------------------------------")
  print(documents)
  num_shelf = int(input("Введите номер полки(от 1 до 3(включительно)): "))
  while num_shelf > 3:
      print("Вы ввели неправильный номер полки! Попробуйте еще раз")
      num_shelf = int(input("Введите номер полки(от 1 до 3(включительно)): "))
  directories[f'{str(num_shelf)}'].append(num_doc)
  
  for key, value in directories.items():
        print(key, '->', value)
  




def main():
  while True:
    list_menu = ['p', 's', 'l', 'a']
    letter_selection = input('Выберите нужную вам команду и введите букву : ')
    if list_menu.count(letter_selection) != 1:
        print("Этой буквы нет в меню. Попробуйте снова! ")
    else:
      if letter_selection == 'p':
        search_name()
      elif letter_selection == 's':
        search_shelf()
      elif letter_selection == 'l':
        print()
        print(" Список всех документов ".center(30, '^') )
        list_all_documents()
      elif letter_selection == 'a':
        print()
        print(" Добавить новый документ в каталог и в перечень полок ".center(30, '^') )
        print()
        document_add()
  


if __name__ == '__main__':
  main()