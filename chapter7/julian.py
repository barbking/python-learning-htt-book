# Barbara King
# julian.py with leap year

def julian(day, month, year):
    daynum = 31 * (month - 1) + day
    leapyr = isLeap(year)
    print("daynum:", daynum)
    if month > 2:
        daynum = daynum - (4 * month + 23) // 10
        print("daynum for month >2", daynum)
        if leapyr:
            daynum = daynum + 1
            print("daynum for month >2 and leapyr", daynum)
    return daynum

def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def main():
    day = int(input("Enter day in interger format: "))
    month = int(input("Enter month in integer format: "))
    year = int(input("Enter year in format XXXX: "))
    results = julian(day, month, year)
    print("The Julian date for day", day, "month", month, "and year", year, "is:", results)

main()