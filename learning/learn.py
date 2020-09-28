class Person(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
    #访问器-getter方法
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    #修改器-setter方法
    @age.setter
    def age(self,age):
        self._age=age
    def play(self):
        if self._age <=18:
            print('%s正在玩飞行棋'%self._name)
        else:
            print('%s正在玩斗地主'%self._name)

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,grade):
        self._grade = grade
    def study(self,course):
        print('%s的%s正在学习%s' %(self._grade,self._name,course))

class Teacher(Person):
    def __init__(self,name,age,title):
        super().__init__(name,age)
        self._title = title
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        self._title = title
    def teach(self,course):
        print('%s%s正在讲%s'%(self._name,self._title,course))
def main():
    stu = Student('王大锤',15,'初三')
    stu.study('数学')
    stu.play()
    t = Teacher('张三',38,'专家')
    t.teach('python')
    t.play()
if __name__ =='__main__':
    main()
