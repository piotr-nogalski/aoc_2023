import time

# Variables
file = open('data.txt', 'r')
sum = 0
result = []
replace = {':':'|',
           'Card ':'',
           '\n':''}
power = 0

# Algorithm

start = time.time()
# remove unneccesary elements from text
for line in file:
    for x,y in replace.items():
        line = line.replace(x,y)
        cards = line.split("|")
    #print(cards)

    cards[1] = cards[1].split(" ")
    cards[2] = cards[2].split(" ")
    #print(cards)
# Check for lucky numbers by indexing elemnts from deck1 in deck2
# Ommit value error by try/except
    for num in cards[1]:
        try:
           # print(num)
            if cards[2].index(num) and power == 0 and num != ' ':
                power = 1
            elif cards[2].index(num) and power >= 1 and num != ' ':
                power = power*2
            else:
                continue
        except ValueError:
            continue
    sum += power
    power = 0

end = time.time()

print("Answer is equal: {}".format(sum))
print("Execution time was: {} ".format(end - start))