import time

# Variables
file = open("sample.txt", "r")
sum = 0
row = 0
result = []
engine_map = []
temp = []
symbols = '{}[]|;:<,>?"!@#$%^&*+\=-//'
check_gear = 0


# Algorithm

start = time.time()

# Convert data to two-dimensional list
for line in file:
    engine_map.append([])
    for value in line:
            engine_map[row].append(value)
    row+=1

# Search for legal values for digits
for column in range(0, len(engine_map)):
    for row in range(0, len(engine_map[column])):
        if engine_map[column][row].isnumeric():
            temp.append(engine_map[column][row])
        # Once the number is interuppted check if any number stored in temp[] has symbol neigbour
        elif not engine_map[column][row].isnumeric():
            # try except to ommit errors in cases with first and last row
            try:
                # Search for special symbol in rows calculated by
                # [column index +-1,0][row index +-1,0 - digits of number] to determie whether value is legal or not
                for nei_co_1 in [-1,0,1]:
                    for nei_co_2 in [-1,0,1]:
                        for num in range(1,len(temp)+1):
                            if engine_map[column + nei_co_1][row + nei_co_2 - num] == '*':
                                result.append([int("".join(temp)),str(column + nei_co_1) + str(row + nei_co_2 - num)])
                                temp = []
            except IndexError:
                pass
            temp = []

#Calculate final sum
print(result)
for items in range(0,len(result)):
    try:
        for awk in range(0,len(result)+1):
            if result[items][1] == result[items+awk][1]:
                print(result[items+awk][1], result[items+awk])
                check_gear +=1
        if check_gear == 2:
            sum += result[items][0]*result[items+awk][0]
    except IndexError:
        pass
end = time.time()

# Answer Prompt
print("Answer is: {}".format(sum))
print("Working time is: {}".format(round(end-start, 5)))
