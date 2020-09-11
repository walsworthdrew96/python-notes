# said to be immutable: strings, integers, tuples
# said to be mutable: lists, dicts

# immutable (value types (primitives)) and specific objects like tuples
string1 = 'original_string'
integer1 = 7
tuple1 = (1, 2, 3)

# mutable (mutable objects and iterables)
list1 = [1, 2, 3]
dict1 = {'a': 'a', 'b': 'b', 'c': 'c'}

# unknown
set1 = {1, 2, 3, 3, 3, 3, }


def test_mutable_immutable(string_arg, integer_arg, tuple_arg, list_arg, dict_arg, set_arg):
    # immutable modification
    string_arg = 'new_string'
    integer_arg = -7
    tuple_arg = (7, 7, 7)

    # sets can't be changed in place, so replacing the object doesn't work.
    set_arg = {7, 7, 7}

    # mutable modification
    list_arg[2] = 7
    dict_arg['c'] = 'Z'

    # replace mutable object with a new object, what happens?

    list_arg = [7, 7, 7]
    dict_arg = {'z': 'z'}

    # seems to be the case that if the objects passed into the function are not modified directly, they do not change.
    # sets can't be changed via item assignment so they are effectively immutable.


print(f'BEFORE\nstring1: {string1}\ninteger1: {integer1}\ntuple1: {tuple1}\nset1: {set1}\n\nlist1: {list1}\ndict1: {dict1}')
test_mutable_immutable(string1, integer1, tuple1, list1, dict1, set1)
print(f'\nAFTER\nstring1: {string1}\ninteger1: {integer1}\ntuple1: {tuple1}\nset1: {set1}\n\nlist1: {list1}\ndict1: {dict1}')


# every variable in python is a pointer to an object
# every value in python is an object. even integers and strings.

# passing a list using list_name[:] will give a copy and leave the original list unchanged.

# python multiple assignment syntax can be used to assign multiple return values from a function call
# example: L1, L2 = myfunc(L1[:], L2[:])


def func1(a, b=4, c=5):
    print('func1:', a, b, c)


func1(1, 2)


def func2(a, b, c=5):
    print('func2:', a, b, c)


func2(1, c=3, b=2)


def func3(a, *pargs):
    print('func3:', a, pargs)


func3(1, 2, 3)


def func4(a, **kargs): print('func4:', a, kargs)


func4(a=1, c=3, b=2)


def func5(a, b, c=3, d=4): print('func5:', a, b, c, d)


func5(1, *(5, 6))


def func6(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'


l = 1
m = [1]
n = {'a': 0}
func6('func6:', l, m, n)
