import os
import inspect
import re
import random
import S6_assignment as s6
import pytest

README_CONTENT_CHECK_FOR = [
    'generate_my_next_number',
    'min_count',
    'docstring',
    'fibonacci',
    'called',
    'closure',
    'global',
    'count',
    'dictioanry',
    'variable'
]


def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(s6, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_readme_contents():
    readme_words = [word for line in open(
        'README.md', 'r') for word in line.split()]
    assert len(
        readme_words) >= 550, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 25, 'You are not writing proper heading'


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


############### 4 test cases for docstring_cls closure function########################
def test_doc_strings_with_lt_50():
    '''
    Checks if function caches if a function has less than 50 character docstring
    '''
    def a():
        '''test docstring'''
        pass
    f1 = s6.docstring_cls(a)
    assert f1() == False, 'no docstring or less than 50 words check failed'


def test_doc_strings_with_gt_50():
    '''
    Checks if function caches if a function has greater than 50 character docstring
    '''

    f1 = s6.docstring_cls(s6.myfibonacci)
    assert f1() == True, 'More than 50 character docstring check failed'


def test_doc_strings_with_no_docstring():
    '''
    Checks if function caches if a function has no docstring
    '''
    def a():
        pass
    f1 = s6.docstring_cls(a)
    assert f1() == False, 'No docstring check failed'


def test_doc_strings_closure_or_not():
    '''
    Checks if its a closure function or not
    '''
    f1 = s6.docstring_cls(s6.myfibonacci)
    assert bool(f1.__closure__) == True, "Not a closure"

####################### 2 Test cases for fibonacci##########################


def test_myfibonacci():
    mylist = [1, 2, 3, 5, 8, 13]
    f1 = s6.myfibonacci()
    for i in mylist:
        assert i == f1(), 'You are not able to generate a fibonacci series'


def test_fibonacci_closure_or_not():
    '''
    Checks if its a closure function or not
    '''
    f1 = s6.myfibonacci()
    assert bool(f1.__closure__) == True, "Not a closure"

###################### 6 test cases for counter closure fn ###################


def test_counter():
    '''to check if counter is working properly or not'''
    f1 = s6.counter(s6.add)
    for i in range(1, 11):
        assert f1(random.randint(1, 100), random.randint(1, 100)
                  ) == i, " Incorrect function add count"


def test_div():
    '''to check if division is happening correctly or not'''
    for _ in range(10):
        number1 = random.randint(-100, 100)
        number2 = random.randint(1, 100)
        assert (s6.div(number1, number2) == number1 /
                number2), 'Incorrect division'
        number2 = random.randint(-100, -1)
        assert (s6.div(number1, number2) == number1 /
                number2), 'Incorrect division'


def test_div_for_error():
    '''to check for division by zero error in denominator'''
    number1 = random.randint(-100, 100)
    number2 = 0
    with pytest.raises(ZeroDivisionError, match=r".*division.*"):
        s6.div(number1, number2), "division by zero"


def test_add():
    '''to check addition happening correctly or not'''
    for _ in range(10):
        number1 = random.randint(-100, 100)
        number2 = random.randint(-100, 100)
        assert (s6.add(number1, number2) == number1 +
                number2), 'Incorrect addition'


def test_mul():
    ''''to check if multiplication happening correctly or not'''
    for _ in range(10):
        number1 = random.randint(-100, 100)
        number2 = random.randint(-100, 100)
        assert (s6.mul(number1, number2) == number1 *
                number2), 'incorrect multiplication'


def test_counter():
    ''' to check if counter in dict is correct or not'''
    mydict_val = {'add': 4, 'mul': 3, 'div': 2}
    fn = s6.add
    value = s6.counter(fn)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s6.mul
    value = s6.counter(fn)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s6.div
    value = s6.counter(fn)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))

    assert s6.fn_cnt_dict == mydict_val, 'just count how many times each funtion is called..'

##################### 6 test cases for counter function with dictionary as parameter########


def test_counter_dict():
    '''to check if counter in passed dictionary is being maintained or not'''
    mydict_val = {'add': 4, 'mul': 3, 'div': 2}
    mypersonaldict = {'add': 0, 'mul': 0, 'div': 0}
    fn = s6.add
    value = s6.counter_dict(fn, mypersonaldict)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s6.mul
    value = s6.counter_dict(fn, mypersonaldict)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))
    fn = s6.div
    value = s6.counter_dict(fn, mypersonaldict)
    value(random.randint(1, 100), random.randint(1, 100))
    value(random.randint(1, 100), random.randint(1, 100))

    assert mypersonaldict == mydict_val, 'just count how many times each funtion is called..'


def test_counter_closure():
    '''
    Checks if its a closure function or not
    '''
    d = {}
    f1 = s6.counter_dict(s6.add, d)
    assert bool(f1.__closure__) == True, "Not a closure"


def test_counter_for_random_fn():
    '''
    Check if its maitaining counter for any random func
    '''
    with pytest.raises(ValueError, match=r".*Invalid.*"):
        d = {}

        f1 = s6.counter_dict(s6.myfibonacci, d)
        f1()


def test_dict_returned_or_not():
    '''
    Check if dictionary type being returned or not
    '''
    d = {}
    f1 = s6.counter_dict(s6.add, d)
    a = f1(1, 2)
    # print(type(a), a)
    assert isinstance(a, dict) == True, "Non dict return type"


def test_keys_of_returned_dict():
    '''
    Check if dict contains only keys for function called or all funcs'''
    d = {}
    f1 = s6.counter_dict(s6.add, d)
    a = f1(1, 2)
    assert a.get('mul') == None, "function never called"


def test_args_for_fn():
    '''Check if function works without dict passed as parameter or not'''
    with pytest.raises(ValueError, match=r".*dict.*"):
        d = 10
        f1 = s6.counter_dict(s6.add, d)
        a = f1(1, 2)


def test_doc_string():
    '''Check if docstring exists or not'''
    assert bool(
        s6.counter_dict.__doc__) == True, "Docstring missing"


def test_check_docs():

    assert bool(s6.docstring_cls.__doc__) == True, "Docstring missing"
    assert bool(s6.myfibonacci.__doc__) == True, "Docstring missing"
    assert bool(s6.add.__doc__) == True, "Docstring missing"

    assert bool(s6.mul.__doc__) == True, "Docstring missing"
    assert bool(s6.div.__doc__) == True, "Docstring missing"

    assert bool(
        s6.counter.__doc__) == True, "Docstring missing"
    assert bool(
        s6.counter_dict.__doc__) == True, "Docstring missing"


def test_check_closure():
    f1 = s6.docstring_cls(s6.myfibonacci)
    assert bool(
        f1.__closure__) == True, "Not a closure"
    f1 = s6.myfibonacci()
    assert bool(
        f1.__closure__) == True, "Not a closure"
    f1 = s6.counter(s6.add)
    assert bool(
        f1.__closure__) == True, "Not a closure"
    fn = s6.add
    f1 = s6.counter(fn)
    assert bool(
        f1.__closure__) == True, "Not a closure"
    mypersonaldict = {'add': 0, 'mul': 0, 'div': 0}
    fn = s6.add
    f1 = s6.counter_dict(fn, mypersonaldict)
    assert bool(
        f1.__closure__) == True, "Not a closure"
