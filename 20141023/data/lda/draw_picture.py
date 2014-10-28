#coding=utf-8
import matplotlib.pylab as plt

f=open("./inference.txt",'r')
data=[]
for line in f.readlines():
	temp_list=[]
	line_clean=line.split()
	for one in line_clean:
		temp_list.append(float(one))
	data.append(temp_list)
plt.title("两评论间的差异")
plt.ylabel("概率值")
plt.xlabel("主题序列")
plt.plot(data[0],"r",label="$iphone5s$")
plt.plot(data[1],"g",label="$rongyao3C$")
plt.legend()
plt.show()
