#!/usr/bin/env python3
#Project Euler - Problem 17 - http://projecteuler.net
#
numbers = { 0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}

total = 0
def nwords(n):
    ''' Given an int n, from 1-1000, the fuction will reference the numbers dictionary and return a string of n written out as words
        example:
        nwords(101)
        'onehundredandone'
    '''
    n = str(n)
    if len(n) == 1:
        return (numbers[int(n)])
    if len(n) == 2:
        return (numbers[int(n[-2])*10] + numbers[int(n[-1])])
    if len(n) == 3:
        return (numbers[int(n[-3])] + 'hundredand' + numbers[int(n[-2])*10] + numbers[int(n[-1])])
    if len(n) == 4:
        return (numbers[int(n[-4])] + 'thousand'

for i in range(1,1001):
    total += len(nwords(i))

print(total)
