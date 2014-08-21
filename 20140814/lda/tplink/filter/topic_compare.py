#coding--utf-8
import numpy as np

trace=[]
for x in list(range(30)):
	position="/home/alber/NLP/20140814/lda/tplink/diff-sampling/model-"+str(x+1)+".txt"
	trace.append(position)

f1=open(trace[1],'r')
topic_set=f1.readlines()
f1.close()
Topic={}
buff=0
for line in topic_set:
	buff+=1
	if buff<=51:
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
f2=open("/home/alber/NLP/20140814/lda/tplink/filter/topic_correlation.txt",'a')
for x in list(range(30)):
	f2.write(str(x)+"    ")
f2.write("\n")
for j in list(range(30)):
	for i in list(range(30)):
		a=set(Topic["Topic "+str(j)+"th:"])&set(Topic["Topic "+str(i)+"th:"])
		f2.write(str(len(a))+"    ")
	f2.write("\n")

f2.close()