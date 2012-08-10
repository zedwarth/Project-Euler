#Progject Euler - Problem 10
#Zedwarth
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

lim= 2000000
prime = [2, 3,]
x = 5 # number being tested for primality
z = 1 # slice of prime
while prime [-1] < lim:
    y = prime [z] 
    if x % y == 0: #if x every fails primality test, move to next odd number
        x += 2
    elif y < x**.5:
        z += 1
    else: #if every prime number has been check then add x the list of primes
        prime.append(x)
        z, x = 1, x + 2
if prime [-1] > lim:
    prime.pop()
print(prime, sum(prime))
