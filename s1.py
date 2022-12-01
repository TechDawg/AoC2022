output = []

f = open("i1.txt", "r")
inputs = f.read()
f.close()

lists = inputs.split("\n\n")

for i in lists:
    calories = i.split("\n")
    print(calories)
    count = 0
    for ii in calories:
        try:
            ii = int(ii)
            count = count + ii
        except:
            print("end of list")
    output.append(count)
output.sort()

print("Part 1:" + str(output[-1]))
print("Part 2:" + str(output[-1] + output[-2] + output[-3]))
