
def solve():
    my_string = 'hfuhfbfhpirherb¿?=fbre·$·"$"$"$f&$//·$·%((ligpi'
    if hidden_operation(my_string) and \
            hidden_operation(my_string) != my_string:
        print('and')
        print(hidden_operation(my_string))
    elif not hidden_operation(my_string):
        if hidden_operation(False):
            print('not')
        else:
            print('and')
            print(hidden_operation(my_string))
    elif hidden_operation(my_string) == my_string:
        print('or')
        print(hidden_operation(False))
