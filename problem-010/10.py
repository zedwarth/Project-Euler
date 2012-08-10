#Progject Euler - Problem 10
#Zedwarth
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

prime = [2, 3,]
lim= 2000000
x = 5 # number being tested for primality
z = 1 # slice of prime
while prime [-1] < lim:
    #print (prime[-1])
    y = prime [z] 
    #print(x, ' is being tested for primeality against ', y)
    if x % y == 0: #if x every fails primality test, move to next odd number
        #print('Primality of ',x," failed.  Divisable by ", y)
        x += 2
        z = 1
    elif y < x**.5:
        #print(x, 'is prime because it has been test for every prime up to ',y)
        z += 1
    else: #if every prime number has been check then add x the list of primes
        #print(x, y)
        prime.append(x)
        z, x = 1, x + 2
if prime [-1] > lim:
    prime.pop()
print(sum(prime))
