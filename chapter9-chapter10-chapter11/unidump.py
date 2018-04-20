# Barbara King
# unidump.py:
#
#   Starting code H7-2
#
import time
N = int(input("Enter integer N: "))

line_count = 32
# print('{:04}: '.format(line_count), end='')
for n in range(32,N):
    if n % 32 == 0:
        print() # new line
        print('{:04}: '.format(line_count), end='')
        line_count += 32
    time.sleep(0.01)
    char = chr(n)
    print("%s" % char, end='') # print


