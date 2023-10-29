import random

# Taking a 4 sided tetrahedron as a example in throwing

mapBias = [('front',40), ('back',30), ('top',20), ('bottom',10)]

def checkIntegrity(map):
    totalPercentage = sum(x[1] for x in map)
    if totalPercentage == 100:
        return True
    else:
        return False

# Placing all the random outcomes from 1 to 100 in the curresponding probalities of the events it will happen.

if not checkIntegrity(mapBias):
    print("not a good input\n")
noEvents = 100
resultMap = {}
for i in mapBias:
    resultMap[i[0]] = 0
for event in range(noEvents):
    bin = 0
    randomOutcome = random.randint(1,100)
    for outcome, percentage in mapBias:
        bin += percentage
        if randomOutcome <= bin:
            resultMap[outcome] += 1
            # print(outcome)
            break

for key, value in resultMap.items():
    print(f"{key} took place in {value} of events")