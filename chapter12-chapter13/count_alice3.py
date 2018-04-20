# Barbara King
# H8-2: count_alice3.py
#
#   Starting code H8-2
#

# start with your H8-2 count_alice2 and continue...

import string

FILENAME = 'alice.txt'

fvar = open (FILENAME, 'r') # open file for reading

allwords = [] # accumulate the words in this list

# print(string.punctuation)

for aline in fvar:

    line = aline.lower()

    punct = '!",?:;>=>{}[]()_.1234567890'
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

# trim leading ' and trailing ', except for 'tis
for ind in range(len(allwords)):
    if allwords[ind][0] == "'":
        allwords[ind] = allwords[ind][1:]
    if allwords[ind][-1] == "'":
        allwords[ind] = allwords[ind][:-1]

print(len(allwords))
allwords.sort()

counts = {}
for word in allwords:
    if word in counts.keys():
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
    # counts[word] = counts.get(word,0) + 1
    # print(word)
# print(allwords)

# for k, v in sorted(counts.key()):
#     print(k,v)


import operator
sorted(counts.iteritems(), key=operator.itemgetter(1))
print(counts)
fvar.close()

