# COMP9021 20T3 - Rachid Hamadi
# Sample Exam Question 8

# Write a function that accepts a string of DISTINCT UPPERCASE letters only called letters and
#  displays all pairs of words using all (distinct) letters in letters.

# Please note that the words need to be valid. Use the provided dictionary.txt to check the validity
#  of words.  

'''
Will be tested with letters a string of DISTINCT UPPERCASE letters only.
'''


def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = 'dictionary.txt'
    solutions = []
    # Insert your code here

    letters2 = list(letters)

    f=open(dictionary, 'r')

    words = []
    for x in f:
        words.append(list(x[:-1]))
    
    for x in words:
        z = 0
        letters2 = list(letters)

        for y in x:

            if not y in letters2:
                z+=1
                break
            else:
                letters2.remove(y)

        if z==0:
            
            for xx in words:

                letters3 = letters2
                k = len(letters3)

                if len(list(xx))==len(letters3):

                    for yy in xx:

                        if str(yy) in letters3:
                            k-=1
                            letters3.remove(yy)
                        else:

                            break

                    if k==0:
                
                        solutions.append([x, xx])

    solutions = [y for x in solutions for y in x]
    
    for x in range(len(solutions)):
        z=''
        for y in solutions[x]:
            z+=y

        solutions[x]=z

    for x in solutions:
        if solutions.count(x)>1:
            solutions.remove(x)

    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')

        for x in range(0, len(solutions), 2):
            
            y = [solutions[x], solutions[x+1]]
            y.sort()

            print(f'(\'{y[0]}\', \'{y[1]}\')')



if __name__ == '__main__':
    import doctest
    doctest.testmod()
