import os

with open("merge-sort.py", "r") as input:
    with open("temp.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if line starts with substring 'time' then don't write it in temp file
            if not line.strip("\n").startswith('time'):
                output.write(line)

# replace file with original name
os.replace('merge-sort.py','temp.txt')