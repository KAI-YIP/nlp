#coding--utf-8
import numpy as np

trace=[]
for x in [25,30,35]:
	position="/home/alber/experiment/20140721/lda/model-final-"+str(x)+".txt"
	trace.append(position)

f1=open(trace[1],'r')
topic_set=f1.readlines()
f1.close()
Topic={}
buff=0
for line in topic_set:
	buff+=1
	if buff<=31:
		if "Topic" in line:
			line_clean1=" ".join(line.split())
			word_list=[]
			Name=line_clean1
		else:
			line_clean2=line.split()
			word_list.append(line_clean2[0])
	Topic[Name]=word_list
	buff=0
letter_list=[]
for key in Topic:
	for letter in Topic[key]:
		if letter not in letter_list:
			letter_list.append(letter)
		else:
			pass
print (len(Topic))
print (len(letter_list))

f2=open("/home/alber/experiment/20140721/topic_matric_set_30_3.txt",'a')

topic_set={}
yuzhi=10
for key in Topic:
	value=0
	topic_each=set(Topic[key])
	for seg in Topic:
		topic_seg=set(Topic[seg])
		topic_sub=topic_seg&topic_each
		if len(topic_sub)>=5:
			value+=1
	topic_set[key]=value
print (len(topic_set))
word_frequency=sorted(topic_set.items(), key=lambda d: d[1],reverse=True)
print (word_frequency)
