#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            tmp_res = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            tmp_res = 0
            print("division by 0")
        except TypeError:
            tmp_res = 0
            print("wrong type")
        except IndexError:
            tmp_res = 0
            print("out of range")
        finally:
            pass
        new_list.append(tmp_res)
    return new_list
