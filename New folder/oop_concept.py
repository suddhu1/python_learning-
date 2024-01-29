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
