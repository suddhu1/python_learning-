# encapsulation 

# wrapping or binding the data or making variable private 
# i can bind data by using the methods 



# class <class_name>:
#    def __init__(self):
#       self.a 
#       self.b

# obj=<class_name>()
# obj.a


# in this way i am able to access the data but this is not the best way of doing it
# because in this way my data are not safe and can be access by any 
# so to maintain the data secutiry their is the concept of encapsulation 
# encapsuation= capsul of data and method 

#  making the variable public private and the protected 

# public <var name>
# protectes _ <var name>
# private__<var name>

# inheritance 

# accquiring the property of the parent by the child 
# or accquring the feature of the base class by the derived class 
# in this we can inherite data and the methods 

# syntax of the inheritance 

# class A:
#     pass
# class B(A):
#     pass

#  types of inheritance
# simple 
# multilevel 
# multiple 
# hybrid
# hirarchical inheritance 



# simple 

# class A:
#     pass
# class B(A):
#     pass


# multilevel 

# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass


# multiple 

# class A:
#     pass 
# class B:
#     pass 
#  class C(A,B):  # class a is inheiting the feature of the class A and the class B 
#     pass



# herarchical inheritance 

# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass


# ḥybrid 

# class A:
#     pass 
# class B(A):
#     pass 
# class C(A):
#     pass 
# class D(B,C):
#     pass 


# simple inheritance
# here the main or the base class is animal and the
#  inherit class is bird  which is inheriting the 
# methods of the base class 

# class animal:
#     def eat(self):
#         print("yes it eats")
#     def sleep(self):
#         print("yes it sleep ")
    

# class bird(animal):
#     def set_types(self,type):
#         self.type=type
#     def fly(self):
#         print("yes it fly ")
#     def speak(self,sound):
#         print(f"it speaks:{sound} {sound}")
#     def __repr__(self):
#         return "this is a " + self.type
              
# duck=bird()
# duck.set_types("duck")
# print(duck)
# duck.eat()
# duck.speak("quak quak ")


# multileve inheritance 

# class person:
#     def __init__(self,age,name):
#         self.name=name
#         self.age=age
#         print("person constructor called ")
# class emp(person):
#     def __init__(self, age, name,ids,sal):
#         self.ids=ids
#         self.sal=sal
#         print("employee constructor called ")

# class manager(emp):
#     def __init__(self, age, name, ids, sal,bonus):
#         self.bonus=bonus
#         print("manager constructor called ")
# m= manager(24,"sudarshan","SEC079BEI009",500000,100000)


#  in c++ the boject of the derived  class can can call the constructor of the base class also 
# but in the python the object of the derived  class can't  call the constructor of the base class 
# this can  be solved in the python in the following way 
# using the super method 
# or calling with the help of the class name

# class person:
#     def __init__(self,age,name):
#         self.name=name
#         self.age=age
#         print("person constructor called ")
# class emp(person):
#     def __init__(self,age,name,ids,sal):
#         person.__init__(self,age,name)
#         self.ids=ids
#         self.sal=sal
#         print("employee constructor called ")

# class manager(emp):
#     def __init__(self, age, name, ids, sal,bonus):
#         emp.__init__(self,age,name,ids,sal)
#         self.bonus=bonus
#         print("manager constructor called ")
# m= manager(24,"sudarshan","SEC079BEI009",500000,100000)


# for super method we use super().__init__(parameter) no need of writing self as parameter as we are
# using the super method 
# replace emp.__init__(self,age,name,ids,sal) with super().__init__(age,name,ids,sal)


# hirarcical inheritance

# class school:
#     def __init__(self,name,age):
#          self.name=name
#          self.age=age
# class student(school):
#         def __init__(self,name,age,rollno,per):
#              super().__init__(name,age)
#              self.rollno=rollno
#              self.per=per
#         def __repr__(self):
#              return f"name of the student is {self.name} his age is {self.age},rollno id {self.rollno} and his percentage is {self.per}"
        
# class teacher(school):
#     def __init__(self,name,age,sal):
#          super().__init__()
#          self.sal=sal
# sudarshan=student("sudarshan",23,2323,90)
# print(sudarshan)


# multiple inheritance 
# class A:
#     def __init__(self):
#         print("A has been called")  
# class B:
#      def __init__(self):
#         print("B has been called")
# class C(A,B):
#      def __init__(self):
#         print(" C has been called")
# call=C()



# hybrid inheritance in python 


# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass


# polymorphism in python oop refers to having the differnt form of the same methods or the entities
# for example we can use + for additioin as well as for string concatination 


 
# in this program we are trying to achive polymorphism for adding the two coordinate points 
# but we are not being able to do so 


# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y 
# pi=point(2,4)
# p2=point(3,5)
# print(pi+p2)


# the above problem id solved using the magic method add 

# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y 
#     def __add__(self,other):
#         x=self.x+other.x
#         y=self.y+other.y
#         p=point(x,y)
#         return p
#     def __repr__(self):
#         return f"x={self.x},y={self.y}"
# pi=point(2,4)
# p2=point(3,5)
# print(pi+p2)


 

