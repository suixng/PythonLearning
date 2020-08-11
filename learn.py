#第一章：python基础

#print('hello, world')
#print('The quick brown fox','jumps over','the lazy dog')
#print(300)
#print(100+200)
# print('100+200=',100+200)


# print('Hello world!')
# print('what is your name?')
# myName=input()
# print('Is is good to meet you, '+myName)
# print('The length of your name is:')
# print(len(myName))
# print('What is your age?')
# myAge=input()
# print('You will be '+str(int(myAge)+1)+' in a year.')


#第二章：控制流

# if name == 'Mary':
#     print('hello Mary')
#     if password == 'swordfish':
#         print('Access granted.')
#     else:
#         print('Wrong password.')


# if name == 'Alice':
#     print('Hi,Alice')
# elif age <12:
#     print('You are not Alice,kiddo')
# else:
#     print('You are neither Alice nor a little kid')


# spam = 0
# if spam<5:
#     print('Hello World!')
#     spam=spam + 1

# spam=0
# while spam<5:
#     print('Hello World!')
#     spam=spam + 1

# while True:
#     print('Please type your name')
#     name=input()
#     if name == 'your name':
#         break
# print('Thank you')

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe . What is the password? (It is a fish)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Aceess granted')

# print("My name is")
# for i in range(5):
#     print('Jimmy Five Times(' + str(i) +')')

# print('My name is')
# i = 0
# while i < 5:
#     print('Jimmy Five Times('+ str(i) + ')')
#     i=i+1

# total = 0
# for num in range(101):
#     total = total + num
# print(total)

# for i in range(12,16):
#     print(i)

# for i in range(0,10,2):
#     print(i)

# for i in range(5,-1,-1):
#     print(i)

# import random
# for i in range(5):
#     print(random.randint(1,10))

# import sys
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == "exit":
#         sys.exit()
#     print("Your tuped" + response + '.')



#第三章：函数

# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')
# hello()
# hello()
# hello()

#def语句和参数
# def hello(name):
#     print('Hello' + name)
# hello('Alice')
# hello('Bob')

#返回值和return语句

# import random
# def getAnswer(answerNumber):
# 	if answerNumber == 1:
# 		return 'It is certain'
# 	elif answerNumber == 2:
# 		return 'It is deciedly so'
# 	elif answerNumber == 3:
# 		return 'Yes'
# 	elif answerNumber == 4:
# 		return 'Reply hazy try again'
# 	elif answerNumber == 5:
# 		return 'Ask again later'
# 	elif answerNumber == 6:
# 		return 'Concentrate and ask again'
# 	elif answerNumber == 7:
# 		return 'My reply is no'
# 	elif answerNumber == 8:
# 		return 'Outlook not so good'
# 	elif answerNumber == 9:
# 		return 'Very doubtful'
# r = random.randit(1,9)
# fortune = getAnswer(r)
# print(fortune)
#print(getAnswer(random.randit(1,9)))

#None值

# spam == print('Hello') #Hello
# None == spam #True

#关键词参数和print()

# print('Hello')
# print('world') #Hello  world

# print('Hello',end='')
# print('world') #Helloworld

# print('cats','dogs','mice') #cats dogs mice

# print('cats','dogs','mice',sep=',') #cats,dogs,mice

#局部和全局作用域

# def spam():                                                                                                                                                                                                                                                     
# 	eggs = 31337
# spam()
# print(eggs) #eggs是局部变量，无法在全局变量域使用

# def spam():
# 	eggs = 99
# 	bacon()
# 	print(eggs)
# def bacon():
# 	ham = 101
# 	eggs = 0
# spam() #99

# def spam():
# 	print(eggs)
# eggs = 42
# spam()
# print(eggs) #42  42

# def spam():
# 	eggs = 'spam local'
# 	print(eggs) #spam local
# def bacon():
# 	eggs = 'bacon local'
# 	print(eggs) #bacon local
# 	spam()
# 	print(eggs) #bacon local
# eggs = 'global'
# bacon()
# print(eggs) #global

#global语句

