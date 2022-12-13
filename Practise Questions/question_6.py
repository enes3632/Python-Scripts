# COMP9021 20T3 - Rachid Hamadi
# Final Exam - Question 6

def found_word_in(word, filename):
    
    '''
    Returns True or False depending on whether "word" can be read
    from the grid represented in the provided file "filename",
    assumed to be stored in the working directory.
	
    There can be spaces anywhere in the file. In particular,
    letters on a given line of the file can be separated by an
    arbitrary number of spaces (possibly none), and there can be
    lines with nothing but spaces.

    Words are to be read HORIZONTALLY FROM LEFT TO RIGHT,
    or VERTICALLY FROM TOP TO BOTTOM,
    or DIAGONALLY FROM TOP LEFT TO BOTTOM RIGHT
    
    
    >>> found_word_in('MANGANESE', 'word_search_1.txt'),\
        found_word_in('GOLD', 'word_search_1.txt')
    (True, False)
    >>> found_word_in('NICKEL', 'word_search_1.txt'),\
        found_word_in('SILVER', 'word_search_1.txt')
    (True, True)
    >>> found_word_in('ZINC', 'word_search_1.txt'),\
        found_word_in('RUBIS', 'word_search_1.txt')
    (True, False)
    >>> found_word_in('BANANA', 'word_search_2.txt'),\
        found_word_in('RASPBERRY', 'word_search_2.txt')    
    (True, True)
    '''
    
    with open(filename) as file:
        matrix = [x.split() for x in file]
        matrix = [x for x in matrix if x!=[]]

        for x in range(len(matrix)):
            if len(matrix[x])==1:
                matrix[x] = list(matrix[x][0])
    
    # for x in matrix:
    #     print(x)

    def horizontally(matrix, word):

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                
                if matrix[x][y]==word[0]:
                    
                    if ''.join(matrix[x][y:y+len(word)])==word:
                        return True
    
    def vertically(matrix, word):

        for y in range(len(matrix[0])):
            for x in range(len(matrix)):
                z=''

                if matrix[x][y]==word[0]:

                    for t in range(len(word)):
                        if t+x<len(matrix):

                            z+=matrix[x+t][y]

                if z==word:
                    return True

    def diagonally(matrix, word):

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                z=''
                # k=x
                # kk=y

                if matrix[x][y]==word[0]:

                    for t in range(len(word)):
                        if t+x < len(matrix) and t+y<len(matrix[0]):

                            z+=matrix[x+t][y+t]
                    # print(z)     
                if z==word:
                    return True

    hor = horizontally(matrix, word)
    ver = vertically(matrix, word)
    dia = diagonally(matrix, word)

    if hor or ver or dia:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()


