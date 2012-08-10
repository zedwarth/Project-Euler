#Progject Euler - Problem 9
#Zedwarth
#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
def tri (m, n, k):
    a, b, c = k*(m**2 - n**2), k*(2*m*n), k*(m**2 + n**2)
    return (a, b, c)
m, n, k, x = 2, 1, 1, 1

while x == 1:
    for k in range(1, 1000):
        a, b, c = tri (m, n, k)
        #print('a = ', a,'b = ', b,'c = ', c, 'm = ',m, 'n = ', n, 'k = ', k)
        if a+b+c == 1000000:
            print('Answer is: ', a*b*c)
            x = 0
    if n + 1 < m:
        n += 1
    else:
        m, n = m +1, 1


