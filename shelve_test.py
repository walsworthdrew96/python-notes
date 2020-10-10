from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones')
tom = Manager('Tom Jones', 50000)

import shelve

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()
