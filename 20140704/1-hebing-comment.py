# -*- coding: UTF-8-*-

index=['app-mac.txt','hp-cq45.txt','lenovo-b490a.txt']
comment=[]
for name in index:
	index_string="/home/alber/experiment/20140704/"+name
	f1=open(index_string,'r')
	each_comment=f1.read()
	comment.append(each_comment)
	f1.close()
f2=open("/home/alber/experiment/20140704/sample.txt",'a')
for line in comment:
	f2.write(line)
f2.close()