for c in range (1, 1000):
    for a in range (1, 1000):
        for b in range (1, 1000):
            if c*c == a*a + b*b:
                print (a, b, c)
                if a+b+c == 1000:
                    print('The answer is ', a*b*c)                                            
