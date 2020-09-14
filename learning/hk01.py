# def hano(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         hano(n-1, a, c, b)
#         hano(1, a, b, c)
#         hano(n-1, b, a, c)
# a = input('请输入A柱盘子的个数：')
# num = int(a)
# print('把',num,'个盘子全部移到C柱子的顺序为：')
# hano(num, 'A', 'B', 'C')

# def Stones(J,S):
#     count=0
#     for i in S:
#         if i in J:
#             count+=1
#     return count
# print(Stones("z","ZZ"))

# def findall(sub,s):
# 	indexlist = []
# 	index = s.find(sub)
# 	while index != -1:
# 		indexlist.append(index)
# 		index = s.find(sub,index+1)
	
# 	if len(indexlist) > 0:
# 		return indexlist
# 	else:
# 		return -1
# print(findall("annacanna","annbcdancaadsannannacannnannacanna"))

# a=lambda b: int(b)
# print(a(input()))

# def test(num,target):
# 	if(len(num)<2):
# 		return
# 	for i in range(0,len(num)-1):
# 		for j in range(i+1,len(num)):
# 			if num[i] + num[j] == target:
# 				return[num[i],num[j]]
# print(test([2,7,11,15],9))

# def test(a):    
#     result=''    
#     for i in zip(*a):        
#         if len(set(i))==1:            
#             result +=i[0]        
#         else:            
#             break    
#     return result
# list=["flower","flow","flight"]
# print(test(list))

# class Person(object):
#     def _init_(self,name,age):
#         self.name=name
#         self._age=age
#     name='li'
#     def setage(self,age):
#         self._age=age
#     def getage(self):
#         return self._age
#     @classmethod
#     def getName(self,value):
#         self.name=value
# print(Person.name)
# p1=Person()
# print(p1.name)
# p1.country='china'
# print(p1.country)
# p1.setage(12)
# print(p1.getage())

# spam=[9,5,2,1,4,8,3,7,10]
# spam.sort()
# n=10
# a=[]
# temporary=0
# def test():
#     for i in range(len(spam)):
#         for j in range(i+1,len(spam)):
#             if spam[i]+spam[j]==n:
#                 a.append(str(spam[i])+","+str(spam[j]))
#             elif spam[i]+spam[j]<n:
#                 temporary=spam[i]+spam[j]
#                 for k in range(j+1,len(spam)):
#                     if temporary+spam[k]==n:
#                         a.append(str(spam[i])+","+str(spam[j])+","+str(spam[k]))
#                     elif temporary+spam[k]<n:
#                         temporary=temporary+spam[k]
#                         for l in range(k+1,len(spam)):
#                             if temporary+spam[l]==n:
#                                a.append(str(spam[i])+","+str(spam[j])+","+str(spam[k])+","+str(spam[l]))
#                         b=1 
#                 b=2
#     return (a)              
# print(test())

#电话号码与E-mail地址提取程序
import pyperclip, re
phoneRegex = re.compile(r'''(
	(\d{3}|\(d{3}\))?					#Area code
	(\s|-|\.)?							#separator
	(\d{3})								#first 3 digits
	(\s|-|\.)							#separator
	(\d{4})								#last 4 digits
	(\s*(ext|x|ext\.)\s*(\d{2,5}))?		#extension
	)''',re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-A0-9._%+-]+		#usernama
	@						#@ symbol
	[a-zA-Z0-9.-]+			#domain name
	(\.[a-zA-Z]{2,4})		#dot-something
	)''')

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard')
	print('\n'.join(matches))
else:
	print('NO phone numbers or email address found.')



