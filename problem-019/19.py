#!/usr/bin/env python3
#Project Euler - Problem 19 - http://projecteuler.net
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def nextMonth():
    global month
    if month == 12:
        month = 1
        nextYear()
    else:
        month += 1


def nextYear():
    global year
    year += 1
    isLeap()


def isLeap():
    global leap
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False


epoch = 2 #day of the week starting from; 0-6
year = 1901 #year starting from 
month = 1
leap = False
daysInMonth = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
daysInLeap = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
firstSunday = 0

while year != 2001:
    if week[epoch % 7] == 'Sunday':
        firstSunday += 1
    if leap:
        epoch+= daysInLeap[month]
    else:
        epoch+= daysInMonth[month]
    nextMonth()

print(firstSunday)
