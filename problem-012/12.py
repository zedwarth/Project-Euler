#Progject Euler - Problem 12 - http://projecteuler.net/problem=12
#Zedwarth
#Find the value of the first triangle number to have over five hundred diviors.

def factor (n):
   largest = int (n ** .5) #Find the square root of n and store it as an integer.
   count = 2 #Holder for the number of factors of n. 1 and n are assumed.
   x = 2 #Holder for the potental factor being tested, starting with 2.
   while x != largest + 1: #Test for x in range 2, int(n**.5)
      if n % x == 0:       #If x is a factor increase factor count and try next number in range 
         count = count + 1
         x = x +1
      else:                #If x is not a factor try next number in range
         x = x +1
   return (count * 2 - 2)

tnum = 1   #The nth triangle number.
tvalue  = 0   #Set inital value to zero.
stop = 0         #Flow control
while stop != 1:
   tvalue  = sum(range(tnum+1)) #Find the vaule of the nth Triangle number
   if factor (tvalue) > 500:
       print ("The answer is ", tvalue, ". The ", tnum, "th triangle number.")
       stop = 1
   else:                        #else, try the next triangle number
       tnum = tnum + 1
