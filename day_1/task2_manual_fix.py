import time

# Variables
File = open("data.txt", "r")
sum = 0
start = time.time()
# Prefixes and postfixes provide fix for situation when two numbers share one letter ex:. eightwo
written_nums = {"zero":"z0o",
                "one":"o1e",
                "two":"t2o",
                "three":"t3e",
                "four":"f4r",
                "five":"f5r",
                "six":"s6x",
                "seven":"s7n",
                "eight":"e8t",
                "nine":"n9e"}
# Read file with data line by line and filter out digits
for line in File:
    num = []
# Iterate through dictionary written_nums to change every written number to its digital form
    for s, d in written_nums.items():
        if line.find(s) >= 0:
            line = line.replace(s, str(d))
    for value in line:
        if value.isdigit():
            num.append(int(value))
    # Format digits to coordinates, by instruction coordinates are first and last digit in each line
    # try except for blank lines (blank "num" variable)
    try:
        coordinate = str(num[0])
        coordinate += str(num[-1])
    except IndexError:
        coordinate = 0
    sum += int(coordinate)

end = time.time()
print(sum)
print("Execution time was: {} ".format(end - start))


# Tests executed on sample.txt file

"""sample = open("sample.txt", "r")
test_array = []
bruv_sum = 0
for line in sample:
    test_array = []
    print(line)
    for s,d in written_nums.items():
        if line.find(s) >= 0:
            line = line.replace(s,str(d))
    print(line)
    for value in line:
        if value.isdigit():
            test_array.append(int(value))

    bruv = str(test_array[0])
    bruv += str(test_array[-1])
    bruv_sum += int(bruv)
    print(test_array)

print(bruv_sum)"""

