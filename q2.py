import re
import string
import sys


class Date:
	def __init__(self, d, m, y):
		self.d = d
		self.m = m
		self.y = y


def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')


def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    total_days = 0
    while not isDateEqual(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        total_days += 1
    return total_days


def isDateEqual(year1, month1, day1, year2, month2, day2):
    if year1 == year2 and month1 == month2 and day1 == day2:
        return True
    else:
        return False


def nextDay(year, month, day):
    if month < 12 and day == daysInMonth(year, month):
        return year, month + 1, 1
    elif month == 12 and day == daysInMonth(year, month):
        return year + 1, 1, 1
    else:
        return year, month, day + 1


def daysInMonth(year, month):
    daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        daysInEachMonth[1] = 29
    return daysInEachMonth[month - 1]


def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

inputDateFormat = sys.argv
DateFormat = str(inputDateFormat[1]).lower()
print(DateFormat)

DateFormat = re.split('/| |-|\.', DateFormat)
print(DateFormat[0])
f = open("date_calculator.txt", 'r')
date = f.read()
date = date.split('\n')
# print(date[0])
date1 = date[0]
date2 = date[1]
date1 = date1.split(':')[1]
date2 = date2.split(':')[1]
date1 = date1[1:]
date2 = date2[1:]
# print(date1)
# print(date2)
date1 = re.split('/| |-|\.', date1)
date2 = re.split('/| |-|\.', date2)

if DateFormat[0] == 'mm':
    t1 = date1[0]
    t2 = date2[0]

    date1[0] = date1[1]
    date2[0] = date2[1]

    date1[1] = t1
    date2[1] = t2

date1[0] = date1[0].rstrip('th')
date2[0] = date2[0].rstrip('th')

try:
    val = int(date1[1])
except ValueError:
    date1[1] = month_string_to_number(date1[1])
try:
    val = int(date2[1])
except ValueError:
    date2[1] = month_string_to_number(date2[1])
  
dt1 = Date(int(date1[0]), int(date1[1]), int(date1[2]))
dt2 = Date(int(date2[0]), int(date2[1]), int(date2[2]))
if date1[2] > date2[2]:
    t = dt1
    dt1 = dt2
    dt2 = t
elif date1[2] == date2[2]:
    if date1[1] > date2[1]:
        t = dt1
        dt1 = dt2
        dt2 = t
    elif date1[1] == date2[1]:
        if date1[0] > date1[0]:
            t = dt1
            dt1 = dt2
            dt2 = dt1
x = daysBetweenDates(dt1.y, dt1.m, dt1.d, dt2.y, dt2.m, dt2.d)
if x < 0:
    x = -1 * x


print(x, "Day(s)")
of = open("output.txt", "w")
of.write("Date Difference: "+str(x) + " Day(s)")
of.close()
