# COMP9021 20T3 - Rachid Hamadi
# Quiz 5 *** Due Friday Week 8 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines moved to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines moved to the right by one position, e.g.
#      111
#       111
#        111
#         111
# The size is the number of 1s in the parallelogram. In the above examples, the size is 12.

from random import seed, randrange
import sys
import operator


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


def size_of_largest_parallelogram():
    
    # ---finding_biggest_rectangle--- #
        
    for x in range(len(grid)):
        for indey, y in enumerate(grid[x]):
            if x!=0 and y==1:
                grid[x][indey]=grid[x-1][indey]+grid[x][indey]

    # for x in range(len(grid)):
    #     print(grid[x])

    indices={}
    count=1
    for x in range(len(grid)):
        for indey,y in enumerate(grid[x][:9]): 

            if y>1:
                for indez,z in enumerate(grid[x]):
                    if z==y and indez>indey:
                        indices[count]=y*(indez-indey+1)
                        count+=1

                    elif z!=y and indez>indey:
                        break


    # ---finding_biggest_right--- #
    # count2=count+1
    # for x in range(len(grid)):
    #     for indey,y in enumerate(grid[x][:9]):
    #         if y==0 and grid[x][indey+1]>1:

    #             for indez,z in enumerate(grid[x]):
    #                 if indez>indey+1 and z==grid[x][indey+1]:
    #                     pass

    #                 elif indez>indey+1 and z!=grid[x][indey+1] and z!=1:
    #                     break

    #                 elif indez>indey+1 and z==1 and grid[x-1][indey]>0:

    #                     for t,q in zip(range(1,x+1),range(0,indey)):

    #                         if grid[x-t][indey-q]>0 and grid[x-t][indey-q+1]>0:

    #                             indices[count2]=(t+1)*(indez-indey)
    #                             count2+=1

    #                         else:
    #                             break    

    count2=count+1
    for x in range(len(grid)):
        for indey,y in enumerate(grid[x][:8]):
            if y>0 and grid[x][indey+1]>0:

                for indez,z in enumerate(grid[x]):

                    if indez>indey and z==0:
                        break

                    elif indez>indey and z>0:

                        for t in range(1,x+1):
                            if indey!=0:
                                if len([q for q in grid[x-t][indey-t:indez-t+1] if q!=0])==(indez-indey+1):
            
                                    #print([q for q in grid[x-t][indey+1:indez+2] if q!=0])
                                    indices[count2]=(t+1)*(indez-indey+1)
                                    #print(count2,x,indey,indez)
                                    count2+=1
                                else:break
   
                            else:
                                break

    # ---finding_biggest_left--- #
    count3=count2+1
    for x in range(len(grid)):
        for indey,y in enumerate(grid[x][:8]):
            if y>0 and grid[x][indey+1]>0:

                for indez,z in enumerate(grid[x]):

                    if indez>indey and z==0:
                        break

                    elif indez>indey and z>0:

                        for t in range(1,x+1):
                            if indez+1<10:
                                if len([q for q in grid[x-t][indey+t:indez+t+1] if q!=0])==(indez-indey+1):
            
                                    #print([q for q in grid[x-t][indey+1:indez+2] if q!=0])
                                    indices[count2]=(t+1)*(indez-indey+1)
                                    #print(count2,x,indey,indez)
                                    count2+=1
                                else:break
   
                            else:
                                break

    #print(indices) 
    try:                         
        return (indices.get(max(indices.items(), key=operator.itemgetter(1))[0]))
    except:
        return None



try:
     
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')