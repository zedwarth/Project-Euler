#!/usr/local/bin/python3
#Collatz Sequence Research
#Project Euler - Problem 14 - http://projecteuler.net/problem=14
#zedwarth
#Takes a starting number from standard input and print out each step on of the Collatz sequence
#until it reaches one.  It also returns how many number are in the sequence, e.g., an input of '13'
#will return '10'.

import sys

n = int(sys.argv[-1])  #assigns the standard input to 'n' and sets to an integer
list = [n] #holds the list of the Collatz sequence
#print (n, type(n))
while n != 1:
    if n % 2 == 0:
        n = n//2
        list.append(n)
    else:
        n = n*3+1
        list.append(n)
print ( "The list of number in the sequence is:\n",  list,  "\nThe number of terms in the sequence is", len(list))
