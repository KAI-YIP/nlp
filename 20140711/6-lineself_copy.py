#coding utf-8
import os
import sys

f1=open("/home/alber/experiment/20140711/sample_result5.txt","r")
txt=f1.readlines()
f1.close()
f2=open("/home/alber/experiment/20140711/sample_result6.txt",'a')
lines=0
for line in txt:
	lines=lines+1
	a=" ".join(line.split())
	line_extend=a+" "+a+" "+a+" "+a+" "+a+"\n"
	f2.write(line_extend)
print lines
f2.close()