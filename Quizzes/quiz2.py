# COMP9021 20T3 - Rachid Hamadi
# Quiz 2 *** Due Friday Week 4 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys
import time
on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()

time.sleep(0.001)
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE

code2='0' * nb_of_leading_zeroes + f'{int(code):o}' #user input-base 8-string 
code8=[] #reversed list of number digits (the directions of route)
for i in range(len(code2)-1,-1,-1):
    code8.append(int(code2[i])) 
#print(code8)

followed_route={1:[0,0]}

def move(x):
    max_key=max(followed_route.keys())
    max_key_position = followed_route[max_key].copy()
    #print(max_key,max_key_position,x)
    if x==0:
        max_key_position[1] += 1
    elif x==1:
        max_key_position[0] += 1
        max_key_position[1] += 1
    elif x==2:
        max_key_position[0] += 1
    elif x==3:
        max_key_position[0] += 1
        max_key_position[1] -= 1
    elif x==4:
        max_key_position[1] -= 1
    elif x==5:
        max_key_position[0] -= 1
        max_key_position[1] -= 1
    elif x==6:
        max_key_position[0] -= 1
    elif x==7:
        max_key_position[0] -= 1
        max_key_position[1] += 1
    #print(max_key_position)
    followed_route[max_key+1] = max_key_position


for x in code8:
    move(x)

#print(followed_route)   


#for position in followed_route.values():

#print(list(followed_route.values()))

positions = list(followed_route.values())
positions = [i for i in positions if positions.count(i)%2!=0]
#print('positions',sorted(positions, key = lambda x: int(x[0])))

if positions!=[]:
    max_x = sorted(positions, key = lambda x: int(x[0]))[-1][0]
    max_y = sorted(positions, key = lambda x: int(x[1]))[-1][1]
    min_x = sorted(positions, key = lambda x: int(x[0]))[0][0]
    min_y = sorted(positions, key = lambda x: int(x[1]))[0][1]

    #print(max_x,max_y,min_x,min_y)


    positions_matrix = []
    for i in range(max_y-min_y+1):
        y=i+min_y
        row = []
        for j in range(max_x-min_x+1):
            x=j+min_x
            if [x,y] in positions:
                row.append(on)
            else:
                row.append(off)
        #print('row',row)
        positions_matrix.append(row)
    positions_matrix.reverse()
    #print(*positions_matrix,sep='\n')


    for i in range(len(positions_matrix)):
        print(*positions_matrix[i],sep='')