# def spam():
# 	global eggs
# 	eggs = 'spam'
# eggs = 'global'
# spam()
# print(eggs) #spam

# def spam():
# 	global eggs
# 	eggs = 'spam' #this is the global
# def bacon():
# 	eggs = 'bacon' #this is the local
# def ham():
# 	print(eggs) #this is the global
# eggs = 42 #this is the global
# spam()
# print(eggs) #spam

# def spam():
# 	print(eggs) #ERROR!
# 	eggs = 'spam local'
# eggs = 'global'
# spam()

#异常处理

# def spam(divideBy):
# 	return 42 / divideBy
# print(spam(2))
# print(spam(12))
# print(spam(0)) #ZeroDivisionError
# print(spam(1))

# def spam(divideBy):
# 	try:
# 		return 42 / divideBy
# 	except ZeroDivisionError:
# 		print('Error:Invalid argument')
# print(spam(2))
# print(spam(12))
# print(spam(0)) #Error:Invalid argument
# print(spam(1))

# def spam(divideBy):
# 	return 42 / divideBy
# try:
# 	print(spam(2))
# 	print(spam(12))
# 	print(spam(0))
# 	print(spam(1)) #不执行：一旦执行except后，不会回到try而是直接向下执行
# except ZeroDivisionError:
# 	print('Error:Invalid argument')

#例子：猜数字

#This is a guess the number game
# import random
# secretNumber = random.randit(1,20)
# print('I am thinking of number between 1 and 20.')

#Ask the player to guess 6 times
# for guessTaken in range(1,7):
# 	print('Thank a guess.')
# 	guess = int(input())

# 	if guess < secretNumber:
# 		print('Your guess is too low')
# 	elif guess > secretNumber:
# 		print('Your guess is too high')
# 	else:
# 		break #This is the correct guess!
# if guess == secretNumber:
# 	print('Good job! Your guessed my number in' + str(guessTaken) + 'guessed!')
# else:
# 	print('Nope. The number I was thinking of was ' + str(secretNumber))



#第四章：列表


#列表数据类型

spam = ['cat','bat','rat','elephant']
print(spam[1]) #bat
spam[-1] #elephant
spam[1:3] #['bat', 'rat']
print(spam[0:-1]) #['cat','bat','rat']
spam[:2] # ['cat','bat']
spam[1:] #['bat','rat','elephant']
spam[:] #['cat','bat','rat','elephant]
len(spam) #4

del spam[2] # spam = ['cat','bat','elephant']
del spam[2] # spam = ['cat','bat']

#使用列表

catNames = []
while True:
	print('Enter the name of cat ' + str(len(catNames) + 1) + '(Or enter nothing to stop.):')
	name =input()
	if name == '':
		break
	catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
	print(' '+ name)

myPets = ['Zoe','Pooka','Fat-tail']
print('Enter a pet')
name = input()
if name not in myPets:
	print('I do not have a pet named' + name)
else:
	print(name + 'is my pet.')

#增强的赋值方法

cat = ['fat','black','loud']
size,color,disposition = cat

#方法

spam = ['hello','hi','howdy','hey']
spam.index('hey') #3
spam.append('mouse') #['hello','hi','howdy','hey','mouse']
spam.insert(1,'chiken') #['hello','chiken','hi','howdy','hey','mouse']
spam.move('hello') #['chiken','hi','howdy','hey','mouse']

spam = [2,5,3.14,1,-7]
spam.sort() #[-7,1,2,3.14,5]
spam.sort() # ['chiken','hey','hi','howdy','mouse'] 按ASCII字符顺序
spam.sort(reverse = True) #['mouse','howdy','hi','hey','chiken']
spam = ['a','z','A','Z']
spam.sort(key=str.lower) #['a','A','z','Z']

#字符串和元组

name = 'Zombie'
name[0] #Z
name[-2] #i
name[0:4] #'Zomb'
name = 'Zombie a cat'
newName = name[0:7]+'the'+name[8:12] #Zombie the cat

eggs=('hello',42,0.5)
eggs[1] #hello
eggs[1:3] #42 0.5
len(eggs) #3

