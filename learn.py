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
