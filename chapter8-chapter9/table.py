# Barbara King
# table.py

print("|  * ", end='')

for row in range(10):
    print("| %02d " % row, end='')
print("|")
print("-" * 56)

for row in range(10):
    print("| %02d " % row, end='')
    for col in range(10):
        cell_value = row*col
        print("| %02d " % cell_value, end='')
    print("|")
    print()


