#coding=utf-8 
import sys 
import matplotlib.pyplot as plt


class lda:
	"""对topic进行再处理和清洗，构造新的主题空间"""
	
	def openfile(open_trace="./iphone5slda.txt"):
		"""打开lda模型，并建立topic字典"""
		
		f=open(open_trace,'r')
		topic_dict={}      
		for line in f.readlines():
			if line[0]!="	":
				word_list=[]
				line_clean=line.split()
				name_key=line_clean[0]+str(line_clean[1][:-3])
			else:
				line_clean=line.split()
				value=tuple(line_clean)
				word_list.append(value)
				topic_dict[name_key]=word_list
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



	def savefile(save_dict,save_trace="./iphone5slda2.txt"):
		"""将topic字典文件存入txt"""
		f=open(save_trace,'a')
		for key in save_dict:
			f.write(key+"\n")
			for word in save_dict[key]:
				f.write("  "+word[0]+"  "+str(word[1])+"\n")



	
if __name__ =='__main__':
	topic_dict=lda.openfile()
	wordtuple=topic_dict["Topic0"]
	y=[]
	for k,v in wordtuple:
		y.append(float(v))
	total=[]
	for i in range(len(y)):
		if i==0:
			total.append(sum(y))
		elif i<len(y)-1:
			sum_no=sum(y[:-i])
			total.append(sum_no)
	x=range(len(total))
	plt.plot(x,total)
	plt.xticks(x,x)
	plt.show()