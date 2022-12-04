scoreOne = 0
scoreTwo = 0

scoring = {
    "A X": 3, "A Y": 6, "A Z": 0,
    "B X": 0, "B Y": 3, "B Z": 6,
    "C X": 6, "C Y": 0, "C Z": 3,
}  

shapeValues = {
    "X": {"game_score": 0, "shape": {"A": "Z", "B": "X", "C": "Y"}},
    "Y": {"game_score": 3, "shape": {"A": "X", "B": "Y", "C": "Z"}},
    "Z": {"game_score": 6, "shape": {"A": "Y", "B": "Z", "C": "X"}},
}

f = open("i2.txt", "r")
inputs = f.read().splitlines()
f.close()

def getScore(shape):
    return list(shapeValues.keys()).index(shape) + 1

for round in inputs:
    left, right = round.split(" ")
    scoreOne += scoring[round] + getScore(right)
    gameScore = shapeValues[right]["game_score"]
    shape = shapeValues[right]["shape"][left]
    scoreTwo += gameScore + getScore(shape)
print("Part 1:", scoreOne, "\nPart 2:", scoreTwo)