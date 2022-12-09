# COMP9021 20T3 - Rachid Hamadi
# Final Exam - Question 3

# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def f(width, height):
    
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when
    z is reached.

    You can assume that width and height are strictly positive integers
    
    >>> f(1, 1)
    a
    >>> f(2, 3)
    ab
    dc
    ef
    >>> f(3, 2)
    abc
    fed
    >>> f(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    
    # INSERT YOUR CODE HERE
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',\
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #26 letters

    alphabet2 = []

    rectangle = []

    if width*height < 26:
        z=0
        for x in range(height):
 
            if x%2==0:
                rectangle.append(alphabet[z:z+width])
                z+=width
            else:
                a = alphabet[z:z+width]
                a = a[::-1]
                rectangle.append(a)
                z+=width

        for x in rectangle:
            x = ''.join(x)
            print(x)
    
    else:
        length = (width * height) // 26 + 1
        
        for x in range(length):
            for y in range(26):
                alphabet2.append(alphabet[y])

        z=0
        for x in range(height):
 
            if x%2==0:
                rectangle.append(alphabet2[z:z+width])
                z+=width
            else:
                a = alphabet2[z:z+width]
                a = a[::-1]
                rectangle.append(a)
                z+=width

        for x in rectangle:
            x = ''.join(x)
            print(x)

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