tuple(['cat','dog',5]) #返回传递给它们的值的元组版本
list(('cat','dog',5)) #返回传递给它们的值的列表
list('hello') #['h','e','l','l','o']

#引用

spam = 42
cheese = spam
spam = 100 # spam=100,cheese=42

spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'Hello!' # spam = [0,'Hello!',2,3,4,5] cheese = [0,'Hello!',2,3,4,5]

def eggs(someParameter):
	someParameter.append('Hello')
spam = [1,2,3]
eggs(spam)
print(spam) #spam = [1,2,3,'Hello']

import copy
spam = ['A','B','C','D']
cheese = copy.copy(spam)
cheese[1] = 42 #spam = ['A','B','C','D'] cheese = ['A',42,'C','D']


#第五章：字典和结构化数据

#字典数据类型

myCat = {'size':'fat','color':'gray','disposition':'loud'}
myCat['size'] #fat
spam = {12345:'Combination',42:'Answer'}

spam = ['cat','dogs','moose']
bacon = ['dogs','moose','cats']
spam == bacon #false
eggs = {'name':'Zombie','age':'8','species':'cat'}
ham = {'age':'8','species':'cat','name':'Zombie'}
eggs == ham #true

birthdays = {'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}
while True:
	print('Enter a name:(blank to quit)')
	name = input()
	if name == '':
		break
if name in birthdays:
	print(birthdays[name]+'is the birthday of'+name)
else:
	print('I do not have birthday information for'+name)
	print('What is their birthday?')
	birthday = input()
	birthdays[name] = birthday
	print('Birthday database updated.')

spam = {'color':'red','age':42}
for v in spam.values():
	print(v) # red  42
for k in spam.keys():
	print(k) #color  age
for i in spam.items():
	print(i) # ('color','red')  ('age',42)
spam.keys() #dict_keys(['color','age'])
list(spam.keys()) #['color','age']
spam = {'color':'red','age':42}
for k,v in spam.items():
	print('Key:'+k+'Value:'+str(v)) #key:age Value:42  Key:color Value:red

spam = {'name':'Zombie','age':7}
'name' in spam.keys() #True
'Zombie' in spam.values() #True
'color' not in spam.keys() #True

picnicItems = {'apples':5,'cups':2}
'I am bringing' + str(picnicItems.get('cups',0)) + 'cups.' # I am bringing 2 cups.
'I am bringing' + str(picnicItems.get('eggs',0)) + 'eggs.' # I am bringing 0 eggs.
'I am bringing' + str(picnicItems['eggs']) + 'eggs.' # Error

spam = {'name':'Pooka','age':5}
spam.setdefault('color','black') #black
#spam = {'color':'black','age':5,'name':'Pooka'}
spam.setdefault('color','white') #black
#spam = {'color':'black','age':5,'name':'Pooka'}

message = 'It was a bright cold day in April,and the clocks were striking thirteen.'
count = {}
for character in message:
	count.setdefault(character,0)
	count[character] = count[character] + 1
print[count] #计算一个字符串中每个字符出现的次数

#漂亮打印

import pprint
message = 'It was a bright cold day in April,and the clocks were striking thirteen.'
count = {}
for character in message:
	count.setdefault(character,0)
	count[character] = count[character] + 1
pprint.pprint(count)

#井字棋盘

theBoard = {'top-L':' ','top-M':' ','top-R':' ',
			'mid-L':' ','mid-M':' ','mid-R':' ',
			'low-L':' ','low-M':' ','low-R':' '}
def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
	printBoard(theBoard)
	print('Turn for' + turn + '.Move on which space?')
	move = input()
	theBoard[move] = turn
	if turn == 'X':
		turn = '0'
	else:
		turn = 'X'
printBoard(theBoard)

allGuests = {'Alice':{'apples':5,'pretzels':12},
			 'Bob':{'ham sandwiches':3,'apples':2},
			 'Carol':{'cups':3,'apple pies':1}}
def totalBrought(guests,item):
	numBrought = 0
	for k,v in guests.items():
		numBrought = numBrought + v.get(item,0)
	return numBrought
print('Number of things being brought:')
print('-Apple' + str(totalBrought(allGuests,'apples')))
print('-Cups' + str(totalBrought(allGuests,'cups')))
print('-Cakes' + str(totalBrought(allGuests,'cakes')))
print('-Ham Sandwiches' + str(totalBrought(allGuests,'ham sandwiches')))
print('-Apple Pies' + str(totalBrought(allGuests,'apples pies')))


#第六章：字符串操作

#处理字符串

spam = "That is Alice's cat." #可以在字符串中使用'
spam = 'Say hi to Bob\'s mother.' # \' 单引号 \"双引号 \t制表符 \n换行符 \\倒斜杠
print(r'That is Carol\'s cat.') #That is Carol\'s cat  
print('''Dear Alice,
Eve's cat has been arrested for catnapping,cat burglary,and extortion
Sincerely,
Bob''') #直接按这个格式输出  多行字符串''' '''中的内容格式直接输出
def spam():
	"""This is a multiline comment to help explain what the spam() function does."""
	print('Hello!')
spam = 'Hello world!'
spam[0] #H
spam[-1] #!
spam[0:5] #Hello
spam[:5] #Hello
spam[6:] #world!
fizz = spam[0:5] #Hello
'Hello' in 'Hello World' #True(大小写有区别)

#有用的字符串方法

spam = 'Hello World!'
spam = spam.upper() #HELLO WORLD!
spam = spam.lower() #hello world!
spam.islower() #false
spam.isupper() #false
'HEELO'.isupper() #True
'abc123456'.islower() #True
'123456'.islower() #false

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
	print('I feel great too.')
else:
	print('I hope the rest of your day is good')

#isalpha() : 如果字符串只包含字母，且非空
#isalnum() : 如果字符串只包含字母和数字，且非空
#isdecimal() : 如果字符串只包含数字字符，且非空
#isspace() : 如果字符串只包含空格、制表符和换行，且非空
#istitle() : 如果字符串仅包含以大写字母开头、后面都是小写字母的单词

while True:
	print('Enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('Please enter a number for your age')
while True:
	print('Select a new password (letters and number only):')
	password = input()
	if password.isalnum():
		break
	print('Passwords can only have letters and numbers.')

'Hello World!'.startswith('Hello') #True
'Hello World!'.endswith('World') #False

'ABC'.join(['My','name','is','Simon']) # MyABCnameABCisABCSimon  join():针对字符串传入列表，返回字符串
'My name is Simon'.split() # ['My','name','is','Simon'] spilt():针对一个字符串调用，返回一个字符串列表
'My name is Simon'.split('m') #['My na','e is Si','on'] 默认以空白字符分割，也可自行指定

'Hello'.rjust(10) #'     Hello'
'Hello'.ljust(10) #'Hello     '
'Hello'.rjust(10,'*') #'*****Hello'
'Hello'.ljust(10,'-') #'Hello-----'
'Hello'.center(10) #'  Hello   '
'Hello'.center(10,'-') #'--Hello---'

def printPicnic(itemDict,leftWidth,rightWidth):
	print('PICNIC ITEMS'.center(leftWidth + rightWidth,'-'))
	for k,v in itemDict.items():
		print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))
