#coding utf-8
import os
import sys
import re

f1=open("/home/alber/experiment/20140704/sample-result1.txt",'r')
txt=f1.readlines()
f1.close()
txtlist=[]
noun=["/n"]
verb=["/v"]
odjective=["/a"]
other=["/l","/eng","/m","/mq","/t","/tg","/f","/s"]
cixing=noun
for line in txt:
	line_list2=re.split('[ ]', line)
	for seg in line_list2:
		for k in cixing:
			if k in seg:
				txtlist.append(seg)
			else:
				pass
	txtlist.append("\n")
wordlist=[]
for v in txtlist:
	if "/" in v:
		position=v.index("/")
		wordlist.append(v[:position])
	else:
		wordlist.append(v)
f2=open("/home/alber/experiment/20140704/sample-result2.txt",'a')
for segs in wordlist:
	f2.write(segs+" ")
f2.close()