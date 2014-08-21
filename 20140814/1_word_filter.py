# -*- coding: utf-8 -*-
from os import listdir
import matplotlib.pyplot as plt
import numpy as np

class LdaWordFilter:
	"""对LDA计算出的主题和主题词进行过滤，去除噪音主题和噪音词"""

	def f_file_namelist(name_index="./lda/"):
		"""获取某目录下所有文件"""
		file_list=listdir(name_index)
		filelist=[]
		for name in file_list:
			trace=name_index+name
			filelist.append(trace)
		return filelist

	def f_open_file(file_trace,word_number=100):
		"""将lda主题-词文本存储为字典"""
		f=open(file_trace,'r')
		count=0
		txt=f.readlines()
		f.close()
		topic_dict={}
		word_value=[]
		for line in txt:
			if "Topic" in line:
				name=line[:-1]
			else:
				line_clean=" ".join(line.split())
				word_value.append(line_clean)
			if count==word_number:
				topic_dict[name]=word_value
				word_value=[]
				count=0
			else:
				count+=1
		return topic_dict


	def f_draw_picture(picture_wordlist,picture_title="word probability of *th Topic"):
		"""根据词-概率字典画概率折线图"""
		x_word=[]
		y=[]
		word_dict={}
		for line in picture_wordlist:
			line_clean=line.split()
			word_dict[line_clean[0]]=line_clean[1]
		sort_word_dict= sorted(word_dict.items(), key=lambda d:d[1], reverse = True)
		for k,v in sort_word_dict:
			x_word.append(k)
			y.append(float(v))
		plt.title(picture_title,color='black')
		plt.xlabel("Word",color='black')
		plt.ylabel("Probability",color='black')
		x=range(len(y))
		plt.plot(x,y,"--",color="red",linewidth=2)
		plt.xticks(x,x_word)
		for label in plt.gca().xaxis.get_ticklabels(): 
			label.set_rotation(90)
			label.set_ha('center')
			label.set_color('black')
		plt.show()

	def f_word_filter(word_prob_dict,prob_threshold):
		"""根据概率阈值过滤掉概率太小的词"""
		new_dict={}
		for key in word_prob_dict:
			new_wordlist=[]
			wordlist=word_prob_dict[key]
			for word in wordlist:
				word_clean=word.split()
				probility=word_clean[1]
				if float(probility)>=float(prob_threshold):
					new_wordlist.append(word)
				else:
					pass
			new_dict[key]=new_wordlist
		return new_dict

	def f_filter_accd_prob(filter_accd_prob_dict):
		"""根据词筛选后主题的长度筛选主题(一阶差分)"""
		Topic=[]
		topic_len=[]
		len_dict={}
		real_topic=[]
		for key in filter_accd_prob_dict:
			len_dict[key]=len(filter_accd_prob_dict[key])
		sort_len_dict=sorted(len_dict.items(),key=lambda d:d[1], reverse = True)
		for k,v in sort_len_dict:
			Topic.append(k)
			topic_len.append(v)
		topic_len_array=np.array(topic_len)
		lenth_diff=np.diff(topic_len_array)
		max_lenth=max(lenth_diff)
		lenth_diff_list=[]
		for i in lenth_diff:
			lenth_diff_list.append(i)
		lenth_diff_list_reverse=lenth_diff_list[::-1]
		position=len(lenth_diff)-lenth_diff_list_reverse.index(max_lenth)
		real_topic=Topic[:position]
		new_dict={}
		for key in filter_accd_prob_dict:
			if key in real_topic:
				new_dict[key]=filter_accd_prob_dict[key]
			else:
				pass
		return real_topic,new_dict

	def f_word_samilarity(f_word_samilarity):
		"""对主题进行相似性处理"""



	def f_save_file(save_file_dict,trace='./new_topic.txt'):
		"""把处理后的主题模型，即主题-词矩阵保存为文本"""
		f=open(trace,'a')
		for key in save_file_dict:
			f.write(key+"....")
			for word in save_file_dict[key]:
				word_clean=word.split()
				f.write(word_clean[0]+" ")
			f.write("\n"+"\n")
		f.close()

if __name__ == '__main__':
	b=3
	trace="./lda/tplink/diff-sampling/model-"+str(b)+".txt"		#主题－词模型位置
	topic_dict=LdaWordFilter.f_open_file(trace,50)	#将模型存入字典
	new_dict=LdaWordFilter.f_word_filter(topic_dict,0.002)				 #根据概率阈值对词进行过滤，得到新的主题-词字典
	real_topic,choose_dict=LdaWordFilter.f_filter_accd_prob(new_dict)	#根据长度对主题进行一阶差分，找到长主题(real_topic差分后留下的主题,choose_dict新的主题模型)
	print (len(choose_dict))
	print (len(real_topic))
	LdaWordFilter.f_save_file(choose_dict,"./lda/tplink/filter/result"+str(b)+"A.txt")
