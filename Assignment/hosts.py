#!/usr/bin/python3

# Terminal/Command Prompt instructions
# copy/paste/tab/enter--> cd C:\Users\eness\Desktop\UTS\#Subjects\2023-1-Autumn
# copy/paste/tab/enter--> cd A
# copy/paste---> C:/Users/eness/AppData/Local/Microsoft/WindowsApps/python3.8.exe "hosts.py" -v file.txt

import sys,re,os

if len(sys.argv) in [1,2] or sys.argv[1] not in ['-a','-d','-c','-v'] or (sys.argv[1] in ['-d','-c'] and len(sys.argv)<4):
    print('Wrong/zero argument provided.')
    sys.exit()
elif sys.argv[1] in ['-a','-v'] and os.path.exists(sys.argv[2])==0:
    print('File is not existing')
    sys.exit()
elif sys.argv[1] in ['-d','-c'] and os.path.exists(sys.argv[3])==0:
    print('File is not existing')
    sys.exit()

def task_4(option):
    try:
        count=0
        f = open(sys.argv[option])
        for line in f:
            line = line.rstrip('\n')
            x=re.split('\s+',line)
            print(x)
            if x:
                if count==0:
                    print('Hostnames:')
                print(f'<{x[1]}>')
                count+=1

        if count==0:
            print('No hosts')

    except:
        print('File is not accessible')
        sys.exit()

def task_5(option):
    try:
        found = 0
        f = open(sys.argv[option])
        for line in f:
            line = line.rstrip('\n')
            regex = r'\.'+sys.argv[2]+r'\s+.+$'
            match_ = re.search(regex,line)
            if match_:
                print(line)
                found+=1

        if found==0:
            print('No hosts in the given domain')
    except:
        print('File is not accessible')
        sys.exit()

def task_6(class_,file_):
    try:
        count=0
        f = open(file_)
        for line in f:
            line = line.rstrip('\n')
            regex = r'^\d+'
            match_ = re.search(regex,line)

            if match_:
                ip=int(match_.group())

                if class_=='A' and 0<=ip<=127:
                    print(line)
                    count+=1
                elif class_=='B' and 128<=ip<=191:
                    print(line)
                    count+=1
                elif class_=='C' and 192<=ip<=255:
                    print(line)
                    count+=1
            
        if count==0:
            print('No hosts in the given class')

    except:
        print('File is not accessible')
        sys.exit()

if sys.argv[1]=='-a':
    task_4(2)

elif sys.argv[1]=='-d':
    task_5(3)

elif sys.argv[1]=='-c':
    task_6(sys.argv[2],sys.argv[3])

elif sys.argv[1]=='-v':
    try:
        f = open(sys.argv[2])
        print('Enes Sahin 14051662 12/05/2023')
    except:
        print('File is not accessible')
        sys.exit()