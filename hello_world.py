def helloworld():
    print("Hello World")
    return helloworld

helloworld()

l1 = [] #empty list
for element in range(0, 10): #element from 0 to 10
    l1.append(element) #add the element into l1 list
print(l1) #print the list.

class BankAccount(object):
    def __init__(self, first_name, last_name, uid):
        self.first_name = first_name
        self.last_name = last_name
        self.uid = uid
    def __str__(self):
        return f"BEGINNING:\n{self.first_name} {self.last_name}\n{self.uid}\nEND OF CLASS PRINTING"

id0 = BankAccount("Ron","Cohen",322492893)
print(id0)
        

