#coding--utf-8
import numpy as np
from sympy import Matrix

a=np.array([[5, 4, 2, 1], [0, 1, -1, -1], [-1, -1, 3, 0], [1, 1, -1, 2]])
m=Matrix(a)
print (m)
(P,j)=m.jordan_form()
print (j)