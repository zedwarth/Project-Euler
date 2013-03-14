#!/usr/local/bin/python3
#Project Euler - Problem 15 - http://projecteuler.net/problem=15
#zedwarth
import math
def biCoe(n,k): #Binomial coefficient; n take k
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))
x = 20
y = 20

print(biCoe(x+y,x)) #latice path combinations given restrictions of only east or north can be expresed as x+y, take x
