# функции для работы с пользователем

def select_op():
    op=int(input('выбери что хочешь сделать: \n1-новая запись\n2-поиск\n3-удаление\n4-изменение\n'))
    return op

def get_info():
    fio = input('введи имя: ')
    tel = input('введи телефон: ')
    data = fio+ ';' + tel + "\n"
    return data

def print_info(*args):
    for res in args:
        if isinstance(res, list):
            count=1
            for string in res:
                print(f'{count}) {string}')
                count+=1
        if isinstance(res, str):
            print(res)
def search():
    search_info = input('введи строку для поиска: ')
    return search_info


def select_name():
    num=int(input('выбери строку: '))
    return num-1
