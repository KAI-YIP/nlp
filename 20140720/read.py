#coding=utf-8

f1=open("/home/alber/experiment/train",'r')
f2=open("/home/alber/experiment/label_stastic.txt",'a')
dict_label={}
print ("start")
for line in f1:
	if len(line)>=2:
		line_new=line[6:]
		line_list=line_new.split()
		label=line_list[0]
		name=label
		if name in dict_label:
			dict_label[name]+=1
		else:
			dict_label[name]=1
for key in dict_label:
	string=key+" "+str(dict_label[key])+"\n"
	f2.write(string)
print ("finished")