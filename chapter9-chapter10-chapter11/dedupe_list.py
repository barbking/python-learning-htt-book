# Barbara King
# dedupe_list.py:
#
#   Starting code H7-3
#

mylist = eval(input("Enter a list in proper Python format:"))
# mylist = [[1,2], 3, 3, [1,3]]
# mylist = ["a", "a", "b", "b", "c", "c"]
results = []
for item in mylist:
    if item not in results:
        results.append(item)
print("mylist:", mylist)
print("duplicateds removed", results)

