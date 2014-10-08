#coding=utf-8
import matplotlib.pyplot as plt
f1=open("./wordfrequency.txt",'r')
y=[]
xlabel=[]
count=0
for line in f1.readlines():
	if count<=30:
		line_clean=line.split()
		word=line_clean[0].split("/")
		if "a" in word[1] or "d" in word[1]:
			xlabel.append(word[0])
			y.append(line_clean[1])
			count+=1
		else:
			pass
	else:
		break
x=range(len(y))
plt.plot(x,y,"--")
plt.xticks(x,xlabel)
plt.xlabel("word",color='black')
plt.ylabel("frequency")
for label in plt.gca().xaxis.get_ticklabels(): 
     label.set_rotation(90)
     label.set_ha('center')
     label.set_color('black')
plt.show()