#Progject Euler - Problem 7
#Zedwarth
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math
#Find the sum of the squares of the first one hundred nautral numbers
a = 0
for x in range(1, 101):
    a += x ** 2
#Find the square of the sum of the first one hundred natural numbers
b = 0
for x in range(1, 101):
    b += x
b = b ** 2

#Find the difference between the sum of the square 'b' and the square of the sums 'a'
print (b-a)
