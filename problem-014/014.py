#!/usr/local/bin/python3
#Project Euler - Problem 14 - http://projecteuler.net/problem=14
#zedwarth
#

def hailstone(n):
    list = [n] #holds the list of the Collatz sequence
    while n != 1:
        if n % 2 == 0:
            n = n//2
            list.append(n)
        else:
            n = n*3+1
            list.append(n)
    return len(list)

largest = 1  #holds the value of the number that has the largest distance to one
terms = 1    #holds the number of terms

for n in range(1,1000000):
    size = hailstone(n) #The number of terms in for the sequense starting with 'n'
    if size  > terms:   #If the size is the greater than the previious largest
        largest, terms = n, size
print (largest)
