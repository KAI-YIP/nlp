#coding=utf-8
import matplotlib.pylab as plt

f=open("./inference.txt",'r')
data=[]
print ("读取数据完毕")
for line in f.readlines():
	topic_dict={}
	line_clean=line.split()
	i=0
	for one in line_clean:
		name="topic"+str(i)
		topic_dict[name]=one
		i+=1
	topic_tuple=sorted(topic_dict.items(),key=lambda d:d[1],reverse=True)
	data.append(topic_tuple)
print ("得到排序数据")
x_name=[]
y=[]
for k,v in data[1]:
	x_name.append(k)
	y.append(v)
x=range(len(y))
plt.title("推断的topic分布排序")
plt.xlabel("topic")
plt.ylabel("概率")
plt.plot(x,y)
plt.xticks(x,x_name)
for label in plt.gca().xaxis.get_ticklabels():
	label.set_rotation(90)
	label.set_ha('center')
	label.set_color('red')
plt.show()