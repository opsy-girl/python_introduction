import numpy as np

def get_vector_sum(vectorLower, vectorUpper):
  '''
  INPUT: vector lower and upper bounds
  OUTPUT: calculated value for vector sum
  (1) create a vector ranging from 1:150
  (2) transform the vector into a matrix with 10 rows and 15 columns
  (3) print the sum for the 10 rows
  '''
  vectorArr=[]
  for x in range(vectorLower,vectorUpper):
    vectorArr.append(x)
  arr = np.array(vectorArr)
  arr.resize((10,15)) 
  W=np.sum(arr,axis=1).tolist()
  return W
  
print(get_vector_sum(1,150))


