#coding=utf-8
import matplotlib.pylab as plt

test_list=["价","价格","便宜","贵"]
f=open('./iphone5s.txt','r')
y=[]
count=0
for line in f.readlines():
	line_clean=line.split()
	if "价格" in line_clean:
		count+=1
	else:
		pass
	y.append(count)
plt.plot(y)
plt.show()