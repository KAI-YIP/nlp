# -*- coding: UTF-8-*-

f1=open("/home/alber/nlp/20140814/lda/iphone5s/diff-topic/model-40.txt",'r')
f2=open("/home/alber/nlp/20140822/model-40.txt",'a')
for line in f1.readlines():
	if "Topic" in line:
		f2.write("\n")
	else:
		line_clean=line.split()
		f2.write(line_clean[0]+" ")
f1.close()
f2.close()