printItems = {'sandwiches':4,'apples':12,'cups':4,'cookies':8000}
printPicnic(picnicItems,12,5)
picnicItems(picnicItems,20,6)

spam = ' Hello World '
spam.strip() #Hello World   strip():返回一个新的字符串，他的开头或末尾都没有空白字符
spam.lstrip() #'Hello World '    
spam.rstrip()  #' Hello World'
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS') #'BaconSpamEggs'  strip('mapS'):删除两端出现的字符，顺序不重要


#第七章：模式匹配与正则表达式

#不用正则表达式来查找文本模式

def isPhoneNumber(text):
	if len(text)!=12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3]!='-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7]!='-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242')) # True
print('Mosh mosh is a phone number:')
print(isPhoneNumber('Mosh mosh')) # False

message = 'Call me at 415-555-1011 tomorrow.415-555-9999 is my office'
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found:' + chunk)
print('Done')

#用正则表达式查找文本模式

import re
phoneNumber = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found:'+mo.group()) # Phone number found: 415-555-4242

#用正则表达式匹配更多模式
#利用括号进行分组
phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1)) # 415
print(mo.group(2)) # 555-4242
print(mo.group(0)) # 415-555-4242
print(mo.group()) # 415-555-4242
print(mo.groups()) # 415,555-4242
areaCode,mainNumber = mo.groups()
print(areaCode) # 415
print(mainNumber) # 555-4242
#本身存在括号
phoneNumRegex = re.compile(r'(\(\d\d\d))(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242')
print(mo.group(1)) # (415)
print(mo.group(2)) # 555-4242

