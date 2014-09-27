#coding=utf-8
import matplotlib.pyplot as plt

f=open("./rongyao3c_seg2.txt",'r')
word_dict={}
for line in f.readlines():
	line_clean=line.split()
	for word in line_clean:
		if word not in word_dict:
			word_dict[word]=1
		else:
			word_dict[word]+=1
word_sorted=sorted(word_dict.items(),key=lambda d:d[1],reverse=True)
f2=open("./wordfrequency.txt",'a')
for key,value in word_sorted:
	f2.write(key+" "+str(value)+"\n")