# Barbara King
# http_ex12.py

def remove_all(sub, s):
    if sub not in s:
        return "Substring not found"
    else:
        index = s.find(sub)  # will be -1 if not found
        while index >= 0:
            results = ''
            sub_len = len(sub)
            results = results + s[:index] + s[index + sub_len:]
            s = results
            index = s.find(sub)
    return "Results with all occurrances of '{}' removed: {}".format(sub, results)

    # easy way solution
    # results = s.split(sub)
    # results = "".join(results)
    # print(results)

def main():
    theStr = input("Enter a string: ")
    substr = input("Enter a substring to remove: ")
    print(remove_all(substr, theStr))

main()