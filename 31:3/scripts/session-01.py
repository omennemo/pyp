# -*- coding: utf-8 -*-
"""
@filename: session-01.py
@author: cyruslentin
"""

# print
print("Hello World!!!")
print("Hello Cyrus!!!")

# input
name = input("Enter your name: ")
print("Hello " + name)

# integer
quantity = 3
print(quantity)
type(quantity)

quantity

# float
price = 2.5
print(price)
type(price)

price

# float
price = 3.0
print(price)
type(price)

price

#boolean
status=True 
print(status)
type(status)

status

# string
message="Hello World!!!"
print(message)
type(message)

message

# maths operations
x = 10
y = 20
z = x + y
print(z)
z = x - y
print(z)
z = x * y
print(z)
z = x / y
print(z)
z = y ** x
print(z)
z = y ** 2
print(z)
z = y % x
print(z)

# auto casting
print(price)
print(type(price))
print(quantity)
print(type(quantity))
amount = price * quantity
print(amount)
type(amount)

# explicit conversion
price=int(price)
print(price)
print(type(price))
print(quantity)
print(type(quantity))
amount = price * quantity
print(amount)
type(amount)

# number from string
x = "123"
print(x)
type(x)

x = int(x)
print(x)
type(x)

x = float(x)
print(x)
type(x)

# if statement
x = 5
if x == 5:
	print('Equals 5')
if x > 4:
	print('Greater than 4')
if x >= 5:
	print('Greater than or Equals 5')
if x < 6: 
	print('Less than 6')
if x <= 5:
	print('Less than or Equals 5')
if x != 6:
	print('Not equal 6')

# another if
print('Before 5')
x = 5
if x == 5:
 print('Is 5		 ')
 print('Is Still 5')
 print('Third 5   ')
 print('After 5   ') 
 print('Before 6  ') 
if x == 6:
    print('Is 6      ')
    print('Is Still 6')
    print('Third 6   ')
    print('After 6')

x = int(input("Please enter an integer: "))
if x < 0:
   x = 0
   print('Negative changed to zero')
elif x == 0:
   print('Zero')
elif x == 1:
   print('Single')
else:
   print('More')

# prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# prints out 3,4,5
for x in range(3, 6):
    print(x)

# prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
    
# for loop ... strange!!!
for i in range(10):
    print(i)
    i = 5  

# while loop
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

