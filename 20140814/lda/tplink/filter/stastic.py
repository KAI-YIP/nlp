# -*- coding: UTF-8-*-
import matplotlib.pyplot as plt

def avg(int_list):
	avg_list=[]
	for line in int_list:
		avg_list.append(int(line))
	if len(avg_list)<1:
		return None
	else:
		return sum(avg_list)/len(avg_list)

useful_topic1=["Topic 19th","Topic 2th","Topic 11th","Topic 25th","Topic 5th","Topic 29th","Topic 6th","Topic 1th","Topic 16th","Topic 3th","Topic 8th","Topic 15th","Topic 12th","Topic 18th","Topic 10th","Topic 23th","Topic 7th"]
useful_topic2=["Topic 1th","Topic 27th","Topic 7th","Topic 22th","Topic 24th","Topic 12th","Topic 25th","Topic 2th","Topic 8th","Topic 5th","Topic 26th","Topic 23th","Topic 16th","Topic 10th","Topic 28th","Topic 4th","Topic 0th","Topic 9th"]
useful_topic3=["Topic 19th","Topic 2th","Topic 11th","Topic 25th","Topic 5th","Topic 29th","Topic 6th","Topic 1th","Topic 16th","Topic 3th","Topic 8th","Topic 15th","Topic 12th","Topic 18th","Topic 10th","Topic 23th","Topic 7th"]
f=open("./result2B.txt",'r')
dict_topic={}
for line in f.readlines():
	line_clean=line.split(":")
	target=line_clean[1].split()
	dict_topic[line_clean[0]]=avg(target)
dict_topic_order=sorted(dict_topic.items(), key=lambda d:d[1], reverse = True)
x_word=[]
y=[]
for k,v in dict_topic_order:
	x_word.append(k)
	y.append(float(v))
plt.title("主题稳定性排序",color='black')
plt.xlabel("主题",color='black')
plt.ylabel("稳定性",color='black')
x=range(len(y))
plt.plot(x,y,"--",color="red",linewidth=2)
plt.xticks(x,x_word)
count=0
for label in plt.gca().xaxis.get_ticklabels(): 
	label.set_rotation(90)
	label.set_ha('center')
	if x_word[count] in useful_topic2:
		label.set_color('green')
	else:
		label.set_color('blue')
	count+=1
plt.show()