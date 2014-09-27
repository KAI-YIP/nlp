#coding=utf-8
import xlrd

class preprocess:
	"""对数据集做预处理，按时间段切分"""
	def readexcel(open_trace="/home/alber/nlp/20140915/data/iphone5s/iphone5s.xlsx",segment_point=4):
		data=xlrd.open_workbook(open_trace)
		table = data.sheets()[0]
		time_list=[]
		count=0
		for i in list(range(table.nrows)):
			temp_list=table.row_values(i)
			time=temp_list[7]
			if count<=10:
					time_list.append(time)
					print (time)
					count+=1
		return time_list[1:]

if __name__=='__main__':
	time_list=preprocess.readexcel()
	print (time_list)
	print (time_list[0]-time_list[1])