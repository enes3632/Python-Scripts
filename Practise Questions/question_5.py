# COMP9021 20T3 - Rachid Hamadi
# Final Exam - Question 5

dictionary_file = 'dictionary.txt'

def number_of_words_in_dictionary(word1, word2):
    
    '''
    Determines the number of words between two words "word1"
	and "word2" inclusive in the provided "dictionary.txt".
    
    "dictionary.txt" is stored in the working directory.
    Words in "dictionary.txt" are all uppercase.
    Words are case sensitive.
    
    
    >>> number_of_words_in_dictionary('company', 'company')
    Could not find company in dictionary.
    >>> number_of_words_in_dictionary('company', 'comparison')
    Could not find at least one of company and comparison in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'comparison')
    Could not find at least one of COMPANY and comparison in dictionary.
    >>> number_of_words_in_dictionary('company', 'COMPARISON')
    Could not find at least one of company and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPANY')
    COMPANY is in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPARISON')
    COMPARISON is in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPARISON')
    Found 14 words between COMPANY and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPANY')
    Found 14 words between COMPARISON and COMPANY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIOUSLY')
    Found 2 words between CONSCIOUS and CONSCIOUSLY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIENTIOUS')
    Found 3 words between CONSCIOUS and CONSCIENTIOUS in dictionary.
    '''
    def second(word1):
        with open(dictionary_file) as file:
            indey=0
            for y in file:
                indey+=1
                if y[:-1]==word1:
                    return indey

    w1 = 0
    w2 = 0
    for x in word1:
        if x.islower():
            w1+=1
            break
    
    for x in word2:
        if x.islower():
            w2+=1
            break
    
    if word1==word2 and (w1==1 or w2==1):
        return print(f'Could not find {word1} in dictionary.')
    
    elif word1!=word2 and (w1==1 or w2==1):
        return print(f'Could not find at least one of {word1} and {word2} in dictionary.')


    with open(dictionary_file) as file:
        index = 0
        indey = 0
        for x in file:
            index+=1

            if word1==word2 and x[:-1]==word1:
                return print(f'{word1} is in dictionary.')

            elif word1!=word2 and x[:-1]==word1:

                for y in file:
                    indey+=1
                    if y[:-1]==word2:
                        return print(f'Found {indey+1} words between {word1} and {word2} in dictionary.')

            elif word1!=word2 and x[:-1]==word2:
                indey = second(word1)
                return print(f'Found {indey-index+1} words between {word1} and {word2} in dictionary.')
            
if __name__ == '__main__':     
    import doctest
    doctest.testmod()

