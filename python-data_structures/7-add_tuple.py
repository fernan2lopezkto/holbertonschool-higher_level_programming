#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 1:
        zero_a = tuple_a[0]
        one_a = tuple_a[1]
    elif len(tuple_a) == 1:
        zero_a = tuple_a[0]
        one_a = 0
    else:
        zero_a = 0
        one_a = 0

    if len(tuple_b) > 1:
        zero_b = tuple_b[0]
        one_b = tuple_b[1]
    elif len(tuple_b) == 1:
        zero_b = tuple_b[0]
        one_b = 0
    else:
        zero_b = 0
        one_b = 0

    n_a = zero_a + zero_b
    n_b = one_a + one_b
    new_tuple = (n_a, n_b)

    return new_tuple
