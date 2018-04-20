# Barbara King fib.py

def fibonacci(N):
    fn_1 = 0
    fn_2 = 1
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        for i in range(1,N):
            fn = fn_1 + fn_2
            fn_1 = fn_2
            fn_2 = fn
    return fn


# print(fibonacci(5))