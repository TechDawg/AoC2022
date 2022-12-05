import string
import re

f = open("i5.txt", "r")
input = f.read()
f.close()

stacks = [[], [], [], [], [], [], [], [], []]

for line in reversed(input.splitlines()[:8]):
    count = -1
    for i in range(1, len(line), 4):
        count += 1
        if line[i] in set(string.ascii_uppercase):
            stacks[count].append(line[i])

for line in input.splitlines()[10:]:
    craneMove = int(re.search("(?<=move )(\d+)(?= from)", line).group(0))
    start = int((re.search("(?<=from )(\d+)(?= to)", line).group(0))) - 1
    end = int(re.search("(?<=to )(\d+)", line).group(0)) -1
    
    crane = stacks[start][-craneMove:]
    stacks[start] = stacks[start][:-craneMove]
#    PART ONE stacks[end].extend(reversed(crane))
    stacks[end].extend(crane)

solution = ""

for stack in stacks:
    solution += str(stack[-1:][0])
