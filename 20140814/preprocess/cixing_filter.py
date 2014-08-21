#coding utf-8
import os
import sys
import re

f1=open("/home/alber/data_base/jd_content/app-mac/mac-result1.txt",'r')
txt=f1.readlines()
f1.close()
txtlist=[]
cixing=["/x","/zg","/uj","/ul","/e","/d","/uz","/y"]
for line in txt:
	line_list2=re.split('[ ]', line)
	line_list=line_list2[:]
	for segs in line_list2:
		for K in cixing:
			if K in segs:
				line_list.remove(segs)
				break
			else:
				pass
	txtlist.extend(line_list)
f2=open("/home/alber/data_base/jd_content/app-mac/mac-result2.txt",'a')
resultlist=txtlist[:]	
for v in txtlist:
	if "/" in v:
		slope=v.index("/")
		letter=v[0:slope]+" "
		f2.write(letter)
	else:
		f2.write(v)