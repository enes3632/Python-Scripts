# COMP9021 20T3 - Rachid Hamadi
# Quiz 1 *** Due Friday Week 3 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
complete_dictionary = mapping.copy()
complete_keys = list(complete_dictionary.keys())
# cycles_list = []
for key in complete_keys:
    #print(key)
    travel_key = key
    visited_keys = [travel_key]
    value = complete_dictionary[travel_key]
    #print('*',travel_key,value)
    while key!=value and value not in visited_keys:
        #print(travel_key,value)
        travel_key = value
        
        
        try:
            value = complete_dictionary[travel_key]
        except:
            break
    
        visited_keys.append(travel_key)
        
    if key==value:
        #print('cycle found',visited_keys)
        cycles.append(visited_keys)
    elif value in visited_keys:
        pass
        #print('other loop')
    else:
        pass
        #print('otherwise')
cycles = [list(i) for i in list(set(tuple(sorted(sub)) for sub in cycles)) ]
cycles = sorted(cycles, key=lambda x: x[0]) 
print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)

all_values = list(complete_dictionary.values())
all_values = list(set(all_values))
all_values.sort()

reversed_dict_per_length = {}
for value in all_values:
    reversed_dict_per_length[value] = []
    for key2 in complete_keys:
        if complete_dictionary[key2]==value:
            reversed_dict_per_length[value].append(key2)

{x: y for x, y in sorted(reversed_dict_per_length.items(), key=lambda item: item[1])}
#pprint(reversed_dict_per_length)

xxx_dict = {}  # dict:{length:{keys:[values]}}
for key,values in reversed_dict_per_length.items():
    try:
        xxx_dict[len(values)][key] = values
    except:    
        xxx_dict[len(values)] = {}
        xxx_dict[len(values)][key] = values

x_dict = dict(sorted(xxx_dict.items()))

print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(x_dict)
