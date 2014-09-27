#coding=utf-8  
import jieba  
import sys 
sys.path.append("../") 
jieba.load_userdict("/home/alber/jieba/user_dict.txt")
import jieba.posseg as pseg 
import time  
t1=time.time() 

stopwords = {}.fromkeys([ line.rstrip() for line in open('/home/alber/jieba/stopwords.txt')])
puntuation={}.fromkeys([ line.rstrip() for line in open('/home/alber/jieba/puntuation.txt')])
frequency={}.fromkeys([ line.rstrip() for line in open('/home/alber/jieba/frequency.txt')])
f1=open("./iphone5s.txt","r") #读取文本  
txtlist=f1.readlines()
f1.close()
f2=open("./iphone5s_seg1.txt",'a')
for line in txtlist:
	line_cut=list(pseg.cut(line))
	for w in line_cut:
		if w.word in puntuation:
			f2.write("\n")
		if w.word not in stopwords and w.word not in frequency:
			f2.write(w.word+" ")
		else:
			pass

t2=time.time() 
print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果