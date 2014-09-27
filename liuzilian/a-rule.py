# -*- coding: UTF-8-*-
import xlrd

class AR:
	"""一种改进型的关联规算法，引入item时间，价格，数量属性"""

	def custom_id_found(custom_id_found_data='./data.xlsx'):            #数据集位置
		"""扫描数据库，并建立以事物项为单位的字典，字典包括N个item字典"""
		data=xlrd.open_workbook(custom_id_found_data)
		table = data.sheets()[0]             #获取第一章表，如果要获取第二张表将０改为１
		custom_id={}
		custom_id_naive={}
		custom_name=0
		brought_time=0
		print ("频繁项集词典创建中")
		for i in list(range(table.nrows)):
			if i!=0:
				temp_list=(table.row_values(i))
				if custom_name!=int(temp_list[0]) or brought_time!=temp_list[1]:
					item={}
					item_naive=[]
				custom_name=int(temp_list[0])
				brought_time=temp_list[1]
				product_id=int(temp_list[2])
				product_price=temp_list[3]
				product_quantity=temp_list[4]
				item[product_id]=[product_price,product_quantity]
				item_naive.append(product_id)                          			
				custom_id[tuple([custom_name,brought_time])]=item
				custom_id_naive[tuple([custom_name,brought_time])]=item_naive	
		print ("频繁项集词典创建完成")
		return custom_id,custom_id_naive

	def save_file(save_file_dict,save_trace="./result_set.txt"):
		"""对得到的项集结果进行保存"""
		f=open(save_trace,'a')
		for key in save_file_dict:
			for item in key:
				f.write(str(item)+",")
			f.write(" ")
			for value in save_file_dict[key]:
				f.write(str(value)+" ")
			f.write("\n")

	def naiveAR(AR_custom_dict,naiveAR_custom_dict,support=5):
		"""根据原始的关联规则计算出的2项和3项频繁集，support默认值为0.05输出事物项集"""

		def product_1set(product_1set_list,naiveAR_custom_dict,support):
			"""产生一项频繁集"""
			product_list1=[]
			new_naiveAR_custom_key=[]
			for prop in product_1set_list:
				count=0
				for key in naiveAR_custom_dict:
					if prop in naiveAR_custom_dict[key]:
						count+=1
						if key not in new_naiveAR_custom_key:
							new_naiveAR_custom_key.append(key)             #根据一项频繁集更新事物项字典
					else:
						pass
				if count>=support:
					product_list1.append(prop)
			if len(product_list1)==0:
				print ("一项集数量为０,请重新设定support")
			else:
				print ("原始一项频繁集数量为"+str(len(product_list1)))
				return product_list1,new_naiveAR_custom_key

		def product_2set(product_2set_1set,product_2set_custom_key,support):
			"""基于一项频繁集，产生二项频繁集"""
			new_naiveAR_custom_key=[]
			product_list=[]
			product_2set_list=[]
			total_set_lenth=len(naiveAR_custom_dict)
			for good1 in product_2set_1set:
				for good2 in product_2set_1set:
					if good1!=good2 and [good1,good2] not in product_list:
						product_list.append([good2,good1])			                          #产生备选二项集
			for good in product_list:
				count=0
				for key in product_2set_custom_key:
					if set(good)<=set(naiveAR_custom_dict[key]):
						count+=1
						if key not in new_naiveAR_custom_key:
							new_naiveAR_custom_key.append(key)          #根据二项频繁集更新事物项列表
					else:
						pass
				if count>=support:
					product_2set_list.append(good)										#对备选二项集进行筛选
				else: 
					pass                                                                          
			if len(product_2set_list)==0:
				print ("二项集数量为０,请重新设定support")
				return ["项集数量为０"]
			else:
				print ("原始二项频繁集数量为"+str(len(product_2set_list)))
				return product_2set_list,new_naiveAR_custom_key

		def product_3set(product_3set_1set,product_3set_2set,product_3set_custom_key,support):
			"""根据二项集和一项集产生三项集并筛选，输出原始三项集"""
			product_3set=[]
			product_list=[]
			new_naiveAR_custom_key=[]
			for good in product_3set_2set:
				for prod in product_3set_1set:
					new_good=set(good+[prod])
					if len(new_good)==3 and new_good not in product_3set:
						product_3set.append(new_good)
			for good in product_3set:
				count=0
				for key in product_3set_custom_key:
					if good<=set(naiveAR_custom_dict[key]):
						count+=1
						if key not in new_naiveAR_custom_key:
							new_naiveAR_custom_key.append(key)
				if count>=support:
					product_list.append(good)
				else:
					pass
			if len(product_list)==0:
				print ("三项集数量为０,请重新设定support")
				return ["项集数量为０"]
			else:
				print ("原始三项频繁集数量为"+str(len(product_list)))
				return product_list,new_naiveAR_custom_key

		product_list=[]
		product_2_set=[]
		for key in naiveAR_custom_dict:
			for good in naiveAR_custom_dict[key]:
				if good not in product_list:
					product_list.append(good)				#读取所有商品到列表
				else:
					pass									
		product_1set,product_1set_key=product_1set(product_list,naiveAR_custom_dict,support)       	     #生成一项频繁集并保存事务项key
		product_2set,product_2set_key=product_2set(product_1set,product_1set_key,support)					#生成二项频繁集，并保存事务项key
		product_3set,product_3set_key=product_3set(product_1set,product_2set,product_2set_key,support)		#生成三项频繁集，并保存事务项key	#
		product_1set_dict={}
		for item in product_1set:
			R,F,M=0,0,0
			for key in product_1set_key:
				if item in AR_custom_dict[key]:
					F+=(int(AR_custom_dict[key][item][1]))
					R+=(1-sigma)**(t0-int(key[1]))                                                     #R的计算方法
					M+=AR_custom_dict[key][item][1]*AR_custom_dict[key][item][0]				#Ｍ的计算方法
			list_RFM=[R,F,M]
			product_1set_dict[tuple([item])]=list_RFM
		print ("RFM一项频繁集计算完成，即将写入AR_set.txt")
		product_2set_dict={}
		for item in product_2set:
			R,F,M=0,0,0
			for key in product_2set_key:
				if set(item) <= set(AR_custom_dict[key]):
					item_tuple=tuple(item)
					item1=item_tuple[0]
					item2=item_tuple[1]
					quantity=int(min(AR_custom_dict[key][item1][1],AR_custom_dict[key][item2][1]))
					F+=quantity
					R+=((1-sigma)**(t0-int(key[1])))#R的计算方法
					price_sum=float(AR_custom_dict[key][item1][0])+float(AR_custom_dict[key][item2][0])#Ｍ的计算方法
					M+=(quantity*price_sum)
			list_RFM=[R,F,M]
			product_2set_dict[item_tuple]=list_RFM
		print ("RFM二项频繁集计算完成，即将写入AR_set.txt")
		product_3set_dict={}
		for item in product_3set:
			R,F,M=0,0,0
			for key in product_3set_key:
				if set(item) <= set(AR_custom_dict[key]):
					item_tuple=tuple(item)
					item1=item_tuple[0]
					item2=item_tuple[1]
					item3=item_tuple[2]
					quantity=min(AR_custom_dict[key][item1][1],AR_custom_dict[key][item2][1],AR_custom_dict[key][item3][1])
					F+=int(quantity)
					R+=((1-sigma)**(t0-int(key[1])))#R的计算方法
					price_sum=float(AR_custom_dict[key][item1][0])+float(AR_custom_dict[key][item2][0])+float(AR_custom_dict[key][item3][0])
					M+=(quantity*price_sum)
			list_RFM=[R,F,M]
			product_3set_dict[item_tuple]=list_RFM
		print ("RFM三项频繁集计算完成，即将写入AR_set.txt")	
		return product_1set_dict,product_2set_dict,product_3set_dict

if __name__=='__main__':
	print ("请输入support,sigma,to，用空格隔开，输入完请按Ｅnter键：\n")
	a=input()
	a_clean=a.split()
	support=int(a_clean[0])
	sigma=float(a_clean[1])
	t0=int(a_clean[2])
	custom_id,custom_id_naive=AR.custom_id_found()
	product_1set_dict,product_2set_dict,product_3set_dict=AR.naiveAR(custom_id,custom_id_naive,support)
	AR.save_file(product_1set_dict,"./AR_set.txt")             #将一项集写入结果
	AR.save_file(product_2set_dict,"./AR_set.txt")             #将二项集写入结果
	AR.save_file(product_3set_dict,"./AR_set.txt")             #将三项集写入结果
	print ("计算完毕，请到当前文件夹下,ARset.txt中查看结果，开哥只能帮你到这了！！！")