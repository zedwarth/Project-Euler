#Progject Euler - Problem 9
#Zedwarth
#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
lim= 1001
m, n, r = 2, 1, 1
while r == 1: #Main loop 
#Generate Simple Pythagorean triplets
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    if a+b+c > lim: #End program if all hope is lost
        print('Epic FAIL!', a, b, c)
        r=0
    elif a+b+c == 1000: #Check to see if the current simple triplet is the answer
        print('The triplet is a=',a,', b=',b,', and c=', c,'.  The product of the triplet is ', a*b*c)
        r=0
    else: #Generate the complex triplets based on the current simple ones
        print('Curent simple triplets are:', a,b,c)
        k = 2
        x ,y, z = a, b, c
        while x+y+z< lim:
            x ,y, z = a, b, c
            x , y, z = k*x, k*y, k*z
            print('Curent complex triplets are:', x,y,z)
            if x+y+z == 1000:
                print('The triplet is a=',x,', b=',y,', and c=', z,'.  The product of the triplet is ', x*y*z)
                r=0
                break
            else:
                k += 1
        m, n, = m+2, n+2
