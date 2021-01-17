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

def cred(credit_member, debit_member, middle):
    if middle - credit_member.contribusion < debit_member.contribusion - middle:
        credit_member.contribusion = middle
        debit_member.contribusion = debit_member.contribusion - middle - credit_member.contribusion

    else:
        credit_member.contribusion = credit_member.contribusion + debit_member.contribusion - middle
        debit_member.contribusion = middle
    return credit_member.contribusion, debit_member.contribusion


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
    credit_members[0] = cred(credit_members[0], debit_members[0], middle)[0]
    debit_members[0] = cred(credit_members[0], debit_members[0], middle)[1]
print(credit_members[0])
print(debit_members[0])