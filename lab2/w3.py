
# BOOLEAN VALUES

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")



#PYTHON OPERATORS

x = 5
print(x)   # x = 5

x += 3
print(x)  # x = x + 3

x -= 3
print(x)  # x = x - 3

x *= 3
print(x)  # x = x * 3

x /= 3
print(x)  # x = x / 3

x %= 3
print(x)  # остаток от деления 

x //= 3
print("//= :", x)  # округленное деление

x **= 3
print("**= :", x)  # возведение в степень


print(5 + 4 - 7 + 3)  #5


#PYTHON LISTS

#Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)


# To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])                        #cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])        #['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])         #['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# The insert() method inserts an item at the specified index

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)          #['apple', 'banana', 'watermelon', 'cherry']


# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) 

# The remove() method removes the specified item.
# (If there are more than one item with the specified value, the remove() method removes the first occurrence)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.
# (If you do not specify the index, the pop() method removes the last item.)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)      #['apple', 'banana']

# The del keyword also removes the specified index:
# The del keyword can also delete the list completely.

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)        #is not defined

# The clear() method empties the list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)      #[]

# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


newlist = [x.upper() for x in fruits]   #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['hello' for x in fruits]     #['hello', 'hello', 'hello', 'hello', 'hello']

# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# To sort descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)         # Z to A

# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)     # Если ты изменишь оригинальный список, копия не изменится

# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


''' 
append() – добавить элемент в конец списка
clear() – очистить список (сделать пустым)
copy() – сделать копию списка
count() – посчитать, сколько раз встречается значение
extend() – добавить все элементы из другого списка
index() – найти номер (индекс) первого элемента с нужным значением
insert() – вставить элемент в определённое место
pop() – удалить элемент по индексу (по умолчанию последний)
remove() – удалить элемент по значению
reverse() – перевернуть список (с конца в начало)
sort() – отсортировать список (по алфавиту или по возрастанию)
'''


# PYTHON TUPLES

''' нельзя добавлять, удалять или менять элементы после создания '''

# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)     # apple  banana  cherry

# Using Asterisk*

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)                   #apple
print(yellow)                  #banana
print(red)                     #['cherry', 'strawberry', 'raspberry']

# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)                 #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')



# SETS

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets cannot have two items with the same value

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)                 #{'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)                 #True and 1 is considered the same value

# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)                   #{'cherry', 'apple', 'orange', 'banana'}

# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)            #set()

# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)             #is not defined

# The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

''' You can use the | operator instead of the union() method, and you will get the same result.
set3 = set1 | set2 '''

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)                # {'apple'}

''' You can use the & operator instead of the intersection() method, and you will get the same result.'''

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)                # {'banana', 'cherry'}

''' You can use the - operator '''


# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)                  # {'google', 'banana', 'microsoft', 'cherry'}

''' You can use the ^ operator '''

# Create a frozenset and check its type: ( замороженное множество, тоесть после создания ты уже не можешь добавлять или удалять элементы)

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


''' 
add() – добавить элемент
clear() – очистить (сделать пустым)
copy() – скопировать множество
difference() – разница (что есть в первом, но нет во втором)
difference_update() – убрать из множества всё, что есть и во втором
discard() – удалить элемент (без ошибки, если его нет)
intersection() – пересечение (что общее у двух множеств)
intersection_update() – оставить только общие элементы
isdisjoint() – проверить, есть ли общие элементы (True/False)
issubset() – проверить, все ли элементы множества входят в другое (подмножество)
issuperset() – проверить, содержит ли множество другое (надмножество)
pop() – удалить случайный элемент
remove() – удалить конкретный элемент (ошибка, если нет)
symmetric_difference() – элементы, которые разные (не общие)
symmetric_difference_update() – обновить множеством, оставив только разные элементы
union() – объединить множества
update() – добавить элементы из другого множества
'''

#PYTHON DICTIONARIES

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)           # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])       # Ford

# Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)            # {'name': 'John', 'age': 36, 'country': 'Norway'}


# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x)  #before the change
car["color"] = "white"
print(x)  #after the change


# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


# Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})        # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Removing Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}               # {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


print(myfamily["child2"]["name"])    # Tobias



# IF ... ELSE

''' 
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

# If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")    # b is greater than a

# Elif 

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")       # a and b are equal

# Else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")      # a is greater than b

# One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

# And

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Or

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Not

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Nasted if

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass


# MATCH

day = 4

match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")                 #Thursday


# WHILE LOOPS

i = 1
while i < 6:
  print(i)
  i += 1


# With the break statement we can stop the loop even if the while condition is true:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# FOR LOOPS

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)               # b a n a n a

# break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# continue

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)    # apple  cherry


# range()

for x in range(6):
  print(x)           # 0 1 2 3 4 5

for x in range(2, 30, 3):
  print(x)           # 2 5 8 11 14 17 20 23 26 29


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

# red apple  
# red banana  
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

