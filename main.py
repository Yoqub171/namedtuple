from collections import namedtuple

Talaba = namedtuple('Student', ['ism', 'familya', 'yosh', 'fakultet'])

talaba1 = Talaba('Yoqub', 'Mardonov', 16, 'Backend Python')
print(talaba1.ism)
print(talaba1.familya)
print(talaba1.yosh)
print(talaba1.fakultet)


print(talaba1[0])
print(talaba1[1])
print(talaba1[2])
print(talaba1[3])


print(talaba1._asdict())


talaba2 = talaba1._replace(yosh = 17)
print(talaba2)


print(talaba2._fields)


data = ['Ali', 'Valiyev', 22, 'Frontend']
talaba3 = Talaba._make(data)
print(talaba3)
