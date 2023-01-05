def part_1(h1s, h1e, h2s, h2e):
    if int(h1s) <= int(h2s) and int(h2e) <= int(h1e):
        return 1
    elif int(h2s) <= int(h1s) and int(h1e) <= int(h2e):
        return 1
    return 0

def part_2(h1s, h1e, h2s, h2e):
    if int(h2s) <= int(h1s) and int(h1s) <= int(h2e):
        return 1
    elif int(h2s) <= int(h1e) and int(h1e) <= int(h2e):
        return 1
    elif int(h1s) <= int(h2s) and int(h2s) <= int(h1e):
        return 1
    elif int(h1s) <= int(h2e) and int(h2e) <= int(h1e):
        return 1
    return 0

input = open('data/input-4.txt', 'r')
lines = input.readlines()

res_1 = 0
res_2 = 0

for line in lines:
    h1, h2 = line.split(',')
    h1s, h1e = h1.split('-')
    h2s, h2e = h2.split('-')
    res_1 += part_1(h1s, h1e, h2s, h2e)
    res_2 += part_2(h1s, h1e, h2s, h2e)

print(res_1)
print(res_2)