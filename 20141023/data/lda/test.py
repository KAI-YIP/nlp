f=open("./inference.txt",'r')
for line in f.readlines():
	a=0
	line_clean=line.split()
	for word in line_clean:
		a+=float(word)
	print (a)