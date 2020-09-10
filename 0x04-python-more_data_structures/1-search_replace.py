#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search < 0 or search >= len(my_list):
        return (my_list)
    else:
        new_list = my_list.copy()
        new_list[search] = replace
        return (new_list)
