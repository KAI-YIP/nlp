#coding=utf-8
import os
import sys
import re
import time

f1=open("/home/alber/experiment/20140709/sample_result3.txt",'r')
f2=open("/home/alber/experiment/20140709/sample_result4.txt","a")
txt=f1.readlines()
f1.close()
list1=[]
for line in txt:
	if len(line)>=4:
		line_clean=" ".join(line.split())
		lines=line_clean+" "+"\n"
		f2.write(lines)
	else:
		pass
f2.close()