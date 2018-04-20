# Barbara King
# patterns2.py

def triangle(N):
    results = ''
    spaces = 5
    for row in range(N):

        for col in range(row):
            print(' ', end='')

        for col in range(N-row):
            print('*', end='')

        print()

    return ' '  # returning ' ' so don't return None

def hollow_box(N):
    for row in range(N):
        print('*', end='')
    print()

    for row in range(1,N-1):
        print('*', end='')
        for col in range(N-2):
            print(' ', end='')
        print('*', end='')
        print()

    for row in range(N):
        print('*', end='')
    print()

    return ' '

def solid_diamond(N):
    lines = 2*N + 1

    for row in range(N,0,-1):
        for col in range(row):
            print(' ', end='')
        for col in range(2*N-(2*(row-1)+1)):
            print('*', end='')
        print()

    for row in range(2*N + 1):
        print('*', end='')
    print()

    for row in range(1,N+1):
        for col in range(row):
            print(' ', end='')
        for col in range(2*N-(2*(row-1)+1)):
            print('*', end='')
        print()

    return ' '

def hollow_diamond(N):

    for row in range((2*N+1)-(2*N)):
        for col in range(N):
            print(' ', end='')
    print('*', end='')
    print()

    for row in range(N):
        for col in range(N-(1*row)-1):
            print(' ', end='')
        print('*', end='')
        for col in range(2*row+1):
            print(' ', end='')
        print('*', end='')
        print()

    for row in range(1, N):
        for col in range(row):
            print(' ', end='')
        print('*', end='')
        for col in range((2*N-1)-2*row):
            print(' ', end='')
        print('*', end='')
        print()

    for row in range((2*N+1)-(2*N)):
        for col in range(N):
            print(' ', end='')
    print('*', end='')
    print()

    return ' '


def main():
    n = int(input("Enter an integer >= 0: "))
    print(triangle(n))
    print(hollow_box(n))
    print(solid_diamond(n))
    print(hollow_diamond(n))
main()
