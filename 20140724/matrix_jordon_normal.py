#coding--utf-8
import numpy as np
from sympy import Matrix

f=open("/home/alber/experiment/20140724/topic_correlation.txt",'r')
topic=[]
for line in f.readlines():
	line_list=line.split()
	topic.append(line_list)
print (len(topic))
print (len(topic[1]))

m=Matrix(topic)
(p,j)=m.jordan_form()
print (len(j))
