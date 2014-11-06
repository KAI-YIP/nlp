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
	data.append(topic_dict)
minus={}
for key in data[0]:
	minus[key]=abs(float(data[0][key])-float(data[1][key]))
sorted_minus=sorted(minus.items(),key=lambda d:d[1],reverse=True)
f1=open("./minus.txt",'a')
for k,v in sorted_minus:
	f1.write(k+" "+str(v)+"\n")