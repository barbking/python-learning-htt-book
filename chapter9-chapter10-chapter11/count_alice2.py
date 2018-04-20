# Barbara King
# count_alice2.py:
#
#   Starting code H7-1
#

# start with your Lab 7 count_alice and continue...
import string
FILENAME = 'alice.txt'

fvar = open (FILENAME, 'r') # open file for reading

allwords = [] # accumulate the words in this list

# print(string.punctuation)

for aline in fvar:

    line = aline.lower()

    punct = '!",?:;>=>{}[]()_.'
    for p in punct:
        line = line.replace(p,'')
    line = line.replace('--', ' ')

    words = line.split() # splits the line on whitespace (blanks, '\n', '\t')

    allwords.extend(words) # this does...

allwords.sort()

results = []
for word in allwords:
    if word != "'":
        results.append(word)
allwords = results

# time leading ' and trailing ', except for 'tis
for ind in range(len(allwords)):
    if allwords[ind][0] == "'":
        allwords[ind] = allwords[ind][1:]
    if allwords[ind][-1] == "'":
        allwords[ind] = allwords[ind][:-1]

print(len(allwords))
allwords.sort()

for word in allwords:
    print(word)
# print(allwords)


fvar.close()


