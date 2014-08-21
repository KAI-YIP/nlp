# -*- coding: UTF-8-*-
import matplotlib.pyplot as plt

f=open("./test.txt",'r')
x_label=[]
y=[]
for line in f.readlines():
	line_clean=line.split()
	x_label.append(line_clean[0])
	y.append(line_clean[1])
x=range(len(y))
plt.title("词－概率折线图",color="black")
plt.xlabel("主题下的词")
plt.ylabel("词的概率")
plt.plot(x,y,'--',label="主题",color='red')
plt.xticks(x,x_label)
for label in plt.gca().xaxis.get_ticklabels(): 
	label.set_rotation(45)
	label.set_ha('center')
	label.set_color('black')
plt.legend()
plt.show()