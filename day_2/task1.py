import time

# Variables
File = open("data.txt", "r")
sum = 0
positive = 0
game = []
result = []
legal_values = { 'r':12,
                 'g':13,
                 'b':14}
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

# Check for every game if it fits legal requierements
# Try/except helps in cases when ball number contains one or two digits ex:. 1b, 11b
# Iterate through legal values dictionary reduce if/else statements
# game[value][2] represents color of two digit numbered ball ex:. 11b
# game[value][1] represents color of one digit numbered ball ex:. 2g
    for value in range(1,len(game)):
        # Tries for two digit balls number
        try:
            for color, legal_value in legal_values.items():
                if game[value][2] == color:
                    if int(game[value][0:2]) <= legal_value:
                        positive+=1
                    else:
                        continue
            if positive == len(game)-1:
                result.append(int(game[0]))
        # When two digit balls number fails checks for one digit number of balls
        except IndexError:
            for color, legal_value in legal_values.items():
                if game[value][1] == color:
                    if int(game[value][0]) <= legal_value:
                        positive+=1
                    else:
                        continue
            # Checks if all configurations were possible
            if positive == len(game)-1:
                result.append(int(game[0]))
    # Resets configuration check
    positive = 0

# Add final results for answer
for value in result:
    sum += value
end = time.time()

# Prompt with result
print(result)
print("Answer is equal: {}".format(sum))
print("Execution time was: {} ".format(end - start))
