from person import Person, Manager
import shelve

bob = Person('Bob Smith')
sue = Person('Sue Jones')
tom = Manager('Tom Jones', 50000)

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()
