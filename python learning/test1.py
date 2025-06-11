import math  # importing file
first_word = 'Hello word'

print(first_word)  # printing


two_words = 5
print(two_words)

course_name = 'Lubowa'  # string
is_published = False  # boolean
is_Not_pulished = True  # boolean
x = 1  # Number
y = 2.5  # float

print(len(course_name))  # counting
print(course_name[0])  # picking out the first letter
print(course_name[-1])  # print the last string from the string
print(course_name[0:3])  # range with the string

print(course_name[0:])
print(course_name[:3])
print(course_name[:])

course = 'Computer \' programming'  # \ escape
course1 = 'Computer \n ' ' programming'  # \n new line
print(course + course1)

# Sting

first_name = 'Lubowa'
last_name = 'Edris'
full_name = first_name + ' ' + last_name  # Or
full_name = f'{first_name} {last_name}'
print(full_name)
print(full_name.upper())  # making Upper case letters
print(full_name.lower())  # lower case
print(full_name.title())  # first letter Upper
print(full_name.strip())  # remove space
print(full_name.rstrip())  # right remove space
print(full_name.lstrip())  # left remove space
print(full_name.find('lu'))  # find letter
print(full_name.replace('L', 'g'))  # replacing
print('u' in full_name)  # checking if yes then True boolean
print('swift' not in full_name)


# Numbe

# when using math in your code you need to import math object


x = 1
y = 2.2
z = 2j

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # Whole number
print(x % y)  # reminder
print(x ** y)  # power

q = 10
q += 20  # ro q = q + 20
q -= 20  # ro q = q - 20

# number functions
print(round(2.9))  # round off the numbee
print(abs(-2.9))  # take off the negative

print(math.ceil(2.9))  # round off to the nearset higher whole number

# data type converting
int(x)  # to number
float(x)  # to floating number
bool(x)  # to boolean
str(x)  # to string

# x =input('x: ')  #asking user input
# y = int(x) + 1  #converting
# print(f'x: {x}, y: {y}') #print as it is

# falsy value
# 1 ''
# 0
# None

10 > 3
10 >= 3
10 == 10  # equal
10 != 10  # not equal

# Condition statements

temputure = 12
if temputure > 30:
    print('its warm \n Drink water')
elif temputure > 20:
    print('its nice')
else:
    print('its cool')
print('Done')


# a proggram that check eligibale age to campus

age = input('Age: ')

if int(age) >= 18:
    message = 'Eligible'
else:
    message = 'Not eligible'
# print(message)

# addvesited if statement
message = 'Eligible' if int(age) >= 18 else 'Not Eligible'
print(message)


# logical operators
# 1. and
# 2. Or
# 3. not

# a program to give out loans

high_income = True
good_credit = True
student = True

if high_income and good_credit:  # both must be true
    print('Eligible')
else:
    print('Not Eligible')

if high_income or good_credit:  # bOne needs to be true
    print('Eligible')
else:
    print('Not Eligible')

if not student:  # if not
    print('Eligible')
else:
    print('Not Eligible')

if (high_income or good_credit) and not student:  # checks 3 conditions
    message = 'Eligible'
else:
    message = 'Not Eligible'
print(message)


message = 'Eligible' if (
    high_income or good_credit) and not student else 'Not Eligible'
print(message)
