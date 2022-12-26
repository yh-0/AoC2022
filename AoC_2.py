input = open('data/input-2.txt', 'r')
lines = input.readlines()

sign_dict = {'A' : 1, 'B' : 2, 'C' : 3, 'X' : 1, 'Y' : 2, 'Z' : 3}
sign_dict_2 = {'X' : 0, 'Y' : 3, 'Z' : 6}

def rps(enemy, ally):
    if enemy == ally: return 3
    if enemy == 1 and ally == 3: return 0
    if enemy == 3 and ally == 1: return 6
    if enemy > ally: return 0
    if enemy < ally: return 6
    return -1

def rps_2(enemy, sign):
    if sign == 3: return enemy
    if sign == 0 and enemy == 1: return 3
    if sign == 6 and enemy == 3: return 1
    if sign == 0: return enemy - 1
    if sign == 6: return enemy + 1
    return -1

points = 0
points_2 = 0

for line in lines:
    sign_1, sign_2 = line.removesuffix('\n').split(' ')
    
    points += rps(sign_dict[sign_1], sign_dict[sign_2])
    points += sign_dict[sign_2]

    points_2 += rps_2(sign_dict[sign_1], sign_dict_2[sign_2])
    points_2 += sign_dict_2[sign_2]

print(points)
print(points_2)