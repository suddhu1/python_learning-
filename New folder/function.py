# concatinating the string

# def attach(s1,s2):
# s3=s1+s2
# print("joined string is",s3)
 
# attach("good","night")
# defgreet(name,msg="how are you")
# print("hellow",name,msg)

# are a of the circle

# ar=0
# de farea(a,p=3.1416):
# ar=p*a*a
# print("area of the circlr is",ar)

# print("enter the radius of the circle")
# s=int(input("enter the radius"))
# area(s)


# find the largest among the group of the word

# def find_largest(*a):
# largest=""
# for i ina:
# if  len(a)>len(largest):
# largest=i
# return len(largest)
# z=find_largest("sudarshan pathak","laxmi subedhi")
# print(z)



# outside and insdie variable

# a="ilovepython"
# def f():
# a="i love java"
# print(a)
# f() 
# print(a)



# globa land the local variable

# a="i love python"
# def f():
# global a
# a="i love java"
# pri nt(a)
# f()
# print(a)

# its the another example

# def foo(x,y):
# global a
# a=42
# x,y =y,x
# b=33
# b=17
# c=100
# print(a,b,x,y)
# a,b,x,y=1,15,3,4
# foo(17,4)
# print(a,b,x,y)

# laymbda function
# there won't be any definition for lambda function
# anonymous function
# key word use:lambda
# syntax: 
# lambda(arg1,arg2,.......,argn):(expression)

# print((lambda a,b:a+b)(2,3))

# my_lambda_function=lambdaa,b:a+b
# print(my_lambda_function)
# x=my_lambda_function(10,15)
# print(x)
# print(my_lambda_function)
# type(my_lambda_function)

# to find the square of the given number using lambda function

# square_of_number=lambdaa,b:(a**2,b**2)
# x=int(input("enter the number"))
# y=int(input("enter the number"))
# Z,U=square_of_number(x,y)
# print(Z,U)
 
# first letter of the  string

# a=input("enter the string")
# z=lambda z:z[0]
# print(z(a))

# use of the lambda function to find true and false

# a=int(input("enter the number"))
# oe=lambda oe:(oe%2==0)
# print(oe(a))


# oroe=lambdaa:"true"ifa%2==0else"false"

# map(function,iterable)
# iterable=string,tuple,set,dict,range

# mylist=[1,2,3,4,5]
# def square(n):
# return n**2
# mylist=[1,2,3,4,5]
# for  i in mylist:
# print(square(i))


# print(square(mylist))

# def square(mylist):
# return mylist**2
# mylist=[1,2,3,4,5]
# pri nt(list(map(square,mylist)))

# inspect the string using the mapping function the python inbuilt function

# def inspect(mylist): 
# for i in mylist:
# if len(mylist)%2==0:
# ret urn "EVEN"
# else:
# return i[0]

# mylist=["january","february","march"]
# print(list(map(inspect,mylist)))

# filter
# i tfilter the values
# mylist=[1,2,3,4,5]
# def check_even(n):
# return n%2==0
# mylist=[1,2,3,4,5]
# pri nt(list(filter(check_even,mylist)))

# lambda and mapfunction being use together examples

# example 1

# mylist=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambdan:n**2,mylist)))

# example2

# mystring=["jan","feb","mar"]
# print(list(map(lambda a:a[0],mystring)))

# oop in python

# class in python

# calss with object python
# class emp:
# def__init__(self):
# self.name="are you serious"
# self.age=1000
# sel f.sel=1000000000
# haina_hola=emp()
# print(haina_hola.age)

# parameterize constructor in python

# class emp:
# def__init__(self,a,b,d):
# self.name=a
# self.age=b
# sel f.self=d
# haina_hola=emp("what are you doing",1999,174489723984)
# print(haina_hola.age)

# class with the constructor and the function(method)in the python

# class emp:
# def__init__(self,a,b,d):
# self.name=a
# self.age=b
# sel f.sel=d
# def show(self):
# print(self.name,self.age,self.sel)
# haina_hola=emp("whatareyoudoing",1999,174489723984)
# hai na_hola.show()

# oops features
# encapsulation
# inheritance
# polymorphism
# abstraction

# special method(dandermethod)

# __init__(constructor)method which is called at the time of creating object
# __str__()
# __repe__()

# circle related problem using the class concept in the python

# class circle:
# def__init__(self,r):
# self.radius=r
# def cal_area(self):
# are a=3.1416*self.radius**2
# print("area of the circle is",area)
# def  calc_circumference(self):
# circ=2*3.1416*self.radius
# print("circumference of the circle is",circ)
 
# calculation=circle(2)
# calculation.cal_area()
# calculation.calc_circumference()



# ((in the above program we can import math library instead to use the value of the pi))
# in the below program i have use a seperate method to print the info usig (f) string


# import math
# class circle:
# def__init__(self,r):
# self.radius=r
# def cal_area(self):
# sel f.area=math.pi*self.radius**2
# #print("area of the circle is",area)
# def  calc_circumference(self):
# self.circ=2*math.pi*self.radius
# #print("circumference of the circle is",circ)
# def  disp(self):
# print(f"area{self.area}")
# print(f"circumference{self.circ}")
# cal culation=circle(2)
# calculation.cal_area()
# calculation.calc_circumference()
# calculation.disp()


# class circle:
# pi=3.1416#class variable
# def__init__(self,r):
# self.radius=r
# def cal_area(self):
# sel f.area=circle.pi*(self.radius**2)#circle.pi accessing the class variable
# #print("area of the circle is",area)
# def  calc_circumference(self):
# self.circ=(2*circle.pi)*self.radius
# #print("circumference of the circle is",circ)
# def disp(self):
# print(f"area{self.area}")
# print(f"circumference{self.circ}")
# cal culation=circle(8)
# calculation.cal_area()
# calculation.calc_circumference()
# calculation.disp()

# class emp():
# arise_amount=float(input("enter the percentage of the salary increase"))
# def__init__(self,a,b,c):
# self.name=a
# self.age=b
# self.sal=c
# defdisp_bef(self):
# print(f"the salary of {self.name} is {self.sal}")
# def increase_sal(self):
# self.sal+=((emp.arise_amount/100)*self.sal)

# def display(self):
# print(f"the amount of the salary of {self.name} after the increament is {self.sal}")

# obj1=emp("sudarshan",12,30000)
# obj2=emp("aayush",13,5600)
# obj1.disp_bef()
# obj1.increase_sal()
# obj1.display()
# obj2.disp_bef()
# obj2.increase_sal()
# obj2.display()

# class math:

#      @staticmethod
#      def add_nod(a,b):
#           c=a+b
#           return c
#            @staticmethod
#           def mul_mos(a,b):
#               c=a*b
#               return c
# a=math.add_no d(10,50)
# print(a)

 
