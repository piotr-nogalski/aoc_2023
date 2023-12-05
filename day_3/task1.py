import time

file = open("sample.txt", "r")
sum = 0
engine_map = []

start = time.time()
for line in file:
    pass



end = time.time()

print("Answer is: {}".format(sum))
print("Working time is: {}".format(round(end-start, 5)))
