#Progject Euler - Problem 7
#Zedwarth
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#rev fuction returns the the revers of it's imput. 
def rev(f):
    r = int (str(f) [::-1]) 
    #coverts the number to a string, reverses it and then converts it back to a string
    return r

h = 999 * 999
l = 111 * 111

if [f == rev(f) for f in reversed((range (l, h)))]:
    print ('The answer is ', f)
    break
