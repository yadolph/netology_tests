

def search_name_by_number(doc_cat, doc_num):
  doc_found = False
  for docs in doc_cat:
    if docs['number'] == doc_num:
      try:
        #print(docs['name'])
        doc_found = True
        return docs['name']
      except KeyError:
        print(f'У документа с номером {docs["number"]} нет имени')
        return
  if doc_found == False:
    print(f'Документ с номером "{doc_num}" не найден')

def list_all_docs(doc_cat):
  for docs in doc_cat:
    print(f'{docs["type"]} "{docs["number"]}"  "{docs["name"]}"')

def find_shelf(doc_num, dir_cat):
  for shelf in dir_cat:
    if doc_num in dir_cat[shelf]:
      #print(f'Ваш документ находится на полке № {shelf}')
      return shelf
  print(f'Документ с номером "{doc_num}" не найден')

def add_doc(doc_cat, dir_cat):
  doc_type = input('Введите тип нового документа: ')
  doc_num = input('Введите номер нового документа: ')
  doc_name = input('Введите имя владельца нового документа: ')
  doc_shelf = input('Введите номер полки для нового документа: ')
  for docs in doc_cat:
    if docs['number'] == doc_num:
      print(f'Документ с номером "{doc_num}" уже существует')
      return
  if doc_shelf in dir_cat:
    doc_cat.append({"type": doc_type, "number": doc_num, "name": doc_name})
    dir_cat[doc_shelf].append(doc_num)
  else:
    print('Такой полки не существует. Попробуйте еще раз.')

def delete_doc(doc_cat, doc_dir):
  doc_found = False
  doc_deleted = False
  doc_num = input('Введите номер документа, который хотите удалить: ')
  for docs in doc_cat:
    if docs['number'] == doc_num:
      doc_found = True
      user_approval = input(f'Ваш документ с номером "{doc_num}" будет удален. Эту операцию нельзя отменить. Вы уверены? (y/n)')
      if user_approval == 'y':
        doc_cat.remove(docs)
        doc_deleted = True
        print(f'Документ c номером "{doc_num}" успешно удален')
      else:
        print('Ваш документ не удален')
  if doc_deleted == True:
    for shelf in doc_dir:
      if doc_num in doc_dir[shelf]:
        doc_dir[shelf].remove(doc_num)
  if doc_found == False:
    print(f'Документ с номером "{doc_num}" не найден')

def move_doc(dir_cat):
  doc_num = input('Введите номер документа, который хотите перенести: ')
  doc_check = False
  for shelf in dir_cat:
    if doc_num in dir_cat[shelf]:
      doc_check = True
  if doc_check:
    current_shelf = find_shelf(doc_num, dir_cat)
    new_shelf = input('Введите номер полки, на которую хотите перенести документ: ')
    if current_shelf == new_shelf:
      print('Новый номер полки совпадает с текущим. Документ остался на своем месте')
    elif new_shelf in dir_cat:
      dir_cat[new_shelf].append(doc_num)
      dir_cat[current_shelf].remove(doc_num)
      print(f'Документ c номером "{doc_num}" успешно перенесен с полки № {current_shelf} на полку № {new_shelf}')
    else:
      print('Перенос не совершен. Проверьте номер полки')
  else:
    print('Документ с таким номером не найден')

def new_shelf(dir_cat):
  new_shelf_num = input('Введите номер новой полки: ')
  if new_shelf_num in dir_cat:
    print(f'Полка с номером {new_shelf_num} уже существует. Попробуйте вызвать команду заново')
  else:
    dir_cat[new_shelf_num] = []
    print(f'Полка с номером "{new_shelf_num}" успешно создана. Самое время поместить на нее документы!')

def names_list(doc_cat):
  for docs in documents:
    try:
      print(docs["name"])
    except KeyError:
      print(f'У документа с номером {docs["number"]} нет имени')
 
def hello_message():
  print('*****************************************************')
  print('**      Добро пожаловать в каталог документов      **')
  print('*****************************************************')
  print(' ')

def instructions():
  print('Введите одну из следующих команд:')
  print('p  - вывести имя человека по номеру его документа')
  print('l  - вывести список всех документов в каталоге')
  print('s  - определить номер полки по номеру документа')
  print('a  - добавить новый документ в каталог')
  print('d  - удалить документ из каталога')
  print('m  - перенести документ на другую полку')
  print('as - создать новую полку')
  print('n  - Вывести перечень всех имен всех владельцев документов')
  print('h  - заново вывести справку по командам')
  print('q  - выйти из программы')
  print('')


if __name__ == '__main__':

  documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "123445"}
  ]

  directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
  }

  hello_message()
  instructions()

  user_choice = input('Ваша команда: ')

  def command_selector(user_choice):
    if user_choice == 'p':
      doc_num = input('Поиск имени человека по номеру документа. Введите номер документа: ')
      search_name_by_number(documents, doc_num)
    elif user_choice == 'l':
      list_all_docs(documents)
    elif user_choice == 's':
      doc_num = input('Определить полку по номеру документа. Введите номер документа: ')
      find_shelf(doc_num, directories)
    elif user_choice == 'a':
      add_doc(documents, directories)
    elif user_choice == 'h':
      instructions()
    elif user_choice == 'd':
      delete_doc(documents, directories)
    elif user_choice == 'm':
      move_doc(directories)
    elif user_choice == 'as':
      new_shelf(directories)
    elif user_choice == 'n':
      names_list(documents)
    else:
      print('Возможно, вы что-то ввели не так. Перепроверьте введенные вами данные. Вызвать помощь можно командой "h"')

  while user_choice != 'q':
    command_selector(user_choice)
    print('')
    user_choice = input('Введите новую команду (h - помощь, q - выход): ')

  if user_choice == 'q':
    print('До свидания!')
