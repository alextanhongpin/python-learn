from collections import namedtuple

Employee = namedtuple('Employee', 'name, age, gender, title, department')

print(Employee)
jack = Employee('Jack', 25, 'M', 'Programmer', 'Engineering')
print(jack)
for field in jack:
    print(field)

updated_jack = jack._replace(age=32)
print(updated_jack)
