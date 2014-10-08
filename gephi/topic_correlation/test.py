#coding=utf-8

f1=open("./correlation.csv",'r')
f0=open("./node.csv",'a')
f2=open("./edge.csv",'a')
f3=open("./weight.csv",'a')
node=[]
for line in f1.readlines():
	line_clean=line.split()
	if line_clean[0] not in node:
		node.append(line_clean[0])
	else:
		pass
	f2.write(line_clean[0]+" "+line_clean[1]+"\n")
	f3.write(line_clean[2]+"\n")
for nod in node:
	f0.write(nod+"\n")
