class Person:
    def __init__(self, name, contribusion):
        self.name = name
        self.contribusion = contribusion

    def get_info(self):
        return self.name, self.contribusion

def sep(credit_list, debit_list, middle):
    pass
    #for i in credit_list:
        #for j in debit_list:
            #j.contribusion = j.contribusion - (j.contribusion - middle)
            #i.contribusion = i.contribusion + (j.contribusion - middle)



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
            if middle - i.contribusion <= j.contribusion - middle:
                i.contribusion = i.contribusion + (middle - i.contribusion)
                j.contribusion = middle

            else:
                i.contribusion = middle
                j.contribusion = j.contribusion - (middle - i.contribusion)

