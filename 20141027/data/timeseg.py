#coding=utf-8

class data:
	"""数据读取，存为数组,按时间取数据"""
	def readdata(readdata_trace="./iphone5s.txt"):
		"""读取数据存为数组[[会员账号,会员等级,地址,星数,购买日期,评价日期,有用,回复,心得][]...]"""
		data=[]
		f=open(readdata_trace,'r')
		for line in f.readlines():
			line_new=line[:-1]
			line_clean=line_new.split("	")
			if len(line_clean)>=4:
				data.append(line_clean)
		return data

	def timeseg(timeseg_str1,timeseg_str2="2014-01-01"):
		"""时间格式转换"""
		time0=timeseg_str2.split("-")
		time1=timeseg_str1.split("-")
		time_diff=365*(int(time1[0])-int(time0[0]))+30*(int(time1[1])-int(time0[1]))+(int(time1[2])-int(time0[2]))
		return time_diff


if __name__=='__main__':
	comment=data.readdata()
	comment_new={}
	for line in comment:
		line4_clean=line[4].split("-")
		if len(line4_clean)==3:
			if int(line4_clean[2])>=15:
				name=str(line4_clean[1])+"0"
			else:
				name=str(line4_clean[1])+"1"
			if name not in comment_new:
				comment_new[name]="."+line[8]
			else:
				comment_new[name]+="."+line[8]
		else:
			pass
	f2=open("./timeseg.txt",'a')
	for key in sorted(comment_new.keys()):
		f2.write(comment_new[key]+"\n")
	