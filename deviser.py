class Person:
    def __init__(self, name, contribusion):
        self.name = name
        self.contribusion = contribusion

    def get_info(self):
        return self.name, self.contribusion

def deb(debitor, creditor, middle):
    debitor = debitor - middle
    creditor = creditor + debitor
    return debitor, creditor

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

for i in contribution_list:
    if i.contribusion > middle:

