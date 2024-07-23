def docstring_cls(fn):
    '''Here we have a closure function which basically
    checks if a function has docstring of more than 50 characters
    or not. Here we have defined a non local variable docstr_len=50
    and comparing doctsring length of passed function fn 
    and returning True or False'''
    docstr_len = 50

    def docstring_check():
        '''checking if docstring is more than 50 words or not'''
        if fn.__doc__ and len(fn.__doc__) > docstr_len:
            return True
        else:
            return False
    return docstring_check


def myfibonacci():
    '''This is a closure function which generates 
    next number in fibonacci series. We have 
    initialized first and second as 0 and 1 which 
    are non local variables and 
    keep adding the last two to get the third'''
    first = 0
    second = 1

    def generate_my_next_number() -> int:
        """
        This function sums the previous two numbers and returns the generated sum, it also updates the previous
        two numbers with the new value
        """
        nonlocal first, second
        temp = second
        second = first + second
        first = temp
        return second
    return generate_my_next_number


# Q3
# We wrote a closure that counts how many times a function was called.
# Write a new one that can keep track of how many times add/mul/div functions were called,
# and update a global dictionary variable with the counts
fn_cnt_dict = {}


def counter(fn):
    ''' This is a closure function which
    maitains a counter on how many times
    add/mul/div functions were called in a 
    global dictionary'''
    cnt_add, cnt_mul, cnt_div = 0, 0, 0

    def inner(*args, **kwargs):
        nonlocal cnt_add, cnt_mul, cnt_div
        global fn_cnt_dict
        if fn.__name__ == "add":
            cnt_add += 1
            fn_cnt_dict[fn.__name__] = cnt_add
            fn(*args, **kwargs)
        elif fn.__name__ == "mul":
            cnt_mul += 1
            fn_cnt_dict[fn.__name__] = cnt_mul
            fn(*args, **kwargs)
        elif fn.__name__ == "div":
            cnt_div += 1
            fn_cnt_dict[fn.__name__] = cnt_div
            fn(*args, **kwargs)
        else:
            "Invalid fn"

        return fn_cnt_dict

    return inner


def add(a, b):
    '''returns addition of two numbers'''
    return a+b


def mul(a, b):
    '''returns multiplication of two numbers'''
    return a*b


def div(a, b):
    '''returns division of two numbers'''
    if b != 0:
        return a/b
    else:
        raise ZeroDivisionError("division by 0")


def counter_dict(fn, d):
    '''This closure function is similar to previous function
    and maintains counter of add/mul/div function but in
    the dictionary which is passed as paramter to closure function'''
    cnt_add, cnt_mul, cnt_div = 0, 0, 0

    def inner(*args, **kwargs):
        if isinstance(d, dict) == False:
            raise ValueError(" paramter passed not dict")
        nonlocal cnt_add, cnt_mul, cnt_div

        if fn.__name__ == "add":
            cnt_add += 1
            d[fn.__name__] = cnt_add
            fn(*args, **kwargs)
        elif fn.__name__ == "mul":
            cnt_mul += 1
            d[fn.__name__] = cnt_mul
            fn(*args, **kwargs)
        elif fn.__name__ == "div":
            cnt_div += 1
            d[fn.__name__] = cnt_div
            fn(*args, **kwargs)
        else:
            raise ValueError("Invalid fn")

        return d

    return inner
