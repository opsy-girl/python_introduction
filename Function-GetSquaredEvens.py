def get_squared_evens(lst):
    newList = []
    for x in lst:
        if x%2 == 0:
            newList.append(x**2)
    return newList          
                  
abc = [1,2,3,4,5,6,7]    
print(get_squared_evens(abc))
