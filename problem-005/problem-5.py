#Progject Euler - Problem 5
#Zedwarth
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n=2520
w=0
while w == 0:
    if n % 20 == 0:
        if n % 9 == 0:
            if n % 7 == 0:
                if n % 8 == 0:
                    if n % 11 == 0:
                        if n % 13 == 0:
                            if n % 16 == 0:
                                if n % 17 == 0:
                                    if n % 19 == 0:
                                        print 'The answer is', n
                                        w = 1
                                    else:
                                        n += 20
                                else:
                                    n += 20
                            else:
                                n += 20
                        else:
                            n += 20
                    else:
                        n += 20
                else:
                    n += 20
            else:
                n += 20
        else:
            n += 20
    else:
        n += 20
