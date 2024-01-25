# concatinating the string

# def attach(s1,s2):
#     s3=s1+s2
#     print("joines string is ", s3)

# attach("good ","night ")
# def greet(name , msg="how are you ")
#     print("hellow ",name , msg)

# area of the circle 

# ar=0
# def area(a,p=3.1416):
#     ar=p*a*a
#     print("area of the circlr is ",ar)

# print("enter the radius of the circle")
# s=int(input("enter the radius"))
# area(s)


# find the largest among the group of the word

# def find_largest(*a):
#     largest = ""
#     for i in a:
#         if len(a)>len(largest):
#             largest = i
#     return len(largest)
# z=find_largest("sudarshan pathak","laxmi subedhi")
# print(z)



# outside and insdie variable

# a="i love python"
# def f():
#    a="i love java"
#    print(a)
# f() 
# print(a)



# global and the local variable

# a="i love python"
# def f():
#    global a 
#    a="i love java"
#    print(a)
# f() 
# print(a)

# its the another example

# def foo(x,y):
#     global a
#     a = 42
#     x,y = y,x
#     b=33
#     b=17
#     c=100
#     print(a,b,x,y)
# a,b,x,y=1,15,3,4
# foo(17,4)
# print(a,b,x,y)

# laymbda function 
# there won't be any definitionn or lambda function 
# anonymous function
# keyword use :lambda
# syntax :
# lambda (arg1,arg2,.......,argn):(expression) 

# print((lambda a,b:a+b)(2,3))

# mylambdafunction=lambda a,b:a+b
# print(mylambdafunction)
# x= mylambdafunction(10,15)
# print(x)
# print(my_lambda_function)
# type(my_lambda_function)

# to find the square of the given number using lambda function

# square_of_number = lambda a,b:(a**2,b**2)
# x= int(input("enter the number"))
# y= int(input("enter the number"))
# Z,U=square_of_number(x,y)
# print(Z,U) 

# first letter of the string

# a=input("enter the string")
# z=lambda z:z[0]
# print(z(a))

# use of the lambda function to find true and false

# a=int(input("enter the number"))
# oe=lambda oe:(oe%2==0)
# print(oe(a))


# or    oe= lambda a:"true " if a%2==0 else "false"             

 # map(function, iterable) 
# iterable= string , tuple , set,dict, range 

 # mylist=[1,2,3,4,5]
# def square(n):
#     return n**2
# mylist=[1,2,3,4,5]
# for i in mylist:
#     print(square(i))


# print(square(mylist))

# def square(mylist):
#     return mylist**2
# mylist=[1,2,3,4,5]
# print(list(map(square, mylist)))


# inspect the string using the mapping function the python inbuilt function

# def inspect(mylist):
#     for i in mylist:
#         if len(mylist)%2==0:
#             return "EVEN"
#         else:
#             return i[0]
        
# mylist=["january","february","march"]
# print(list(map(inspect,mylist)))

#  filter
# it filter the values 
# mylist=[1,2,3,4,5]
# def check_even(n):
#     return n%2==0
# mylist=[1,2,3,4,5]
# print(list(filter(check_even,mylist)))

#  lambda and  map function being use together examples

# example 1

# mylist=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda n:n**2,mylist)))

# example 2

# mystring=["jan","feb","mar"]
# print(list(map(lambda a: a[0],mystring)))

# oop in python 
 
# class in python 

# calss with object python 
# class emp:
#     def __init__(self):
#         self.name="are you seerious"
#         self.age=1000
#         self.sel=1000000000
# haina_hola=emp()
# print(haina_hola.age)

# parameterize constructor in python

# class emp:
#     def __init__(self,a,b,d):
#         self.name=a
#         self.age=b
#         self.self=d
# haina_hola=emp("what are you doing",1999,174489723984)
# print(haina_hola.age)

# class with the constructor and the function(method ) in the python 

# class emp:
#     def __init__(self,a,b,d):
#         self.name=a
#         self.age=b
#         self.sel=d
#     def show(self):
#         print(self.name,self.age,self.sel)
# haina_hola=emp("what are you doing",1999,174489723984)
# haina_hola.show()

# oops features 
#  encapsulation 
# inheritance 
# polymorphism 
# abstraction 

# special method (dander method )

#  __init__(constructor ) method which is called at the time of creating onject 
# __str__()
# __repe__()

# circle relared problem using the class concept in the python 

# class circle:
#     def __init__(self,r):
#         self.radius=r
#     def cal_area(self):
#         area=3.1416*self.radius**2
#         print("area of the circle is ",area)
#     def calc_circumference(self):
#         circ=2*3.1416*self.radius
#         print("circumference of the circle is ",circ)
             
# calculation=circle(2) 
# calculation.cal_area()  
# calculation.calc_circumference()



# ((in the above program we can import math library instead to use the value of the pi ))
# in the below program i have use a seperate method to print the info usig f string 


# import math
# class circle:
#     def __init__(self,r):
#         self.radius=r
#     def cal_area(self):
#         self.area=math.pi*self.radius**2
#         # print("area of the circle is ",area)
#     def calc_circumference(self):
#         self.circ=2*math.pi*self.radius
#         # print("circumference of the circle is ",circ)
#     def disp(self):
#         print(f"area {self.area}")
#         print(f"circumference {self.circ }")       
# calculation=circle(2) 
# calculation.cal_area()  
# calculation.calc_circumference()
# calculation.disp()


