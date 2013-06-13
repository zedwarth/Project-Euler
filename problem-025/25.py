#!/usr/bin/env python3
# Project Euler - Problem 25 - http://projecteuler.net

class Fib:
    '''Iterator that will yield the entire Fibonacci series;
          if you'd only give it the chance'''

    def __init__(self):
        pass

    def __iter__(self):
        self.a = 1
        self.b = 1
        self.count = 1

    def __next__(self):
        fib = self.a
        count = self.count
        self.a, self.b = self.b, self.a + self.b

