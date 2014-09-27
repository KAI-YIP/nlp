# -*- coding: UTF-8-*-
import matplotlib.pyplot as plt

f=open("./test_result0.txt",'r')
word_dict={}
for line in f.readlines():
	line_clean=line.split()
	line_new=line_clean[1:]
	for word in line_new:
		if word in word_dict:
			word_dict[word]+=1
		else:
			word_dict[word]=1
print (len(word_dict))
new_word_list=sorted(word_dict.items(), key=lambda d:d[1], reverse = True)
x_word=[]
y=[]
f2=open("./test.txt",'a')
for k,v in new_word_list:
	x_word.append(k)
	f2.write(str(k)+",")
	y.append(v)
	f2.write(str(v)+"\n")
x=range(len(y))
plt.plot(x,y)
plt.title("词频统计")
plt.xlabel("word")
plt.ylabel("frequency")
plt.xticks(x,x_word)
for label in plt.gca().xaxis.get_ticklabels(): 
     label.set_rotation(45)
     label.set_ha('center')
     label.set_color('red')
plt.show()
