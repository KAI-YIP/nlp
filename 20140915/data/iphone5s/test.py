#coding=utf-8

f1=open("./主题-主要名词.txt",'r')
f2=open("./Hir-topic.csv",'a')
for line in f1.readlines():
	line_clean=line.split()
	if len(line_clean)>=2:
		topic1=" ".join([line_clean[1],line_clean[2]])
		topic2=" ".join([line_clean[1],line_clean[3]])
		topic3=" ".join([line_clean[2],line_clean[3]])
		f2.write(topic1+"\n"+topic2+"\n"+topic3+"\n")
	else:
		pass
