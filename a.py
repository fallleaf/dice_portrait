import os
import sys


f = open('a.txt', 'r', encoding = 'utf-8')
f1 = open('b.txt', 'w', encoding = 'utf-8')
linenumber = 0
for line in f:
    linenumber +=1
    index = line.index(':')
    line = line[index+1 :]
    line = line.strip()
    line = line.replace(',','')
    #print(line)
    t = line[0]
    count = 0
    print('%2d:'%(linenumber),end='', file=f1)
    #f1.write('%2d:'%(linenumber),end='')
    for a in line:
        if t == a:
            count +=1
        else:
            print('【%s】%2d'%(t, count),end='', file=f1)
            #f1.write('【%s】%2d'%(t, count),end='')
            t = a
            count = 1
    print('【%s】%2d'%(t,count), file=f1)
    #f1.write('【%s】%2d'%(t,count))
f.close()
f1.close()