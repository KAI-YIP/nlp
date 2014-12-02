#coding=utf-8
import matplotlib.pylab as plt

f=open("./data.txt",'r')
word_dict={}
for line in f.readlines():
    line_clean=line.split()
    for word in line_clean:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
tf=sorted(word_dict.items(),key=lambda d:d[1],reverse=True)
h=open("./词频统计.txt",'w')
for k,v in tf:
    h.write(str(k)+" "+str(v)+"\n")
h.close()
count=0
x_name=[]
y=[]
for k,v in tf:
    if count<=20:
        x_name.append(k)
        y.append(v)
        count+=1
    else:
        break
x=range(len(y))
plt.title("词频统计图")
plt.xlabel("词/词频排序")
plt.ylabel("词频")
plt.plot(x,y,color='green')
plt.xticks(x,x_name)
for label in plt.gca().xaxis.get_ticklabels():
    label.set_rotation(90)
    label.set_ha("center")
    label.set_color("red")
plt.show()
h=open("./名词词频统计.txt",'w')
for k,v in tf:
    if "/n" in k:
        h.write(str(k)+" "+str(v)+"\n")
h.close()
count=0
x_name=[]
y=[]
for k,v in tf:
    if "/n" in k:
        if count<=20:
            x_name.append(k)
            y.append(v)
            count+=1
        else:
            break
    else:
        pass
x=range(len(y))
plt.title("名词词频统计图")
plt.xlabel("词/词频排序")
plt.ylabel("词频")
plt.plot(x,y,color='green')
plt.xticks(x,x_name)
for label in plt.gca().xaxis.get_ticklabels():
    label.set_rotation(90)
    label.set_ha("center")
    label.set_color("red")
plt.show()