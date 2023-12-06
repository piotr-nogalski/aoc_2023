import time

# Variable
file = open("sample.txt", "r")
sum = 0
row = 0
result = []
engine_map = []


# Algorithm
start = time.time()

for line in file:
    engine_map.append([])
    for value in line:
        if value == '\n':
            continue
        else:
            engine_map[row].append(value)
    row+=1
for column in range(0, len(engine_map)):
    for row in range(0, len(engine_map[column])):
        if engine_map[column][row].isdigit():
            temp = []



end = time.time()

# Answer Prompt
print(engine_map)
print(result)

print("Answer is: {}".format(sum))
print("Working time is: {}".format(round(end-start, 5)))
