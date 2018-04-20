# Barbara King
# andornot.py extra credit

print("|", "A".center(5), "|", "B".center(5),
      "|", "A and B".center(5), "|", "A or B".center(5),
      "|", "not A".center(5),"|", "not B".center(5), "|")
print("|","-"*48,"|")

for A in [True, False]:
    for B in [True, False]:
        print("|", str(A).ljust(5), "|", str(B).ljust(5),
              "|", str(A and B).ljust(7), "|", str(A or B).ljust(6),
              "|",str(not A).ljust(5),"|", str(not B).ljust(5), "|")