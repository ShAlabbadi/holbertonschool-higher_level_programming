#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = printed_idx = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end='')
                index += 1
                printed_idx += 1
            else:
                print()
                return (printed_idx)
        except Exception:
            index += 1
