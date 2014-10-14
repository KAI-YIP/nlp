#coding=utf-8
import matplotlib.pylab as plt

f=open('./correlation2.txt','r')
f2=open('./sorted_correlation2.txt','a')
topic_dict={}
for line in f.readlines():
	line_clean=line.split()
	value=float(line_clean[2])
	if line_clean[0] not in topic_dict:
		topic_dict[line_clean[0]]=value
	elif line_clean[0] in topic_dict:
		topic_dict[line_clean[0]]+=value
	if line_clean[1] not in topic_dict:
		topic_dict[line_clean[1]]=value
	elif line_clean[1] in topic_dict:
		topic_dict[line_clean[1]]+=value
sorted_topic_dict=sorted(topic_dict.items(),key=lambda d: d[1],reverse=True)
x_topic=[]
y=[]
for k,v in sorted_topic_dict:
	x_topic.append(k)
	y.append(v)
plt.xlabel("Topic")
plt.ylabel("Topic得分")
x=range(len(y))
plt.plot(x,y,color='red')
plt.xticks(x,x_topic)
for label in plt.gca().xaxis.get_ticklabels(): 
     label.set_rotation(90)
     label.set_ha('center')
     label.set_color('black')
plt.show()
