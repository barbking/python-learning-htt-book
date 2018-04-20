# Barbara King
# num2eng4.py

def digit_to_english(N):
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

def teens_to_english(N):
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

def tens_to_english(N):
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

def num_to_english(N):

    first_digit = 0
    second_digt = 0
    eng_word1 = ''
    eng_word2 = ''

    if N < 0 or N > 100:
        return "Invalid"
    else:
        if N >= 0 and N <= 10:
            return digit_to_english(N)
        elif N > 10 and N < 20:
            return teens_to_english(N)
        else:
            if N >= 20 and N < 100:
                first_digit = N // 10
                second_digit = N % 10
                eng_word1 = tens_to_english(first_digit)
                if second_digit != 0:
                    eng_word2 = digit_to_english(second_digit)
                    result = eng_word1 + '-' + eng_word2
                    return result
                else:
                    return tens_to_english(first_digit)
            else:
                return "one-hundred"

def main():
    intnum = int(input("Enter a number equal to or between 0 and 100: "))
    print(num_to_english(intnum))


if __name__ == "__main__":
    main()