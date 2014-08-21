#coding=utf-8
import os
import sys
import re
import matplotlib.pylab as plt

f1=open("/home/alber/experiment/20140719/dell_result1.txt",'r')
txt=f1.readlines()
lenth_count=[]
count1=0
wordlist=[]
for line in txt:
	count2=0
	line_list=line.split()
	for word in line_list:
		if word not in wordlist:
			wordlist.append(word)
			count2+=1
		else:
			pass
	count1+=count2
	lenth_count.append(count1)
plt.plot(lenth_count)
plt.show()
