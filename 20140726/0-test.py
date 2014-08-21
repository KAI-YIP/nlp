#coding=utf-8

f=open("/home/alber/experiment/20140726/sample_result3.txt",'r')
f2=open("/home/alber/experiment/20140726/sample_result4.txt",'a')
for line in f.readlines():
	line_list=line.split()
	for word in line_list:
		if word=="hellip":
			pass
		else:
			f2.write(word+" ")
	f2.write("\n")