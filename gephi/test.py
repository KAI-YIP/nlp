#coding=utf-8

f=open("/home/alber/experiment/gephi/test.txt",'r')
txt=f.readlines()
f.close()
f2=open("/home/alber/experiment/gephi/test_result.txt",'a')
f2.write("edge"+","+"link"+"\n")
count=0
for line in txt:
	count+=1
	f2.write(str(count)+",")
	f2.write((" ".join(line.split())))
	f2.write("\n")
