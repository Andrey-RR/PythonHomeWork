# функция для работы с базой данных

def write_info(info):
    with open('text.txt', 'a', encoding = 'utf-8') as file:
        file.write(info)
    return 'имя добавлено'

def search_name(spec):
    with open('text.txt', 'r', encoding = 'utf-8') as file:
        data = file.readlines()
        name_accept = []
        count=1
        for i in range(len(data)):
            if spec in data[i]:
                name_accept.append(data[i])
        return data, name_accept, "поиск завершен"

def change_name(old_lst, delete_line, new_line=None):
    with open('text.txt', 'w', encoding='utf-8') as file:
        for line in old_lst:
            if line == delete_line:
                if new_line:
                    file.write(new_line)
                continue
            file.write(line)
    return 'запись удалена' if not new_line else 'запись изменена'
