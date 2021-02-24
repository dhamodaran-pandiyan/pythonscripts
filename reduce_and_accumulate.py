li = [1,2,3,4,5]
import functools
from itertools import accumulate
ixor_out = accumulate(li, lambda x,y : x^y)
xor_out = functools.reduce( lambda x,y : x^y, li)

print(xor_out)
print(list(ixor_out))

#output
# 1                                                                                                                                              
# [1, 3, 0, 4, 1]  
