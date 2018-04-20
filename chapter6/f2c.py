# Barbara King f2c.py

def f_to_c(fahr):
    cels = (fahr - 32)*5/9
    return round(cels, 2)

def main():
    f = int(input("Enter degrees in Fahrenheit: "))
    results = f_to_c(f)
    print(f, "degrees F is equivalent to", results, "degrees C")

if __name__ == "__main__":
    main()
