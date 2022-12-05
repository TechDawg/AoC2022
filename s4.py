f = open("i4.txt", "r")
input = f.read().splitlines()
f.close()

matchingPairs = list()
for item in input:
    pair = item.split(",")
    for i in range(len(pair)):
        split = pair[i].split("-")
        pair[i] = (int(split[0]), int(split[1]))
    matchingPairs.append(pair)
    
partOne = 0

for pair in matchingPairs:
    if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1] 
    or pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]):
        partOne+=1

partTwo = 0
for pair in matchingPairs:
    if pair[0][0] >= pair[1][0]:
        if pair[0][0] <= pair[1][1]:
            partTwo+=1
    else:
        if pair[1][0] <= pair[0][1]:
            partTwo+=1

print("Part 1: " + str(partOne) + "\nPart 2: " + str(partTwo))