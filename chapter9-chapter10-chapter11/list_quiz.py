# Barbara King
# list_quiz.py:
#
#   Starting code H7-5
#

# Give short one-question quiz on HTT10 (Lists) to user
print("List Quiz")

quest1 = input("How do you determine the length of alist?\n(A) alist.length(),(B) len(alist),"
               "(C) None of the above.\nEnter A, B or C: ").upper()

if quest1 == "B":
    print("Correct! The function len() returns length of a list.")
else:
    print("Incorrect. The function len() returns length of a list.")

print()

quest2 = input("alist = [3, 67, 'cat', [56, 57, 'dog'], [ ], 3.14, False]\n"
          "What will print(alist[4:]) output be?\n"
          "(A) [ [ ], 3.14, False]\n(B) [ [ ], 3.14]\n(C) [ [56, 57, 'dog'], [ ], 3.14, False]\n"
               "Enter A, B or C:").upper()

print(quest2)
if quest2 == "A":
    print("Correct! Slice[4:] takes the 4th element up to the end of the list")
else:
    print("Incorrect. Slice[4:] takes the 4th element up to the end of the list")
