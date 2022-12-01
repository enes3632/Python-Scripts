import sys
from time import sleep
import re
import json

def isvalid(word,a):
    
    print(word)
    x=re.('',word)
    print(x)


def is_valid(word, arity):
    a=int(arity)

    word_list=[]

    for x in word:
        word_list.append(x)
    # print(word_list)

    if a==0:
        for x in word_list:
            if x.isalpha()  :pass
            elif x=='_'     :pass
            else            :return False

    if a!=0:

        open_bra=0
        close_bra=0

        for x in word_list:
            try:
                if x=='(' and open_bra>=close_bra and a!=0  :open_bra+=1
                elif x==')'and open_bra>close_bra and a!=0  :close_bra+=1
            except: return False    
        
        if not open_bra==close_bra: return False
        
        for x in word_list:
            if not x=='(':
                if x.isalpha():pass
                elif x=='_':pass
                else: return False
            else: break
    
        try:
            par_index = word_list.index('(')
            word_list = word_list[par_index:]
       
        except: return False
        
        for index, x in enumerate(word_list):
            if x.isalpha()              :pass
            elif x in [',','(',')']     :pass
            elif x==' '     :
                if word_list[index-1] in [',','(',')',' '] or word_list[index+1] in [',','(',')',' ']\
                                            :pass
                else                        :return False
            else                        :return False
        
        open=0
        comma=0
        for index,x in enumerate(word_list):
            if x=='(':
                open+=1
            elif open==1 and x==',':
                    comma+=1

            elif x==')':
                open-=1
            elif open==0:
                break

        comma+=1
        if comma!=a:return False   

    
    if not isvalid(word,a):
        return False

    return True
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
    sleep(0.001)
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
sleep(0.001)
word = input('Input a word: ')
sleep(0.001)
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')