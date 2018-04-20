# Barbara King
# HW 8-1: ascend3.py
#
#   Starting code for program that prints out all 3 digit ints
#		abc where a < b < c,  '0123456789'
#
for hundreds in range (0,10):
    for tens in range(0,10):
        for ones in range(0,10):
            if hundreds < tens and tens < ones:
                print(hundreds,tens, ones, sep='')
