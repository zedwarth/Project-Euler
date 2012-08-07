#!/usr/bin/python
#
# Project Euler (projecteuler.net) - Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

n = 600851475143

def getnextprime(primes):
      a = primes[-1] + 1
        c = 0
          while 1:
                  d = primes[c]
                      (q, r) = (a // d, a % d)
                          if r:
                                    if d <= q :
                                                c += 1 
                                                      else:
                                                                  primes.append(a)
                                                                          break
                                                                          else:
                                                                                    a += 1

                                                                                    primes = [2]
                                                                                    pfactors = []
                                                                                    d = 0
                                                                                    while n > 0 and primes[-1] <= n:
                                                                                          try:
                                                                                                  if n % primes[d] == 0:
                                                                                                            n = n // primes[d]
                                                                                                                  pfactors.append( primes[d] )
                                                                                                                      else:
                                                                                                                                d += 1
                                                                                                                                  except IndexError:
                                                                                                                                          getnextprime(primes)

                                                                                                                                          print max(pfactors)
