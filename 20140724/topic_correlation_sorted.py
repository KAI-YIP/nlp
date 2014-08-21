#coding--utf-8
import numpy as np
import matplotlib.pyplot as plt

useful_topic_30=["topic  0","topic  3","topic  26","topic  28","topic  4","topic  6","topic  19","topic  7","topic  8","topic  15","topic  15","topic  16","topic  17"]
useful_topic_35=["topic  1","topic  8","topic  26","topic  29","topic  30","topic  32","topic  5","topic  7","topic  17","topic  20","topic  24","topic  9","topic  10","topic  12","topic  11","topic  16","topic  25","topic  33"]
f=open("/home/alber/experiment/20140724/topic_correlation.txt",'r')
topic_dict={}
count=0
for line in f.readlines():
	line_list=line.split()
	Total_line=0
	for number in line_list:
		if int(number)>=3:
			Total_line+=int(number)
	name="topic  "+str(count)
	topic_dict[name]=Total_line
	count+=1
Topic=sorted(topic_dict.items(), key=lambda d: d[1],reverse=True)
y=[]
x_label=[]
for k,v in Topic:
	y.append(v)
	x_label.append(k)
x=range(len(y))
z=range(len(y))
plot1=plt.plot(x,y,"--",label="$topic-correlation$",color="red",linewidth=2)
plt.xlabel("TOPIC",color='black')
plt.ylabel("交集总数",color='black')
plt.title("交集总数")
plt.legend()
plt.xticks(x,x_label)
count=0
for label in plt.gca().xaxis.get_ticklabels(): 
	if x_label[count] in useful_topic_30:
		label.set_rotation(90)
		label.set_ha('center')
		label.set_color('green')
	else:
		label.set_rotation(90)
		label.set_ha('center')
		label.set_color('red')
	count+=1
plt.show()
