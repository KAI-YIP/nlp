#coding=utf-8

f1=open("/home/alber/NLP/20140814/jd_comment/tplink_result1.txt",'r+')
f2=open("/home/alber/NLP/20140814/jd_comment/tplink_result2.txt","a")
txt=f1.readlines()
f1.close()
list1=[]
for line in txt:
	if len(line)>=4:
		line_clean=" ".join(line.split())
		lines=line_clean+" "+"\n"
		f2.write(lines)
	else:
		pass
f2.close()