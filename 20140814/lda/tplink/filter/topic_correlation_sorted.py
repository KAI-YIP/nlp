#coding--utf-8
import matplotlib.pyplot as plt

useful_topic2=["Topic 1th","Topic 27th","Topic 7th","Topic 22th","Topic 24th","Topic 12th","Topic 25th","Topic 2th","Topic 8th","Topic 5th","Topic 26th","Topic 23th","Topic 16th","Topic 10th","Topic 28th","Topic 4th","Topic 0th","Topic 9th"]
f=open("/home/alber/NLP/20140814/lda/tplink/filter/topic_correlation.txt",'r')
topic_dict={}
count=0
for line in f.readlines():
	line_list=line.split()
	Total_line=0
	for number in line_list:
		if int(number)>=10:
			Total_line+=1
	name="Topic "+str(count)+"th"
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
	if x_label[count] in useful_topic2:
		label.set_rotation(90)
		label.set_ha('center')
		label.set_color('green')
	else:
		label.set_rotation(90)
		label.set_ha('center')
		label.set_color('blue')
	count+=1
plt.show()
