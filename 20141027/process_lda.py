#coding=utf-8
import sys
import numpy
import matplotlib.pyplot as plt

class lda:
	"""对topic进行再处理和清洗，构造新的主题空间"""
	
	def openfile(open_trace="./lda/iphone5s_lda.txt"):
		"""打开lda模型，并建立topic字典"""
		
		f=open(open_trace,'r')
		topic_dict={}     
		for line in f.readlines():
			if len(line)>=3:
				if line[0]!="	":
					word_list=[]
					line_clean=line.split()
					name_key=line_clean[0]+str(line_clean[1][:-3])
				else:
					line_clean=line.split()
					value=tuple(line_clean)
					word_list.append(value)
					topic_dict[name_key]=word_list
			else:
				pass
		return topic_dict

	def topic_del_word (topic_dict):
		"""依据概率对词进行筛选，去掉topic尾部的词"""
		
		def del_word(del_wordlist):
			"""倒序差分,取第一个拐点"""
			word=[]
			prob=[]
			word_list=del_wordlist[::-1]
			for line in word_list:
				word.append(line[0])
				prob.append(line[1])
			first_diffrence=[]
			for count in range(len(prob)):
				if count==0:
					first_diffrence.append(0)
					count+=1
				else:
					first_diffrence.append(float(prob[count])-float(prob[count-1]))
			for i in range(len(first_diffrence)):
				if i!=0: 
					if i<len(first_diffrence)-1:
						if first_diffrence[i]>first_diffrence[i-1] and first_diffrence[i]>first_diffrence[i+1]:
							positon=i
							break
					else:
						positon=i
			new_wordlist=word_list[i:]
			return new_wordlist
		new_topic_dict={}	
		for key in topic_dict:
			word_list=topic_dict[key]
			new_wordlist=del_word(word_list)
			new_topic_dict[key]=new_wordlist[::-1]
		return new_topic_dict

	def word_choose(word_choose_topic_dict):
		"""将topic抽取为名词，依据概率选择top名词作为该topic下的主要特征"""
		new_dict={}
		for key in word_choose_topic_dict:
			wordlist=[]
			for w,p in word_choose_topic_dict[key]:
				wordlist.append(w)
			wordstr=" ".join(wordlist)
			words=pseg.cut(wordstr)
			new_words=[]
			for w in words:
				if "n" in w.flag or "eng" in w.flag or "user" in w.flag or "m" in w.flag:
					new_words.append(w.word)
			new_dict[key]=new_words
		return new_dict

	def TopicCluster(TopicCluster_dict):
		"""计算topic两两之间的相似度，并输出为csv数据，方便做图"""

		def Samilarity1(samilar_list1,samilar_list2):
			"""计算两列表(列表的项为元组)的相似度(概率值相加)，并返回相似度"""
			samilar_dict1={}
			samilar_dict2={}
			common_key=[]
			dict1_prop=0
			dict2_prop=0
			for itern1 in samilar_list1:
				samilar_dict1[itern1[0]]=float(itern1[1])
				dict1_prop+=float(itern1[1])
			for itern2 in samilar_list2:
				samilar_dict2[itern2[0]]=float(itern2[1])
				dict2_prop+=float(itern2[1])
			common_pro=0
			for key in samilar_dict2:
				if key in samilar_dict1:
					common_pro+=float(samilar_dict1[key]+samilar_dict2[key])
					common_key.append(key)
			if common_pro!=0:
				samilarity_value=common_pro/(dict1_prop+dict2_prop)
			else:
				samilarity_value=0
			return samilarity_value,common_key

		def Samilarity2(samilar_list1,samilar_list2):
			"""计算余弦相似度(取topic前30词计算)"""
			samilar_dict1={}
			samilar_dict2={}
			dict1_prop=0
			dict2_prop=0
			if len(samilar_list1)<=30 and len(samilar_list2)<=30:
				for itern1 in samilar_list1[:30]:
					samilar_dict1[itern1[0]]=float(itern1[1])
					dict1_prop+=numpy.square(float(itern1[1]))
				for itern2 in samilar_list2[:30]:
					samilar_dict2[itern2[0]]=float(itern2[1])
					dict2_prop+=numpy.square(float(itern2[1]))
			else:
				position=min([len(samilar_list1),len(samilar_list2)])
				for itern1 in samilar_list1[:position]:
					samilar_dict1[itern1[0]]=float(itern1[1])
					dict1_prop+=numpy.square(float(itern1[1]))
				for itern2 in samilar_list2[:position]:
					samilar_dict2[itern2[0]]=float(itern2[1])
					dict2_prop+=numpy.square(float(itern2[1]))
			denominator=numpy.sqrt(dict1_prop)*numpy.sqrt(dict2_prop)
			common_key=[]
			common_pro=0
			for key in samilar_dict1:
				if key in samilar_dict2:
					common_pro+=float(samilar_dict1[key]*samilar_dict2[key])
					common_key.append(key)
			if common_pro!=0:
				samilarity_value=common_pro/denominator
			else:
				samilarity_value=0
			return samilarity_value,common_key			

		coralation=[]
		cora_dict={}
		common_dict={}
		for key1 in TopicCluster_dict:
			for key2 in TopicCluster_dict:
				if key1!=key2 and set([key1,key2]) not in coralation:
					coralation.append(set([key1,key2]))
					Samilarity_key,common_key=Samilarity2(TopicCluster_dict[key1],TopicCluster_dict[key2])        #选择相似度的度量方式
					cora_dict[tuple([key1,key2])]=Samilarity_key
					common_dict[tuple([key1,key2])]=common_key
		return cora_dict,common_dict

	def list2str(list2str_list):
		"""将list转换成空格隔开的字符串"""
		list_str=" ".join(list2str_list)
		return list_str

	def savefile(save_dict,save_trace="./lda/iphone5slda2.txt"):
		"""将topic字典文件存入txt"""
		f=open(save_trace,'a')
		for key in save_dict:
			f.write(key+"\n")
			for word in save_dict[key]:
				f.write("  "+word[0]+"  "+str(word[1])+"\n")

	def sortedTopic(sortedTopic_tuple):
		"""根据相似度对topic进行排序(相似度和除以相似topic数量)"""
		
		def tuple2dict():
			"""将元组字典转换为单topic数组"""
			topic_list=[]
			topic_name_list=[]
			for k,v in sortedTopic_tuple:
				temp_list1=[k[0],v]
				topic_list.append(temp_list1)
				temp_list2=[k[1],v]
				topic_list.append(temp_list2)
				if k[0] not in topic_name_list:
					topic_name_list.append(k[0])
				if k[1] not in topic_name_list:
					topic_name_list.append(k[1])
			return topic_name_list,topic_list
		
		name_list,topic_list=tuple2dict()
		topic_dict={}
		for name in name_list:
			count=0
			temp_correlation=0
			for itern in topic_list:
				if name==itern[0]:
					count+=1
					temp_correlation+=float(itern[1])
			topic_dict[name]=temp_correlation/count
		return topic_dict

	def topicHconfirm(topic_confirm_dict,topic_h_trace='./correlation/topic-h.txt'):
		"""通过层次划分，对第一层topic建立联系和区别"""
		f=open(topic_h_trace,'r')
		topic_hierarchy=[]
		for line in f.readlines():
			line_clean=line.split()
			topic_hierarchy.append(line_clean)
		A_hierarchy={}
		topic_list=topic_hierarchy[1]
		for topic1 in topic_list:
			for topic2 in topic_list:
				if topic1!=topic2:
					topic_key=tuple([topic1,topic2])
					if topic_key in topic_confirm_dict:
						A_hierarchy[topic_key]=topic_confirm_dict[topic_key]
					else:
						pass
				else:
					pass
		return A_hierarchy


if __name__ =='__main__':
	topic_dict=lda.openfile("./data/lda.txt")
	#new_topic_dict=lda.topic_del_word(topic_dict)      #倒序差分，删除部分词
	#lda.savefile(new_topic_dict,)
	cora_dict,common_dict=lda.TopicCluster(topic_dict)
	sortedTopic_tuple=sorted(cora_dict.items(),key=lambda d:d[1],reverse=True)
	f=open("./correlation.txt",'a')
	for key,v in sortedTopic_tuple:
		f.write(key[0]+" "+key[1]+" "+str(v)+'\n')
