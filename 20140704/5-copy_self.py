#coding utf-8
import os
import sys

f1=open("/home/alber/experiment/20140704/sample-result3.txt","r")
txt=f1.readlines()
f1.close()
f2=open("/home/alber/experiment/20140704/sample-result4.txt",'a')

for line in txt:
	a=" ".join(line.split())
	line_extend=a+" "+a+" "+a+" "+a+" "+a+"\n"
	f2.write(line_extend)
f2.close()