# COMP9021 20T3 - Rachid Hamadi
# Sample Exam Question 5

# Write a function that accepts a year between 1913 and 2013 inclusive and displays the maximum 
# inflation during that year and the month(s) in which it was achieved.

# You might find the reader() function of the csv module useful, but you can also use the split()
#  method of the str class.

# Make use of the attached cpiai.csv file.

'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv
import operator

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here

    monthss = {}
    z=1
    for x in months:
        monthss[z] = x
        z+=1

    with open('cpiai.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        months_values = []
        if header !=None:

            for row in reader:
                x = row[0].split('-')

                if int(x[0])==year:
                    months_values.append([int(x[1]),float(row[2])])


        maxx = float(max((months_values), key=operator.itemgetter(1))[1])
        achived_months = []

        for x in range(12):

            if months_values[x][1] == maxx:

                achived_months.append(months_values[x][0])

    months2 = [months[x-1] for x in achived_months]

    months3 = ', '.join(months2)


    print(f'In {year}, maximum inflation was: {maxx}')
    print(f'It was achieved in the following months: {months3}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()