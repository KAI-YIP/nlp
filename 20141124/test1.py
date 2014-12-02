#coding=UTF-8
f1=open("./名词词频统计.txt",'r')
f2=open("./名词的余弦相似度.txt",'r')
count=0
noun_list=[]
for line in f1.readlines():
    if count<=19:
        line_clean=line.split()
        noun_list.append(line_clean[0])
        count+=1
    else:
        pass
f3=open("./top20名词余弦相似度.txt",'w')
for line in f2.readlines():
    line_clean=line.split()
    if line_clean[0] in noun_list or line_clean[1] in noun_list:
        f3.write(line)