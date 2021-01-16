'''
определяет сумму кто кому сколько должен
при солидарном участии
'''
class Person:
    def __init__(self, name, contribusion):
        self.name = name
        self.contribusion = contribusion

    def get_info(self):
        return self.name, self.contribusion

members = []
credit_members = []
debit_members = []
contribution_list = []
numbers = int(input('введите колличество участников:'))
for i in range(numbers):
    member = Person(str(input('Введите имя:')), float(input('Введите первоначальный взнос:')))
    members.append(member)
for i in members:
    contribution_list.append(i.contribusion)
middle = sum(contribution_list)/numbers
for i in members:
    if i.contribusion < middle:
        credit_members.append(i)
    else:
        debit_members.append(i)
if len(credit_members) < 1:
    print('никто никому ничего не должен!!!')
else:
    for i in credit_members:
        for j in debit_members:
            if middle - i.contribusion < j.contribusion - middle:
                if middle - i.contribusion != 0:
                    print(i.name, 'должен', j.name, round(middle - i.contribusion, 2), 'руб.')
                i.contribusion = middle
                j.contribusion = j.contribusion - (middle - i.contribusion)

            else:
                if j.contribusion - middle != 0:
                    print(i.name, 'должен', j.name, round(j.contribusion - middle, 2), 'руб.')
                i.contribusion = i.contribusion + j.contribusion - middle
                j.contribusion = middle
    print('Общие затраты:', round(sum(contribution_list), 2), 'руб.')
    print('Сумма с каждого', round(middle, 2), 'руб.')