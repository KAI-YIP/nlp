#coding=utf-8

class lda:
	"""主题两两之间的相似，并输出"""

	def f_open_file(file_trace="./lda/tplink/model-1.txt",word_number=10):
		"""打开模型并保存为字典"""
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

if __name__ == '__main__':
	f2=open('./tplink.csv','a')
	f3=open('./tplink.txt','a')
	topic_dict,topic_unpro_dict=lda.f_open_file()
	samilar_dict={}
	edge_list=[]
	for key1 in topic_unpro_dict:
		for key2 in topic_unpro_dict:
			temp_list=set([key1,key2])
			if key1!=key2 and temp_list not in edge_list:
				edge_list.append(temp_list)
				samilarity=len(set(topic_unpro_dict[key1])&set(topic_unpro_dict[key2]))
				samilar_dict[tuple(temp_list)]=samilarity
	new_samilar_dict=sorted(samilar_dict.items(),key=lambda d:d[1],reverse=True)
	for k,v in new_samilar_dict:
		f3.write(str(k[0][6:-3])+","+str(k[1][6:-3])+" "+str(v)+"\n")



