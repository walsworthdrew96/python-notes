X = 11


# def f():
#     global X
#     nonlocal X
#     X = 57
#     print('print in f():', X)


def h():
    X = 87
    print('print in h() before f():', X)

    def f():
        # global X
        nonlocal X
        X = 57
        print('print in f():', X)
    f()

    print('print in h() after f():', X)


def g():
    X = 22
    print('print in g():', X)


class C:
    X = 33

    def m(self):
        X = 44
        self.X = 55


if __name__ == '__main__':
    print('print in main():', X)
    # f()
    g()
    h()
    print('print in main() after f() and g():', X)

    obj = C()
    obj2 = C()
    print(f'obj.X: {obj.X}')
    print(f'obj2.X: {obj2.X}')
    print(f'C.X: {C.X}')
    print('\nC.X = 27')
    C.X = 27
    print(f'\nobj.X: {obj.X}')
    print(f'obj2.X: {obj2.X}')
    print(f'C.X: {C.X}')
    print('\nobj2.X = 47')
    obj2.X = 47
    print(f'\nobj.X: {obj.X}')
    print(f'obj2.X: {obj2.X}')
    print(f'C.X: {C.X}')
    # print(f'C.__class__.__dict__:\n{C.__class__.__dict__}')
    # for k, v in C.__class__.__dict__.items():
    #     print(f'{str(k).rjust(20)}: {str(v)}')
    # print(f'obj2.__class__.__dict__:\n{obj2.__class__.__dict__}')
    print(C.X)

    obj.m()
    print(obj.X)
    print(C.X)

    print('Basically static members can be accessed through the class, or through the instance if there is not an\n' +
          'instance variable with the same name.')
