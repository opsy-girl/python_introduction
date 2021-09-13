def count_characters(string):
    myDict = dict()
    lenA=0
    lenB=0
    lenC=0
    lenD=0
    lenE=0
    lenF=0
    lenG=0
    lenH=0
    for x in string:
        if x=='a':
            lenA = lenA + 1
        if x=='b':
            lenB = lenB + 1  
        if x=='c':
            lenC = lenC + 1 
        if x=='d':
            lenD = lenD + 1 
        if x=='e':
            lenE = lenE + 1 
        if x=='f':
            lenF = lenF + 1 
        if x=='g':
            lenG = lenG + 1 
        if x=='h':
            lenH = lenH + 1    
    myDict['a']= lenA
    myDict['b']= lenB
    myDict['c']= lenC
    myDict['d']= lenD
    myDict['e']= lenE
    myDict['f']= lenF
    myDict['g']= lenG
    myDict['h']= lenH
    return(myDict)

abc=['a','b','b','c','c','c','d','d','d','d','e','e','e','e','e','f','f','f','f','f','f','g','g','g','g','g','g','g','h','h','h','h','h','h','h','h']
print(count_characters(abc))
  

