#Progject Euler - Problem 4
#Zedwarth
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#rev fuction returns the the revers of it's imput. 
def rev(f):
    r = int (str(f) [::-1]) 
    #coverts the number to a string, reverses it and then converts it back to a string
    return r

x = 999 * 999
y = 100 * 100

while x >= y:
    if x == rev (x):
        for z in range (100, 1000):
#            print (x, z)
            if x % z == 0:
                if len (str(x//z)) == 3:
                    print ('The answer is ', x, 'With z being ', z) 
                    x = 0
    x-= 1
