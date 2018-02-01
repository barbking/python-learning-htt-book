''' 2.13 Python expression exercises
5 ** 2  = 25
9 * 5 = 45
15 / 12 = 1.25
12 / 15 = 0.8
15 // 12 = 1
12 // 15 = 0
5 % 2 = 1
9 % 5 = 4
15 % 12 = 3
12 % 15 = 12
6 % 6 = 0
0 % 7 = 0 '''


''' Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours),
and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the 
clock when the alarm goes off. '''

hours = input("Enter time in hours")
alarm = input("Enter number of hours to wait")
int_hours = int(hours)
print(int_hours)
int_alarm = int(alarm)
print(int_alarm)
alarm_hours = (int_hours + int_alarm) % 24
print(alarm_hours)


'''It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday.
If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would
return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and
the length of your stay, and it will tell you the number of day of the week you will return on.'''

day = input("Enter starting day number")
stay = input("Enter length of your stay in number of nights")
day_int = int(day)
stay_int = int(stay)
return_day = (day_int + stay_int) % 7
print(return_day)
