# связь между view и db

from view import *
from db import *

def main():
    while True:
        ans = select_op()
        if ans == 1:
            human_info = get_info()
            res_str = write_info(human_info)
            print_info(res_str)
        elif ans == 2:
            spec = search()
            full_lst , accept_lst, res_str = search_name(spec)
            print_info(accept_lst, res_str)
        elif ans == 3:
            spec = search()
            full_lst, accept_lst, res_str = search_name(spec)
            print_info(accept_lst, res_str)
            selected_num = select_name()
            res_str = change_name(full_lst, accept_lst[selected_num])
            print_info(res_str)
        elif ans == 4:
            spec = search()
            full_lst, accept_lst, res_str = search_name(spec)
            print_info(accept_lst, res_str)
            selected_num = select_name()
            new_line = get_info()
            res_str = change_name(full_lst, accept_lst[selected_num], new_line)
            print_info(res_str)

main()