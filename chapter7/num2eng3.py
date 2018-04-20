# Barbara King
# num2eng3.py

def tens_to_english(N):
    if N < 2 or N >= 10:
        return "Invalid"
    else:
        N = 10 * N
        if N == 20:
            return "twenty"
        elif N == 30:
            return "thirty"
        elif N == 40:
            return "fourty"
        elif N == 50:
            return "fifty"
        elif N == 60:
            return "sixty"
        elif N == 70:
            return "seventy"
        elif N == 80:
            return "eighty"
        elif N == 90:
            return "ninety"

def main():
    intnum = int(input("Enter an integer >= 2 but < 10: "))
    print(tens_to_english(intnum))

main()