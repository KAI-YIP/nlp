#coding=utf-8  
import sys
import os
import re
import time

t1=time.time()
f1=open("/home/alber/experiment/20140719/prio_result.txt",'r')
topic_txt=f1.readlines()
f1.close()
topic={}
for line in topic_txt:
	line_list=line.split()
	topic[line_list[0]]=line_list
print (topic)
f2=open("/home/alber/experiment/test.txt",'r')
target_txt=f2.readlines()
f2.close()
document=[]
for line in target_txt:
	line_clean=line.split()
	line_new=[]
	for word in line_clean:
		word_ctrl=0
		for key in topic:
			if word in topic[key]:
				line_new.append(key+" ")
				word_ctrl=1
				break
			else:
				pass
		if word_ctrl==0:
			line_new.append(word+" ")
		else:
			pass
	document.extend(line_new)
	document.extend('\n')
print (len(document))
f3=open("/home/alber/experiment/20140721/dell_test.txt",'a')
for word in document:
	f3.write(word)
f3.close()
t2=time.time()

print ("topic match is finished in %f"%(t2-t1))