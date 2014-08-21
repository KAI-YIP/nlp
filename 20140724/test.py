#coding--utf-8
import numpy as np


f=open("/home/alber/experiment/20140724/topic_correlation_35.txt",'r')

ar_list=[]
for line in f.readlines():
	topic_correlation=[]
	line_list=line.split()
	count=0
	for num in line_list:
		if int(num)>=4:
			topic_correlation.append(count)
			count+=1
		else:
			count+=1
	ar_list.append(topic_correlation)

print (ar_list[0])

f2=open("/home/alber/experiment/20140724/35opic_correlation_for_AR.txt",'a')
for line in ar_list:
	for word in line:
		f2.write(str(word)+"  ")
	f2.write("\n")


