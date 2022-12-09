# COMP9021 20T3 - Rachid Hamadi
# Final Exam - Question 2
from copy import deepcopy

def filtered_sequence(L, n):
    
    '''
    Returns a list LL that keeps from L all elements e
    that are part of a sub-sequence of length at least n.
    
    All elements of the sub-sequence have the same value as e.
        
    You can assume that L is a list of valid integers.

    >>> filtered_sequence([], 2)
    []
    >>> filtered_sequence([7], 0)
    [7]
    >>> filtered_sequence([7], 1)
    [7]
    >>> filtered_sequence([7], 2)
    []
    >>> filtered_sequence([1, 3, 1, 2, 5, 6, 8, 2], 1)
    [1, 3, 1, 2, 5, 6, 8, 2]
    >>> filtered_sequence([1, 3, 3, 3, 2, 4, 4, 5, 6, 6, 6, 6], 2)
    [3, 3, 3, 4, 4, 6, 6, 6, 6]
    >>> filtered_sequence([7, 7, 7, 7, 2, 2, 7, 3, 4, 4, 4, 6, 5], 3)
    [7, 7, 7, 7, 4, 4, 4]
    >>> filtered_sequence([1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 5, 5, 5, 5, 5, 6], 4)
    [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]
    '''
    
    LL = []
    # INSERT YOUR CODE HERE
    L1 = deepcopy(L)
    L2 = []
    L3 = []

    if not L:
        return LL
    
    elif n==0 and L:
        return L

    elif n==1 and L:
        return L

    elif n > len(L):
        return LL

    elif n>1 and L:

        for x in range(len(L1)-1):
            if L1[x]==L1[x+1]:

                for y in range(x, len(L1)):
                    if L1[y]!=L1[x]:
                        L2.append([L1[x], y-x])
                        break
                    elif y==len(L1)-1:
                        L2.append([L1[x], y-x+1])
                        break

        for index, x in enumerate(L2):

            if index!=0:
                if x[0] != L2[index-1][0] and x[1]>=n:
                    for y in range(x[1]):

                        L3.append(x[0])

            if index==0 and x[1>=n]:

                for y in range(x[1]):

                        L3.append(x[0])

        return L3
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

