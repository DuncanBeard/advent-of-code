num_twos = 0
num_threes = 0

with open('input.txt') as f:
    for line in f:
        dupes = {}
        for c in line:
            if c in dupes.keys():
                dupes[c] = dupes[c] + 1
            else:
                dupes[c] = 1

        for key in dupes.keys():
            if dupes[key] == 2:
                num_twos+=1
                break
        for key in dupes.keys():
            if dupes[key] == 3:
                num_threes+=1
                break
print (num_twos * num_threes)