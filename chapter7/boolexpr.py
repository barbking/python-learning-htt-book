# Barbara King
# boolexpr.py

# function before extra credit attempt
# def is_in_semester(month, day):
#
#     if month > 1 and month < 5:
#         return True
#     elif month == 1 and day > 29:
#         return True
#     elif month == 5 and day < 12:
#         return True
#     else:
#         return False

def is_in_semester(month, day):

    if month > 1 and month < 5 or month == 1 and day > 29 or month == 5 and day < 12:
        return True

    return False

def main():
    month = int(input("Enter a month: "))
    day = int(input("Enter a day: "))
    print(is_in_semester(month, day))

main()

