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

max_kcal = max(elves)
max_elf = elves.index(max_kcal) + 1

print(f'Elf {max_elf} has {max_kcal} kcal.')