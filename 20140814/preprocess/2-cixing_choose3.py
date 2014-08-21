#coding utf-8
import re

f1=open("/home/alber/NLP/20140814/jd_comment/tplink_result0.txt",'r')
txt=f1.readlines()
f1.close()
txtlist=[]
noun=["/n","/ns","/nt","/nz","/ng"]
verb=["/v","/vd","/vn","/vshi","/vyou","/vf","/vx","/vi","/vl","/vg"]
odjective=["/a","/ad","/an","/ag","/al"]
other=["/l","/eng","/m","/mq","/t","/tg","/f","/s","/user"]
cixing=noun+verb+odjective+other
for line in txt:
	line_list2=re.split('[ ]', line)
	for seg in line_list2:
		for k in cixing:
			if k in seg:
				txtlist.append(seg)
				break
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
f2=open("/home/alber/NLP/20140814/jd_comment/tplink_result1.txt",'a')
for segs in wordlist:
	f2.write(segs+" ")
f2.close()

