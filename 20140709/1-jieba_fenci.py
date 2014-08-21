#coding=utf-8  
import jieba  
import sys 
sys.path.append("../") 
jieba.load_userdict("/home/alber/jieba/user_dict.txt")
import jieba.posseg as pseg 
import time  
t1=time.time() 

stopwords = {}.fromkeys([ line.rstrip() for line in open('/home/alber/jieba/stopwords.txt') ])
f1=open("/home/alber/experiment/20140709/sample_result1.txt","r") #读取文本  
txtlist=f1.read().decode('utf-8')
words=pseg.cut(txtlist)  
for w in words: 
	seg=str(w.encode('utf-8'))
	if seg not in stopwords:
		result=str(seg)+" "
		f2=open("/home/alber/experiment/20140709/sample_result10.txt","a")  #将结果保存到另一个文档中  
		f2.write(result)
	
f2.close()  
t2=time.time() 
print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果