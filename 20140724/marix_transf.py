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
count=0
buff=0
for line in topic_set:
	buff+=1
	if buff<=31:
		if "Topic" in line:
			word_list=[]
			Name="topic"+str(count)
			count+=1
		else:
			line_clean=line.split()
			word_list.append(line_clean[0])
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

f2=open("/home/alber/experiment/20140721/topic_matric_30.txt",'a')

for key in Topic:
	f2.write(key+"  ")
	for letter in letter_list:
		if letter in Topic[key]:
			f2.write("1"+"  ")
		else:
			f2.write("0"+"  ")
	f2.write("\n")