def prime():
    n = 4
    p = [2, 3]
    if [n%x for x in p] != 0:
        p.append(n)
        n += 1
    else:
        n += 1
    print (p)
