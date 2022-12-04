f = open("i3.txt", "r")
input = f.read().split("\n")
f.close()

itemIdentifiers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", 
"C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
"R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

totalOne = 0
totalTwo = 0

for rucksack in input:
    for c in rucksack[:int(len(rucksack)/2)]:
        if c in rucksack[int(len(rucksack)/2):]:
            totalOne += (itemIdentifiers.index(c)+1)
            break
        
for count in range(100):
    group = [input.pop(0), input.pop(0), input.pop(0)]
    for c in group[0]:
        if c in group[1] and c in group[2]:
            totalTwo += (itemIdentifiers.index(c)+1)
            break

print("Part 1: " + str(totalOne) + "\nPart 2: " + str(totalTwo))
