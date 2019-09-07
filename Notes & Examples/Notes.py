# Mod Operator
7%4 

#POWERS
2 ** 8

(2 + 10) * (10+3)

#VARIABLES
a = 10

a = a + a

type(a)

my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

#STRINGS
print('Hello World One.')
print('Hello World Two.')

#Esc Sequence
print('Hello \nworld')
#Tab Sequence
print('Hello \tworld')

#LENGTH
len("I am a String")

#INDEXING
myString = "Hello World"
myString[0]
myString[8]
myString[-2]

#SLICING
myString = 'abcdefghijkl'

myString[2:] 
myString[:3]
myString[3:6]
myString[::3]
myString[::-1]

#Properties & Methods
name = 'Ethan'

last_letters = name[2:]

#CONCATANATIONS
"Nat" + last_letters

letter = 'z'

letter * 10

"3" + "2"

#METHODS 
x = "Hello World"

x.upper()
x.lower()
x.split()

#Print Formatting Strings
print('This is a string {}'.format('INSERTED'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

#Float Formatting
result = 100/777

print('The Result Was {r:1.3f}'.format(r=result))

#Ver. 3.6
name = "Jose"

print(f'Hello, his name is {name}')

#LISTS
myList = ['one', 'two', 'three']

myList[0]
myList[1:]

myList.append('four')
myList.pop()

num_list = [4, 2, 1, 3]

num_list.sort()

#DICTIONARIES

my_dict = {"key1":'value1', 'key2':'value2'}

my_dict['key1']

d = {'k1': 123,'k2':[1,2,13],'k3':{'insideKey':100}}

d['k2']

d['k3']['insideKey']

d['k4'] = 300

d['k1'] = 'New Value'

d.keys()

d.values()

d.items()

#TUPLES
t = (1,2,3)

type(t)

len(t)

t.index(2)

#BOOLEANS
type(False)

1 > 2

#COMPARISONS 
2 == 2
#True
2 == 1
#False
'helo' == 'bye'
#False
2.0 == 2
#True
4 != 2
#True
#< <= > >=

1 < 2 and 2 > 3
#False
'h' == 'h' and 2 == 2
#True

1 == 1 or 2 == 3
#True

#If, Elif, and Else Statements
if 3 > 2:
    print('ITS TRUE')
else:
    print('ITS FALSE')

#FOR LOOPS
myReadyList = [1,2,3,4,5,6,7,8,9,10]

for item in myReadyList:
    print(item)

for num in myReadyList:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in myReadyList:
    list_sum = list_sum = num

    print(list_sum)

myTupleList = [(1,3,5),(2,4,6),(3,5,8)] 

for a,b,c in myTupleList:
    print(b)

#WHILE LOOPS
x = 0

while x < 5:
    print(f'The current value is {x}')
    x = x + 1

y = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

#OPERATORS 
opList = [1,2,3]

for num in range(0,10,2):
    print(num)

list(range(0,10,2))

opLetters = ['a','b','c']

for item in zip(opList, opLetters):
    print(item)

list(zip(opList,opLetters))

'a' in opList
'a' in opLetters

min(opList)
max(opList)

# input('Enter a Number Here: ')0-+

#METHODS && FUNCTIONS
def name_function():
    print('Hello')

name_function()

def say_hello(name='NAME'):
    return 'hello '+name

result = say_hello('Jose')

result

def add(a,b): 
    return a+b

addition = add(2, 4)

addition

def dog_check(mystring):
    return 'dog' in mystring.lower()

dog_check('My Dog ran away')

def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    
    return pig_word

pig_latin('apple')

#ARGS && KWARGS
def myFunc(*args):
    print(args)

myFunc(40,60,70,80)

def fruitFunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['kwargs']))
    else:
        print('I did not fins any fruit.')

fruitFunc(fruit='apple', veggie='lettuce')

def thisFunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

thisFunc(10,20,30,fruit='orange',food='eggs',animal='dog')

#FUNCTION PRACTICE EXERCISES 1
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

def animal_crackers(text):
    wordList = text.split()

    return wordList[0][0] == wordList[1][0]

def makes_twenty(n1,n2):
    return n1 + n2 == 20 or n1 == 20 or n2 ==20

def old_mcdonald(name):
    firstHalf = name[:3]
    secondHalf = name[3:]

    return firstHalf.capitalize() + secondHalf.capitalize()

def master_yoda(text):
    wordList = text.split()
    reverse = wordList[::-1]
    return ' '.join(reverse)

def almost_there(num):
    return (abs(100 - num) <= 10) or (abs(200 - num) <= 10)

#FUNCTION PRACTICE EXERCISES 2
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True

    return False

def paper_doll(text):
    result = ''

    for char in text:
        result += char*3
    return result

def black_jack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in ([a,b,c]) and sum([a,b,c]) <= 31:
        return sum([a,b,c]) - 10
    else:
        return 'BUST'

def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

def spy_game(nums):
    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1

def count_primes(num):
    if num < 2:
        return 0
    
    primes = [2]
    x = 3

    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)