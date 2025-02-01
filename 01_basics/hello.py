print("hello")

# funtions in python
def number(n):
    print(n)

number(10)

# -------------------------------------------------------------------
# ocatal number 
print(0o20) 
# Hex number
print(0xFF)
# binary number
print(0b1000)

# binary to other numbers
print(oct(64))
print(hex(64))
print(bin(64))

# integer to other format : int(value, base number of format)
print(int('64' , 8))
print(int('64' , 16))
print(int('1000' , 2))





# -------------------------------------------------------------------
import random
print(random.random())
print(random.randint(1, 2000)) # give any number between 1 to 2000


l1 = ['lemon', 'ginger', 'mint', 'masala'];
print(random.choice(l1))

random.shuffle(l1)
print(l1)





# -------------------------------------------------------------------
# get unexpected result
print(0.1 + 0.1 + 0.1 - 0.3)

from decimal import Decimal
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1))





# -------------------------------------------------------------------
# sets: we can perform oprations on it like intersection, etc
setOne = {1,4,7,9}
print(setOne & {1,5,9})  # intersection
print(setOne | {1,5,9})  # union

print(setOne - {1,4})
print(type({}))
print(type(set()))





# -------------------------------------------------------------------
# slice method
slice = "hello guys"
print(slice[0:6])
slice_method = "hello guys you fuckers"
# method[start, end, hoop]
print(slice_method[2:15:2])

# lower case method
first = "Hello Fuckers"
print(first.lower())

second = "Hello Fuckers"
print(second.upper())

# strip method like trim()
strip_method = '   hello fuckers    '
print(strip_method.strip())

# replace method 
replace_method = 'hello bsdk'
print(replace_method.replace("hello", "hii"))
print(replace_method)

# split method : string to array
car = 'thar, i10, scarpio, ford'
print(car.split(", "))

# count the number of words in string
count_words = "hii guys how how are you how"
print(count_words.count("how"))





# -------------------------------------------------------------------
# set the varibles iunside the string
order = "I booked my {} which is {} model" 
car = "i10"
model = 2025
print(order.format(car, model))

# arrary or list to string
car1 = ['thar', 'i10', 'scarpoi']
print("".join(car1))
print(" ".join(car1))
print("-".join(car1))


aosomeCar = "He said. \"scarpoi car is asome\" "
print(aosomeCar)

path_row = r"c:\user\id"
print(path_row)






# -------------------------------------------------------------------
# list
car2 = ['thar', 'sfcarpio', 'i10', 'bemer']
print(car2)
print(car2[1:])
car2[1:2] = 'benz' # check issue
print(car2)

car3 = ['thar', 'sfcarpio', 'i10', 'bemer']
car3[1:2] = ["benz", "hummer"]
print(car3)
car3[1:3] = []
print(car3)

for car in car3:
    print(car, end="-")

car3.append("aura")
print(car3)

car3.pop()
print(car3)

car3.remove("thar")
print(car3)

car3.insert(1, "thar");
print(car3)





# -------------------------------------------------------------------
square_num = [x**2 for x in range(30)]
print(square_num)
# -------------------------------------------------------------------
# dictinory
dcar = {'scapio' : 'gangster', 'i10' : 'middleclass', 'fortuner' : 'politian'}
print(dcar.get('i10'))

dcar["fortuner"] = "superman"
print(dcar)
for car in dcar:
    print(car, dcar[car])

for key, value in dcar.items():
    print(key, value)

dcar.pop("i10")
print(dcar)

dcar.popitem()
print(dcar)

dcar["aura"] = "middle c"
dcar["paltina"] = "superbike"
print(dcar)

del dcar["aura"]
print(dcar)

dcar["aura"] = 'nprmal'
print(dcar)

squareInDic = {x:x**2 for x in range(10)}
print(squareInDic)




# -------------------------------------------------------------------
# tuple: immutable
car4 = ('thar', 'i10', 'i20', 'aura')
(car1, car2 , car3 , car4) = car4
print(car1)

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------