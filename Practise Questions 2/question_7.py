# COMP9021 20T3 - Rachid Hamadi
# Sample Exam Question 7

# Write a function that accepts a string of DISTINCT UPPERCASE letters only called letters and 
# displays all pairs of words using all (distinct) letters in letters.

# Please note that the words need to be valid. Use the provided dictionary.txt to check the validity 
# of words.  

'''
Will be tested with height a strictly positive integer.
'''


def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
     0
    123
    >>> f(3)
      0
     123
    45678
    >>> f(4)
       0
      123
     45678
    9012345
    >>> f(5)
        0
       123
      45678
     9012345
    678901234
    >>> f(6)
         0
        123
       45678
      9012345
     678901234
    56789012345
    >>> f(20)
                       0
                      123
                     45678
                    9012345
                   678901234
                  56789012345
                 6789012345678
                901234567890123
               45678901234567890
              1234567890123456789
             012345678901234567890
            12345678901234567890123
           4567890123456789012345678
          901234567890123456789012345
         67890123456789012345678901234
        5678901234567890123456789012345
       678901234567890123456789012345678
      90123456789012345678901234567890123
     4567890123456789012345678901234567890
    123456789012345678901234567890123456789
    '''
    # Insert your code here

    if height < 3:
        y = [str(t) for t in range(10)]

    else:
        y = []
        for x in range((height*height)//10):
            for z in range(10):
                y.append(str(z))

        for x in range((height*height)%10):
            y.append(str(x))

    y=''.join(y)

    t = []
    z=1
    k=0
    j=3
    for x in range(height):

        t.append(y[0+k : z])

        k = z
        z += j
        j += 2

    for x in range(height):

        print(' '*(height-1-x) + str(t[x]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
