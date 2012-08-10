#200 375 425
a = 200
b = 375
c = 425

for x in range (1, 426):
    if c % x == 0 and b % x == 0 and a % x == 0:
        print (x)
