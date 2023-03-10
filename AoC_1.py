import sys

input = open('data/input-1.txt', 'r')
lines = input.readlines()

count = 0

for line in lines:
    if line == '\n':
        count += 1

if count != 0:
    count += 1
    current = 0
else:
    sys.exit('Empty file...')
    
elves = [0] * count

for line in lines:
    if line != '\n':
        elves[current] += int(line)
    else:
        current += 1

print(f'Elf {elves.index(max(elves)) + 1} has {max(elves)} kcal.')

elves.sort(reverse=True)

print(f'3 elves with most kcal combined have {elves[0] + elves[1] + elves[2]} kcal.')