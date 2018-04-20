# Barbara King
# num2eng1.py

def digit_to_english(N):

    if N < 0 or N > 10:
        return "Invalid"
    else:
        if N == 0:
            return "zero"
        elif N == 1:
            return "one"
        elif N == 2:
            return "two"
        elif N == 3:
            return "three"
        elif N == 4:
            return "four"
        elif N == 5:
            return "five"
        elif N == 6:
            return "six"
        elif N == 7:
            return "seven"
        elif N == 8:
            return "eight"
        elif N == 9:
            return "nine"
        else:
            return "ten"


def main():
    num = int(input("Enter an integer between 0 and 10: "))
    print(digit_to_english(num))

main()