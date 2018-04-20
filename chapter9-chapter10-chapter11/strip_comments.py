# Barbara King
# strip_comments.py:
#
#   Starting code H7-4
#

# read string fname from user
fname = input("Enter file name (xxxx.py): ")

# open Python source file named fname.py for reading
f = open(fname, 'r')

# create new file 'strip_' + fname.py for writing
new_file = 'strip_' + fname
w = open(new_file,'w')

# for each line in fname file:
data = f.read().split('\n')

# read line remove comments: starting at # and going to end of line

for aline in data:
    # trying to check if # in quotes or real comment
    if '#' in aline and aline.count("'") == 2 or aline.count("'") == 2:
        hash_index = aline.rfind("#")
        compare_index = max(aline.rfind('"'), aline.rfind("'"))
        if hash_index > compare_index:
            aline_index = data.index(aline)
            new_line = aline[:hash_index]
            data[aline_index] = new_line

    if "#" in aline and "'" not in aline and '"' not in aline:
        aline_index = data.index(aline)
        hash_index = aline.find('#')
        new_line = aline[:hash_index]
        data[aline_index] = new_line

# write modified line to output file
for aline in data:
    w.write(aline + '\n')

# close both files
f.close()
w.close()