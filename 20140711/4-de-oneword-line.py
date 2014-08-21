#coding=utf-8
import os
import sys

f1=open("/home/alber/experiment/20140711/sample_result4.txt",'r')
txt=f1.readlines()
f1.close()
f2=open("/home/alber/experiment/20140711/sample_result5.txt",'a')
for line in txt:
	line_clean=line.split()
	if len(line_clean)>=2:
		line_new=" ".join(line_clean)+"\n"
		f2.write(line_new)

