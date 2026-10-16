# 1. Structure : ()
tu= (10, 20, 30 )  # For myultiple elements in tuple
tu= (60 , )        # for storing single elemnt in tuple use comma(ele ,) 
# tu=10,20,30,40,50,60

# 2 . Heterogenous
tu=(10, 20, 30 ,'abc')

# 3 . Ordered

#4 .Immutable
# tu[0]=50         raised error

# 5. Duplication allowed




print(tu)
print(type(tu))

# 6 .Tuple is faster than list
import sys

tu=()
li=[]
print(sys.getsizeof(tu))
print(sys.getsizeof(li))