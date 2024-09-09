# -*- coding: cp1252 -*-
import sys

print sys.argv[0],sys.argv[1],sys.argv[2]

if sys.argv[1] == 'soma':
    res = float(sys.argv[2]) + float(sys.argv[3])

elif sys.argv[1] == 'mult':
    res = float(sys.argv[2]) * float(sys.argv[3])
    
else:
    res = u'Não existe operação!'

print res
