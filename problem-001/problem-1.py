#Problem-1
#Project Euler
#zedwarth
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#
x = 3  #x will contain the number I'm counting; starting at 3 since three is the lowest answer
answer = 0 #answer contains the sum of all vaild numbers

while x < 1000: #loop will run as until it's counted to 1000
    if x%3 == 0: #sees if the current number is divisable by 3
       answer += x #adds the current number to the sum if it's divisable by 3
    elif x % 5 == 0: #is x divisable by 5? will only run if x is not divsable by 3
        answer += x #adds the current number to the sum if it's divisable by 5
    x+=1 #incresses the vaule of x by one so the next int can be anyalized
print (answer) #prints the sum of all vailid numbers after the loop has reached 1000
