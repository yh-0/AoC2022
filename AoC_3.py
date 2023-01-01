def match_number(char):
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38

def find_common_char(str_1, str_2, br):
    res = []
    for char in str_1:
            common = str_2.find(char)
            if common >= 0:
                if br:
                    return char
                res.append(char)
    return res

def part_1():
    input = open('data/input-3.txt', 'r')
    lines = input.readlines()

    res = 0

    for line in lines:
        h1 = line[:len(line)//2]
        h2 = line[len(line)//2:]
        res += match_number(find_common_char(h1, h2, True))

    print(res)

def part_2():
    data = [i.strip('\n') for i in open('data/input-3.txt')]
    new_data = [', '.join(data[i:i+3]) for i in range(0, len(data), 3)]

    f = open('data/new-input-3.txt', 'w')
    for i in new_data:
        f.write("{}\n".format(i))
    f.close()

    input = open('data/new-input-3.txt', 'r')
    lines = input.readlines()

    res = 0

    for line in lines:
        l = line.split(", ")
        maybe_common = find_common_char(l[0], l[1], False)
        res += match_number(find_common_char(maybe_common, l[2], True))
        
    print(res)

part_1()
part_2()