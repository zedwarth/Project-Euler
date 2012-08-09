#Progject Euler - Problem 9
#Zedwarth
#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Generate Pythagorean triplets
a = 3
b = c = 0
x = 1

while x == 1:
    if a % 2 == 0:
        b = a**2/2-.5
        c = b + 1
    else:
        b = a**2/4 -1
        c = b + 2
    if a + b + c == 1000:
        print('The answer is ', a*b*c)
        x = 0
    elif a + b + c > 1001:
        print ('Epic fail!', a,b,c)
        x = 0
    else:
        a += 1
