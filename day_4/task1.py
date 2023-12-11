import time

file = open('sample.txt', 'r')
sum = 0
result = []
replace = {':':'|'}

start = time.time()
for line in file:
    for x,y in replace.items():
        line = line.replace(x,y)
        cards = line.split("|")



end = time.time()
