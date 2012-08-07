#Problem 3
#Project Euler
#Zedwarth
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math #import the math module for the square root fuction
n = 600851475143 #the number the program will find the largest prime factor for
f = 0 #the holder for the potential highest prime, this will be the answer output
l = 2 #the holder for the lowest factor 
p = 0 #prime number found flag

while p == 0:
    #print "l=", l
    if n%l==0: #find if l is a factor of n
        f = n/l #use l to find it's corisponding high factor
        #print 'f=',f
        z = math.sqrt(f) #the squareroot of f is the highest number needed to test for primality
        #print "z=",z
        y = 2 #delcare y to be two for each time the while loop is run
        while y <= z: #Primality test
            if f%y!=0: #Is f divisable by y?
                y += 1 #If no then add 1 to y and see if that's divisable
            else:
                l += 1 #try the next number as a potential factor
                break
        else:
            print 'Highest prime factor found ',f
            p = 1

    else:
        l+=1 #if l is not a factor try l+1 to see if that is one
