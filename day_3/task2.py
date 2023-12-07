import time

# Variables
file = open("sample.txt", "r")
sum = 0
row = 0
result = []
engine_map = []
temp = []
symbols = '{}[]|;:<,>?"!@#$%^&*+\=-//'
sum_item = ""


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
                            if engine_map[column + nei_co_1][row + nei_co_2 - num] == "*":
                                print(temp)
                                temp = []
            except IndexError:
                pass
            temp = []

# Calculate final sum
#for item in range(0,len(result)):
 #   for num in range(0,len(result[item])):
  #      sum_item += result[item][num]
   # sum += int(sum_item)
    #sum_item = ""

end = time.time()

# Answer Prompt
#print("Answer is: {}".format(sum))
print("Working time is: {}".format(round(end-start, 5)))
