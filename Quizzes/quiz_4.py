# COMP9021 20T3 - Rachid Hamadi
# Quiz 4 *** Due Friday Week 7 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a strictly positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys
from time import sleep


def encode(list_of_integers):
    list1=list(list_of_integers)
    list1=[bin(x)[2 :] for x in list1]
    
    no2=[]
    for x in list1:
        for y in x:
            no2.append(y*2)

        if x==list1[-1]: break    
        no2.append('0')
    
    no2=''.join(no2)
    
    no3=0
    for index,x in enumerate(no2):
        no3 += int(x)*2**((len(no2)-1)-index)
    
    return no3 

def decode(integer):
    no_2=bin(the_input)[2 :]
    no_2=list(no_2)

    if len(no_2)==1:
        return None

    no_2_indices=[]
    parts=[]
    for index,x in enumerate(no_2):

        if x=='0' and 0 < index < (len(no_2)-1) and no_2[index+1]=='1' and no_2[index-1]=='1':
            no_2_indices.append(index)

        elif x=='0' and 0 < index < (len(no_2)-1) and no_2[index-1]=='0' and no_2[index+1]=='1'\
            and no_2[index-2]=='0' and index%2==0 and len(no_2_indices)%2==0:

            no_2_indices.append(index)

        elif x=='0' and 0 < index < (len(no_2)-1) and no_2[index-1]=='0' and no_2[index+1]=='1'\
            and no_2[index-2]=='0' and index%2==1 and len(no_2_indices)%2==1:

            no_2_indices.append(index)   

    if no_2_indices:
        for index,x in enumerate(no_2_indices):

            if index==0 and len(no_2_indices)>1:
                parts.append(no_2[:x])

            elif no_2_indices[index]==no_2_indices[-1] and len(no_2_indices)>1:
                parts.append(no_2[(no_2_indices[index-1])+1:x])
                parts.append(no_2[x+1:])

            elif len(no_2_indices)>1:
                parts.append(no_2[(no_2_indices[index-1])+1:x]) 

            elif len(no_2_indices)==1:
                parts.append(no_2[:x])
                parts.append(no_2[(x+1):]) 
    else:
        parts.append(no_2) 


    for x in parts:
        for y in range(0,len(x)-1,2):
            if x[y]!=x[y+1]:
                print('1')
                return None

    for index,x in enumerate(parts):
        z=[]
        for y in range(0,len(x),2):
            z.append(x[y])
        parts[index]=z

    
    parts2=[]
    for x in range(len(parts)):
        parts2.append(''.join(parts[x]))
    
    for x in range(len(parts2)):
        parts2[x]=int(parts2[x],2)
    
    if parts2:
        return parts2
    else:
        return None


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
sleep(0.00001)
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
