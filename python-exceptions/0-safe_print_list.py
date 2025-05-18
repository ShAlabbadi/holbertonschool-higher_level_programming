#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.
    
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.
        
    Returns:
        int: The real number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
