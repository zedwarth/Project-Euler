#Progject Euler - Problem 7
#Zedwarth
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#rev fuction returns the the revers of it's imput. 
def rev(f):
    r = int (str(f) [::-1]) 
    #coverts the number to a string, reverses it and then converts it back to a string
    return r

x = 999 * 999
y = 111 * 111

while x >= y:
    if x == rev (x):
        z = [x /y for y in range(100, 999)]
        print ('The answer is ', x, 'With y equaling ', y) 
        break
    else:
        x-= 1
