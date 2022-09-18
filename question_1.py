L = [1, 2, 3, 5, 6, 7, 8, 9, 10]

def foo(int_list):
    count = 0
    list_length = len(int_list)
    lowest_integer = -1
    while count <= list_length:
        count = count + 1
        if count in int_list:
            pass
        else:
            lowest_integer = count
            break
    print(lowest_integer)
    
foo(L)