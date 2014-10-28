#coding=utf-8
import jieba  
import sys 
sys.path.append("../") 
jieba.load_userdict("/home/alber/jieba/user_dict.txt")	#用户词表位置
import jieba.posseg as pseg 
import time
import numpy as np
import matplotlib.pylab as plt


class TextProcess:
	"""对文本数据进行预处理，包括，分词，词性筛选，去高频形容词，按标点分句"""
	
	def wordseg(wordseg_trace="./data.txt"):
		"""分词，返回分好词，且带词性标记的数组"""
		f1=open(wordseg_trace,"r")
		txtlist=f1.readlines()
		f1.close()
		new_txt=[]
		for line in txtlist:
			line_cut=list(pseg.cut(line))#调用jieba分词
			for w in line_cut:
				temp_list=[]
				temp_list.append(w.word)
				temp_list.append(w.flag)
				new_txt.append(temp_list)
		return new_txt
	
	def stopwordRM(stopwords_array):
		"""去除听用词"""
		new_txt=[]
		stopwords = {}.fromkeys([ line.rstrip() for line in open('/home/alber/jieba/stopwords.txt') ])    #听用词表位置
		for word in stopwords_array:
			if word[0] not in stopwords:
				new_txt.append(word)
			else:
				pass
		return new_txt

	def wordfilter(wordfilter_array,wordfilter_list=["x","zg","uj","ul","e","/d","uz","y"]):
		"""去除不需要的词性"""
		new_txt=[]
		for word in wordfilter_array:
			if word[0]=="\n":
				new_txt.append(word)
			else:
				if word[1] not in wordfilter_list:
					new_txt.append(word)
				else:
					pass
		return new_txt

	def adjfilter(adjfilter_array):
		"""去除词频最高的几个形容词(地一个拐点前)"""
		new_txt=[]
		wordlist=[]
		frequency={}
		for word in adjfilter_array:
			if word[1]=="a":
				if word[0] not in wordlist:
					wordlist.append(word[0])
					frequency[word[0]]=1
				else:
					frequency[word[0]]+=1
			else:
				pass
		sorted_frequency=sorted(frequency.items(),key=lambda d:d[1],reverse=True)
		count=0
		for k,v in sorted_frequency:
			if count<=10:
				print (k,v)
				count+=1

	def santencebreak(santencebreak_array,santencebreak_punctuation=['，','。','！','？',',','.','!','?']):
		"""将标点符号替换为换行符"""
		new_txt=[]
		for word in santencebreak_array:
			temp_list=[]
			if word[0] in santencebreak_punctuation:
				temp_list.append("\n")
				temp_list.append(word[1])
			else:
				temp_list=word
			new_txt.append(temp_list)
		return new_txt

	def array2str(array2str_array):
		"""将处理完成的数组，变为新的数组，换行符作为数组中列表的分割点"""
		new_txt1=[]
		new_txt=[]
		temp_list=[]
		for word in array2str_array:
			if word[0]!="\n":
				temp_list.append(word[0])
			else:
				new_txt1.append(temp_list)
				temp_list=[]
		for value in new_txt1:				
			if len(value)>1:                             #删除单字符的项
				new_txt.append(value)
			else:
				pass
		return new_txt

	def savearray(savearray_array,savearray_trace):
		"""将任何一步的结果进行保存"""
		f=open(savearray_trace,'a')
		for word in savearray_array:
			f.write(str(word[0])+"/"+str(word[1]+" "))
		f.close()		
			
	def savefile(savefile_array,savefile_trace='./data_result.txt'):
		"""保存txt"""
		f=open(savefile_trace,'a')
		for word in savefile_array:
			for w in word:
				f.write(w+" ")
			f.write("\n")


if __name__=='__main__':
	txt1=TextProcess.wordseg("./iphone5s.txt")   #分词    参数为要处理的文本
#	txt2=TextProcess.santencebreak(txt1,)        #按标点分句
	txt3=TextProcess.stopwordRM(txt1)			#去停用词
	txt4=TextProcess.wordfilter(txt3,)			#过滤词性
	txt5=TextProcess.array2str(txt4)				#数组转化为无词性的数组
	TextProcess.savefile(txt5,"./iphone5s_result.txt")　#括号中参数为保存的文本路径