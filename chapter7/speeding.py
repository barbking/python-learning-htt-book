# Barbara King speeding.py

limit = float(input("Enter speed limit: "))
measured = float(input("Enter measured speed: "))

def check_speed(limit, measured):
    fine = 0
    if measured <= limit:
        return "Your speed is legal"
    elif measured > limit and measured <= 90:
        fine = 50 + 5 * (measured - limit)
        print("Your measured speed was over the limit, your fine in dollars is: ")
        return fine
    else:
        fine = (50 + 5 * (measured - limit)) + 200
        print("Your measured speed was over the limit, your fine in dollars is: ")
        return fine

print(check_speed(limit, measured))