#用管道模式匹配多个分组(字符|称为管道)
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group()) # Batman
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group()) # Tina Fey

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group()) # Batmobile
print(mo.group(1)) # mobile

#用问号实现可选匹配
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventure of Batman')
print(mo1.group()) # Batman
mo2 = batRegex.search('The Adventure of Batwoman')
print(mo2.group()) # Batwoman

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group()) # 415-555-4242
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group()) # 555-4242
 
#用星号匹配零次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventure of Batman')
print(mo1.group()) # Batman
mo2 = batRegex.search('The Adventure of Batwoman')
print(mo2.group()) #Batwoman
mo3 = batRegex.search('THe Adventure of Batwowoman')
print(mo3.group()) # Batwowoman

#用加号匹配一次或多次
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventure of Batwoman')
print(mo1.group()) # Batwoman
mo2 = batRegex.search('The Adventure of Batwowoman')
print(mo2.group()) # Batwowoman
mo3 = batRegex.search('The Adventure of Batman')
print(mo3 == None) #True

#用花括号匹配特定次数(Ha){3}  (Ha){3,5}  (Ha){3,}
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group()) # HaHaHa
mo2 - haRegex.search('Ha')
print(mo2 == None) # True

#贪心和非贪心匹配
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group()) # HaHaHaHaHa
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group()) #HaHaHa

#findall()方法
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Cell:415-555-9999 Work:212-555-0000')
print(mo.group()) # 415-555-9999
print(phoneNumRegex.findall('Cell:415-555-9999 Work:215-555-0000')) # ['415-555-9999','212-555-0000]

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex.findall('Cell:415-555-999 Work: 212-555-0000')) # [('415','555','9999'),('212','555','0000')]

#建立自己的字符分类
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RobCop eats baby food. BABY FOOD.')) # ['o','o','o','e','a','a','o','o','A','O','O']
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RobCop eats baby food. BABY FOOD.')) # 不存在字符类中所有字符

#插入字符和美元字符
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello World')
print(beginsWithHello.search('He said hello') == None) # True

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
print(endsWithNumber.search('Your number is forty two') == None) # True

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('12345xyz67890') == None) # True
print(wholeStringIsNum.search('12 34567890') == None) # True

#通配字符
atRegex = re.compile(r'.at') #句号.通配符只匹配一个字符(除了换行之外所有字符)
print(atRegex.findall('The cat in the hat sat on the flat mat')) # ['cat','hat,'sat','lat','mat']
#用点-星匹配所有字符(用re.DOTALL可以让句点.字符匹配所有字符，包括换行字符)
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: AI Last Name: Swigart')
print(mo.group(1)) # AI
print(mo.group(2)) # Swigart

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) # <To serve man>
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) # <To serve man> for dinner.>

#不分大小写的匹配
robot = re.compile(r'robot',re.I)
robot.search('Robot is part man,part machine,all cop').group() # Robot
robot.search('ROBOT is part man,part machine,all cop').group() # ROBOT
robot.search('robot is part man,part machine,all cop').group() # robt

#用sub()方法替换字符串
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED','Agent Alice gave Agent Bob')) # CENSORED gave CENSORED 

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****','Agent ALice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')) # A**** told C**** that ....

#电话号码与E-mail地址提取程序

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
