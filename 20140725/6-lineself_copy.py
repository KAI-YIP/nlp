#coding utf-8
import os
import sys

f1=open("/home/alber/experiment/20140719/dell_result1.txt","r")
txt=f1.readlines()
f1.close()
f2=open("/home/alber/experiment/20140719/dell_result3.txt",'a')

for line in txt:
	if len(line)<=4:
		pass
	else:	
		f2.write(line)
f2.close()