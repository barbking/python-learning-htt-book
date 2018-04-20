# Barbara King
# leap.py

def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def main():
    intyear = int(input("Enter year to determine if leap year: "))
    print(isLeap(intyear))

main()