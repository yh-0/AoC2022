from queue import LifoQueue
import re

input = open('data/input-5.txt', 'r')
lines = input.readlines()

crate_lines = []
crates_1 = []
crates_2 = []
moves = []
switch = False

for line in lines:
    if line == '\n':
        switch = True

    if line.strip().startswith('1'):
        cnt = len(line.removesuffix('\n').replace(' ', ''))
    
    if not switch:
        crate_lines.append(re.findall("\[.\]", line.replace("    ", "[.]")))

    if switch:
        moves.append(line.removesuffix('\n').removeprefix('move '))

for i in range(cnt):
    crates_1.append(LifoQueue())
    crates_2.append(LifoQueue())

it = 0
for cl in crate_lines[::-1]:
    for crate in cl:
        if it == cnt:
            it = 0
        if crate != "[.]":
            crates_1[it].put(crate)
            crates_2[it].put(crate)
        it += 1

del moves[0]
moves = [m.replace(" from ", ',').replace(" to ", ',').split(',') for m in moves]

for m in moves:
    for _ in range(int(m[0])):
        item = crates_1[int(m[1]) - 1].get()
        crates_1[int(m[2]) - 1].put(item)

for m in moves:
    tmp = []
    for _ in range(int(m[0])):
        item = crates_2[int(m[1]) - 1].get()
        tmp.append(item)

    for t in tmp[::-1]:
        crates_2[int(m[2]) - 1].put(t)

res_1 = ''
res_2 = ''

for i in range(cnt):
    res_1 += crates_1[i].get()[1]
    res_2 += crates_2[i].get()[1]

print(res_1)
print(res_2)