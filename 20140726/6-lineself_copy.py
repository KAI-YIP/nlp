#coding utf-8
import os
import sys

f1=open("/home/alber/experiment/20140726/sample_result4.txt","r")
txt=f1.readlines()
f1.close()
f2=open("/home/alber/experiment/20140726/sample_result5.txt",'a')

for line in txt:
	if len(line)<=4:
		pass
	else:	
		line_clean=" ".join(line.split())
		f2.write(line_clean+" "+line_clean+"\n")
f2.close()