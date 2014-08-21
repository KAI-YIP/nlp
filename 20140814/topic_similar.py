# -*- coding: UTF-8-*-
from os import listdir

class LdaTopicSimilar:
	"""基于lda计算出的多个模型进行主题稳定性的晒选"""
	def f_file_namelist(name_index="./lda/iphone5s/diff-sampling/"):
		"""获取某目录下所有文件"""
		file_list=listdir(name_index)
		filelist=[]
		for name in file_list:
			trace=name_index+name
			filelist.append(trace)
		return filelist

	def f_open_file(file_trace,word_number=100):
		"""将lda主题-词文本存储为不计概率值的字典,topic_dict为带概率的字典，topic_unpro_dict为不带概率的字典"""
		f=open(file_trace,'r')	
		count=0
		txt=f.readlines()
		f.close()
		topic_dict={}
		topic_unpro_dict={}
		word=[]
		word_value=[]
		for line in txt:
			if "Topic" in line:
				name=line[:-1]
			else:
				line_list=line.split()
				word.append(line_list[0])
				line_clean=" ".join(line_list)
				word_value.append(line_clean)

			if count==word_number:
				topic_dict[name]=word_value
				topic_unpro_dict[name]=word
				count=0
				word=[]
				word_value=[]
			else:
				count+=1
		return topic_dict,topic_unpro_dict

	def f_topic_samilarity(topic_samilarity_dict1,topic_samilarity_dict2):
		"""在字典一中找字典二中最相似的键，返回｛topic:最大相似度}字典"""
		eachkey_len_intersection={}
		for key1 in topic_samilarity_dict1:
			len_intersection=[]
			for key2 in topic_samilarity_dict2:
				lenth=len(set(topic_samilarity_dict1[key1])&set(topic_samilarity_dict2[key2]))
				len_intersection.append(lenth)
				max_samilar=max(len_intersection)
			eachkey_len_intersection[key1]=max_samilar                    
		return eachkey_len_intersection

if __name__ == '__main__':
	b=2
	filelist=LdaTopicSimilar.f_file_namelist("./lda/tplink/diff-sampling/")
	topic_dict_list=[]
	topic_samilarity_lenth_dict={}
	for filetrace in filelist:
		topic_dict,topic_unpro_dict=LdaTopicSimilar.f_open_file(filetrace,50)
		topic_dict_list.append(topic_unpro_dict)
	for topic in topic_dict_list:
		if topic!=topic_dict_list[b]:                                                        #第一组实验作为初始组进行计算
			topic_samilarity_dict=LdaTopicSimilar.f_topic_samilarity(topic_dict_list[b],topic)
		for key in topic_dict_list[b]:
			if key in topic_samilarity_lenth_dict:
				topic_samilarity_lenth_dict[key].append(topic_samilarity_dict[key])
			else:
				topic_samilarity_lenth_dict[key]=[]
				topic_samilarity_lenth_dict[key].append(topic_samilarity_dict[key])
	f=open("./lda/tplink/filter/result"+str(b+1)+"B.txt",'a')
	for key in topic_samilarity_lenth_dict:
		f.write(key)
		for word in topic_samilarity_lenth_dict[key]:
			f.write(str(word)+" ")
		f.write("\n")


