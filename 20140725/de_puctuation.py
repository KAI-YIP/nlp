# coding=utf-8
import sys
import os

def f_open_file(trace_open):
	"""打开目标文件"""
	f=open(trace_open,'r')
	txt=[]
	for line in f.readlines():
		line_list=line.split()
		txt.append(line_list)

	return txt

def f_punctuation_match(txt_con_puctuation):
	"""按标点符号换行"""
	puctuation=[",",".","。","，","!","?"]
	txt=[]
	for line in txt_con_puctuation:
		for word in line:
			if word in puctuation:
				txt.append("\n")
			else:
				txt.append(word)
	return txt

def f_save_file(trace_save,target_txt):
	"""保存文件"""
	f=open(trace_save,'a')
	for word in target_txt:
		f.write(word)

trace_open="/home/alber/experiment/20140725/sample_fenci.txt"
trace_save="/home/alber/experiment/20140725/sample_new.txt"
txt=f_punctuation_match(f_open_file(trace_open))
f_save_file(trace_save,f_punctuation_match(txt))


