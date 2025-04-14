from collections import namedtuple

Talaba = namedtuple('Student', ['ism', 'familya', 'yosh', 'fakultet'])

talaba1 = Talaba('Yoqub', 'Mardonov', 16, 'Backend Python')

# nomi orqali
print(talaba1.ism)
print(talaba1.familya)
print(talaba1.yosh)
print(talaba1.fakultet)

# indeks orqali
print(talaba1[0])
print(talaba1[1])
print(talaba1[2])
print(talaba1[3])

# _asdict orqali
print(talaba1._asdict())

# _replace orqali
talaba2 = talaba1._replace(yosh = 17)
print(talaba2)

# _fields orqali
print(talaba2._fields)

# _make orqali
data = ['Ali', 'Valiyev', 22, 'Frontend']
talaba3 = Talaba._make(data)
print(talaba3)
