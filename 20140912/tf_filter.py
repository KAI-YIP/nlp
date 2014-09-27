# -*- coding: UTF-8-*-
import matplotlib.pyplot as plt

f1=open("/home/alber/nlp/20140827/tplink/h-cluster/相似度阈值0.12/test_result3.txt",'r')
f2=open("./tf_filter_result3.txt",'a')
for line in f1.readlines():
	line_clean=line.split()
	line_new=line_clean[1:]
	word_dict={}
	for word in line_new:
		if word not in word_dict:
			word_dict[word]=1
		else:
			word_dict[word]+=1
	new_word_dict=sorted(word_dict.items(),key=lambda d:d[1],reverse=True)
	for key,value in new_word_dict:
		f2.write(str(key)+str(value)+" ")
	f2.write("\n")