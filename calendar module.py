# Calendar of a month
import calendar
print(calendar.month(2000,4))
print("X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X")
# Calender of a Year
# print first is model name and second is method name
import calendar
print(calendar.calendar(2017))

# Week day method
# Index of monday is zero
import calendar
print("\nweekday number : ")
print(calendar.weekday(2017,4,11))


# Leap year or not
import calendar
print("\nleap year = ")
print(calendar.isleap(2000))

# no. of leap years between two years [ 2000 2004 2008 201202016 ]
import calendar
print("\nno. of leap days/year : ")
print(calendar.leapdays(2000,2017))


# MONTH RANGE
# Returns two integers. The first one is the code of the weekday for the first day of the month
# month in year; the second one is the number of days in the month.
# Weekday codes are 0 (Monday) to 6 (Sunday); month numbers are 1 to 12.
print("\nrange of the month : ")
print(calendar.monthrange(2017,8))

# to set first week day
import calendar
print("\nweekday number {if weeek is starting from 6th day} : ")
calendar.setfirstweekday(6)
print(calendar.weekday(2017,4,11))
