#Reduce function

from functools import reduce
list2 =[1,2,3,4,5]
fins = reduce(lambda x,y:x+y, list2)
print(fins)

#o/p : 15 

# reduce similar to this concept
list2 =[1,2,3,4,5]
adds = 0
for i in list2:
    adds+=i
print(adds)