#q1
'''def nearest_palindrome(number):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    i = number + 1
    while True:
        if is_palindrome(i):
            return i
        i += 1
print(nearest_palindrome(99))   
print(nearest_palindrome(1221))'''
#q2
'''def find_speciality(patient_medical_speciality_list):
    speciality={"P":"pediatrics","O":"orthopedics","E":"ENT"}
    speciality_counts={"P":0,"O":0,"E":0}
    if P>E and P>O:
        speciality=medical_speciality['P']
    elif E>O:
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']
    return speciality
patient_medical_speciality_list=[301,'P',302,'P',305,'P',401,'E',656,'E']

speciality=find_speciality(patient_medical_speciality_list)
print(speciality)'''

#another
'''def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    max_visit=0
    P=patient_medical_speciality_list.count ('P')
    E=patient_medical_speciality_list.count ('E')
    O=patient_medical_speciality_list.count ('O')
    if P>E and P>0:
         speciality= medical_speciality ['P']
    elif E>O:
         speciality= medical_speciality ['E']
    else:
         speciality= medical_speciality ['O']
    return speciality
patient_medical_speciality_list=[301,'P',302,'P',305,'P',401,'E',656,'E']
medical_speciality={"P":"Peddiatrics","O":"Orthopedics","E":"ENT"}
speciality= max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
'''
#q3
'''
def find_common_chars(str1, str2):
    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')
    common_chars = set()
    for char in str1:
        if char in str2:
            common_chars.add(char)
    if len(common_chars) == 0:
        return -1
    return ''.join(sorted(common_chars))
str1 = "I like Python"
str2 = "Java is a very popular language"
result = find_common_chars(str1, str2)
print(result)'''
#q4
#code snippet?
'''
class Example:
    def __init__ (self,num):
        self.num=num
        
    def set_num (self,num):
        self.num=num

    def get_num (self):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''
#q5
'''
class Customer:
    def __init__(self,id):
        self_id = 100

c1=Customer(200)
print(c1.id)

class customer:
    def __init__(self,id):
        self.id=id
c1=Customer(200)
print(c1.id)
'''
#q6
'''
class book:
    def __init__(self):
        self.title=None
my_fav=book()
my_fav.title="head first programming"
your_fav=book()
your_fav.title="learing python"

print("my favorite is",my_fav.title)
print("your's is",your_fav.title)
'''

#q6
'''
class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material

s1=Shoe(1000, "Canvas")
print(s1)
print(s1.price,s1.material)
'''
'''
class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
    def __str__(self):
        return "shoe with price: "+ str(self.price)+"and material:" + self.material


s1=Shoe(1000, "Canvas")
print(s1)    
'''       
#q7
'''class Mobile:

    def display(self):
        print("Displaying details")

    def purchase(self):
        self.display()
        print("Calculating price")

Mobile().purchase()
Mobile().purchase()
m1=Mobile()
print(m1)
m2=Mobile()'''
#
'''
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand == "Redmi":
            discount = 10
        else:
            discount=5
        self.total_price=self.price-self.price * (discount/100)
        print("Total price of",self.brand,"mobile is",self.total_price)
mob1=Mobile("Redmi",20000)
mob2=Mobile("Realmi",10000)
mob1.purchase()
mob2.purchase()
'''
#
class Customer:
    def __init__(self, cust_id, name, age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance(self)
    def show_balance(self):
            print("the balance is",self.wallet.balance)
c1=Customer(100,"Gopal",24,1000)


'''c1=Update_balance(500)
c1.show_balance()
  '''

print(c1.get_wallet_balance())
c1.set_balance(5000)
print(c1.get_wallet_balance())

















































    













































        
