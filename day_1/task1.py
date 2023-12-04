import time

# Variables
File = open("data.txt", "r")
sum = 0
start = time.time()
# Read file with data line by line and filter out digits
for line in File:
    num = ""
    for value in line:
        if value.isdigit():
            num+=value
# Format digits to coordinates, by instruction coordinates are first and last digit in each line
# try except for blank lines(blank "num" variable
    try:
        coordinate = num[0]
        coordinate += num[-1]
    except IndexError:
        coordinate = 0
    sum += int(coordinate)

end = time.time()
print(sum)
print("Execution time was: {} ".format(end - start))
