#coding=utf-8
import matplotlib.pylab as plt


f=open("/home/alber/experiment/20140720/label_stastic.txt",'r')
txt=f.readlines()
f.close()
label_dict={}
for line in txt:
	line_clean=line.split()
	label_dict[line_clean[0]]=line_clean[1]
label_frequency=sorted(label_dict.items(), key=lambda d: d[1],reverse=True)
print (label_frequency)

x=[]
y=[]
for key,value in label_frequency:
	x.append(key)
	y.append(value)
plt.plot(y)
plt.show()

print(sum(y))