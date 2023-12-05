import time

# Variables
File = open("data.txt", "r")
sum = 0
ans = 1
game = []
result = []
max_values = {   'r':1,
                 'g':1,
                 'b':1}
change = { ':':';',
           ';':',',
           'Game ':"",
           " red":"r",
           " blue":"b",
           " green":"g",
           "\n":"",
           " ":""}

# Algorithm
start = time.time()
# Modife data for futrhter operations, change values listed in change dictionary
for line in File:
    for x,y in change.items():
        line=line.replace(x,y)
    game = line.split(",")

# Check for every game for its maximu number of each ball color
# Try/except helps in cases when ball number contains one or two digits ex:. 1b, 11b
# Iterate through legal values dictionary reduce if/else statements
# game[value][2] represents color of two digit numbered ball ex:. 11b
# game[value][1] represents color of one digit numbered ball ex:. 2g
    for value in range(1,len(game)):
        # Tries for two digit balls number
        try:
            for color, max_value in max_values.items():
                if game[value][2] == color:
                    if int(game[value][0:2]) >= max_value:
                        max_values[color] = int(game[value][0:2])
                    else:
                        continue

        # When two digit balls number fails checks for one digit number of balls
        except IndexError:
            for color, max_value in max_values.items():
                if game[value][1] == color:
                    if int(game[value][0]) >= max_value:
                        max_values[color] = int(game[value][0])
                    else:
                        continue
    # Multiplies max color numbers for power of set
    for color, max_value in max_values.items():
     ans *= max_value

    result.append(ans)
    for color in max_values:
        max_values[color] = 1
    ans = 1

# Add final results for answer

for value in result:
    sum += value
end = time.time()

# Prompt with result
print(result)
print("Answer is equal: {}".format(sum))
print("Execution time was: {} ".format(end - start))
