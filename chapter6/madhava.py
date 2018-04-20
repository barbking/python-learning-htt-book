# Barbara King extra credit madhava.py

import math

def madhavaPi(N):
    sum_term = 1
    sign = -1
    x = 3
    for i in range(1, N):
        term = 1 / ((x) * (3**i)) * sign
        sum_term = sum_term + term
        sign = -1 * sign
        x = x + 2
    results = math.sqrt(12) * sum_term
    return(results)

numTerms = int(input("Enter number of terms to estimate pi: "))
results = madhavaPi(numTerms)
print("Madhava Pi estimate:", results)
print("Actual Pi value:", math.pi)
print("Difference:", abs(math.pi - results))


