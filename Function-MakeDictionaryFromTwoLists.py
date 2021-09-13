def make_dict(lst1,lst2):
    myDict = dict()
    for x in range(len(lst1)):
        Mykey = lst1[x]
        MyValue = lst2[x]
        myDict[Mykey]= MyValue
    return myDict

abc1=['a','b','c']
abc2=[1,2,3]    

print(make_dict(abc1, abc2))
