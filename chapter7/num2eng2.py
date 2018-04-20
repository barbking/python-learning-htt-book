# Barbara King
# num2eng2.py

def teens_to_english(N):

    if N < 10 or N >= 20:
        return "Invalid"
    else:
        if N == 10:
            return "ten"
        elif N == 11:
            return "eleven"
        elif N == 12:
            return "twelve"
        elif N == 13:
            return "thirteen"
        elif N == 14:
            return "fourteen"
        elif N == 15:
            return "fifteen"
        elif N == 16:
            return "sixteen"
        elif N == 17:
            return "seventeen"
        elif N == 18:
            return "eighteen"
        else:
            return "nineteen"

def main():
    intnum = int(input("Enter an integer >= 10 but < 20: "))
    print(teens_to_english(intnum))

main()