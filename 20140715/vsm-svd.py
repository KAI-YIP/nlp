#coding=utf-8
import re
import math
import numpy as np
import matplotlib.pylab as plt

def f_file_open(trace_string):
	"""open the document_set, save in the list called txt"""
	f=open(trace_string,'r')
	txt=f.readlines()
	f.close()
	return txt

def f_vector_found(txt):
	"""calculate all of the word in the document set---构造词空间"""
	word_list=[]
	for line in txt:
		line_clean=line.split()
		for word in line_clean:
			if word not in word_list:
				word_list.append(word)
			else:
				pass
	return word_list

def f_IDF_word(calculate_word,whole_txt):
	"""calculate the TF of each word in document,计算每一个词的TF-IDF值"""
	Num_document=0
	Num_document_has_word=0
	for line in whole_txt:
		Num_document+=1
		if calculate_word in line:
			Num_document_has_word+=1
	idf_value=float(Num_document_has_word)/Num_document
	return idf_value


def f_document_vector(document,word_list,f_IDF_word):
	"""transform the document to vector---文档向量化TF-IDF"""
	vector=[]
	document_clean=document.split()
	for word in word_list:
		a=document_clean.count(word)
		TF=float(a/len(document_clean))
		b=f_IDF_word(word,txt)
		TF_IDF=a*b
		vector.append(TF_IDF)
	return vector

def f_svd_calculate(document_array):
	"""calculate the svd and return the three matrics"""
	U,S,V=np.linalg.svd(document_array)
	return (U,S,V)

def f_process_matric_U(matric_U,Save_N_Singular_value):
	"""according to the matric U, choose the words as the feature in each document,根据前N个奇异值对U进行切分,选择前N列""" 
	document_matric_U=[]
	for line in matric_U:
		line_new=line[:Save_N_Singular_value]
		document_matric_U.append(line_new)
	return document_matric_U

def f_process_matric_S(matric_S,Save_information_value):
	"""choose the items with large singular value,根据保留信息需求选择奇异值个数"""
	matricS_new=[]
	S_self=0
	N_count=0
	Threshold=sum(matric_S)*float(Save_information_value)
	for value in matric_S:
		if S_self<=Threshold:
			matricS_new.append(value)
			S_self+=value
			N_count+=1
		else:
			break
	print ("the %d largest singular values keep the %s information " %(N_count,Save_information_value))
	return (N_count,matricS_new)

def f_process_matric_V(matric_V,Save_N_Singular_value):
	"""according to the matric V, choose the words as the feature in each document,根据前N个奇异值对U进行切分,选择前N行"""
	document_matric_V=matric_V[:Save_N_Singular_value]
	return document_matric_V

def f_combine_U_S_V(matric_u,matric_s,matirc_v):
	"""calculate the new document对奇异值筛选后重新计算文档矩阵"""
	
	new_document_matric=np.dot(np.dot(matric_u,np.diag(matric_s)),matirc_v)
	return new_document_matric

def f_matric_to_document(document_matric,word_list_self):
	"""transform the matric to document,将矩阵转换为文档"""
	new_document=[]
	for line in document_matric:
		count=0
		for word in line:
			if float(word)>=0.02:                                                                                     #转换后文档中词选择的阈值
				new_document.append(word_list_self[count]+" ")
			else:
				pass
			count+=1
		new_document.append("\n")
	return new_document


def f_save_file(trace,document):
	f=open(trace,'a')
	for line in document:
		for word in line:
			f.write(word)

trace_open="/home/alber/experiment/test.txt"
trace_save="/home/alber/experiment/20140715/svd_result2.txt"
txt=f_file_open(trace_open)
word_vector=f_vector_found(txt)
print (len(word_vector))

document=[]
Num_line=0
for line in txt:								#transform the document set to matric
	Num_line=Num_line+1
	document_vector=f_document_vector(line,word_vector,f_IDF_word)
	document.append(document_vector)
print (len(document))
U,S,V=f_svd_calculate(document)
print (sum(S))
N_count,document_matric_S=f_process_matric_S(S,0.6)
document_matric_U=f_process_matric_U(U,N_count)
document_matric_V=f_process_matric_V(V,N_count)
document_matric=f_combine_U_S_V(document_matric_U,document_matric_S,document_matric_V)
print (len(document_matric[1]))
print (len(document_matric))
print (sorted(document_matric[3],reverse=True))
plt.plot(sorted(document_matric[7],reverse=True))
plt.show()
new_document=f_matric_to_document(document_matric,word_vector)
f_save_file(trace_save,new_document)
print ("the new document has been saved in %s"%trace_save)
