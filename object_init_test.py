class A:
    pass


a = A()

print(a.__dict__)
print(a.__class__)
print(a.__class__.__bases__)
print(a.__class__.__bases__[0].__dict__)

for k, v in a.__class__.__bases__[0].__dict__.items():
    print(f'{k}: {v}')
