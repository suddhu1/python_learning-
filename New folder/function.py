#concatinatingthestring

#defattach(s1,s2):
#s3=s1+s2
#print("joinesstringis",s3)

#attach("good","night")
#defgreet(name,msg="howareyou")
#print("hellow",name,msg)

#areaofthecircle

#ar=0
#defarea(a,p=3.1416):
#ar=p*a*a
#print("areaofthecirclris",ar)

#print("entertheradiusofthecircle")
#s=int(input("entertheradius"))
#area(s)


#findthelargestamongthegroupoftheword

#deffind_largest(*a):
#largest=""
#foriina:
#iflen(a)>len(largest):
#largest=i
#returnlen(largest)
#z=find_largest("sudarshanpathak","laxmisubedhi")
#print(z)



#outsideandinsdievariable

#a="ilovepython"
#deff():
#a="ilovejava"
#print(a)
#f()
#print(a)



#globalandthelocalvariable

#a="ilovepython"
#deff():
#globala
#a="ilovejava"
#print(a)
#f()
#print(a)

#itstheanotherexample

#deffoo(x,y):
#globala
#a=42
#x,y=y,x
#b=33
#b=17
#c=100
#print(a,b,x,y)
#a,b,x,y=1,15,3,4
#foo(17,4)
#print(a,b,x,y)

#laymbdafunction
#therewon'tbeanydefinitionnorlambdafunction
#anonymousfunction
#keyworduse:lambda
#syntax:
#lambda(arg1,arg2,.......,argn):(expression)

#print((lambdaa,b:a+b)(2,3))

#mylambdafunction=lambdaa,b:a+b
#print(mylambdafunction)
#x=mylambdafunction(10,15)
#print(x)
#print(my_lambda_function)
#type(my_lambda_function)

#tofindthesquareofthegivennumberusinglambdafunction

#square_of_number=lambdaa,b:(a**2,b**2)
#x=int(input("enterthenumber"))
#y=int(input("enterthenumber"))
#Z,U=square_of_number(x,y)
#print(Z,U)

#firstletterofthestring

#a=input("enterthestring")
#z=lambdaz:z[0]
#print(z(a))

#useofthelambdafunctiontofindtrueandfalse

#a=int(input("enterthenumber"))
#oe=lambdaoe:(oe%2==0)
#print(oe(a))


#oroe=lambdaa:"true"ifa%2==0else"false"

#map(function,iterable)
#iterable=string,tuple,set,dict,range

#mylist=[1,2,3,4,5]
#defsquare(n):
#returnn**2
#mylist=[1,2,3,4,5]
#foriinmylist:
#print(square(i))


#print(square(mylist))

#defsquare(mylist):
#returnmylist**2
#mylist=[1,2,3,4,5]
#print(list(map(square,mylist)))


#inspectthestringusingthemappingfunctionthepythoninbuiltfunction

#definspect(mylist):
#foriinmylist:
#iflen(mylist)%2==0:
#return"EVEN"
#else:
#returni[0]

#mylist=["january","february","march"]
#print(list(map(inspect,mylist)))

#filter
#itfilterthevalues
#mylist=[1,2,3,4,5]
#defcheck_even(n):
#returnn%2==0
#mylist=[1,2,3,4,5]
#print(list(filter(check_even,mylist)))

#lambdaandmapfunctionbeingusetogetherexamples

#example1

#mylist=[1,2,3,4,5,6,7,8,9,10]
#print(list(map(lambdan:n**2,mylist)))

#example2

#mystring=["jan","feb","mar"]
#print(list(map(lambdaa:a[0],mystring)))

#oopinpython

#classinpython

#calsswithobjectpython
#classemp:
#def__init__(self):
#self.name="areyouseerious"
#self.age=1000
#self.sel=1000000000
#haina_hola=emp()
#print(haina_hola.age)

#parameterizeconstructorinpython

#classemp:
#def__init__(self,a,b,d):
#self.name=a
#self.age=b
#self.self=d
#haina_hola=emp("whatareyoudoing",1999,174489723984)
#print(haina_hola.age)

#classwiththeconstructorandthefunction(method)inthepython

#classemp:
#def__init__(self,a,b,d):
#self.name=a
#self.age=b
#self.sel=d
#defshow(self):
#print(self.name,self.age,self.sel)
#haina_hola=emp("whatareyoudoing",1999,174489723984)
#haina_hola.show()

#oopsfeatures
#encapsulation
#inheritance
#polymorphism
#abstraction

#specialmethod(dandermethod)

#__init__(constructor)methodwhichiscalledatthetimeofcreatingonject
#__str__()
#__repe__()

#circlerelaredproblemusingtheclassconceptinthepython

#classcircle:
#def__init__(self,r):
#self.radius=r
#defcal_area(self):
#area=3.1416*self.radius**2
#print("areaofthecircleis",area)
#defcalc_circumference(self):
#circ=2*3.1416*self.radius
#print("circumferenceofthecircleis",circ)

#calculation=circle(2)
#calculation.cal_area()
#calculation.calc_circumference()



#((intheaboveprogramwecanimportmathlibraryinsteadtousethevalueofthepi))
#inthebelowprogramihaveuseaseperatemethodtoprinttheinfousigfstring


#importmath
#classcircle:
#def__init__(self,r):
#self.radius=r
#defcal_area(self):
#self.area=math.pi*self.radius**2
##print("areaofthecircleis",area)
#defcalc_circumference(self):
#self.circ=2*math.pi*self.radius
##print("circumferenceofthecircleis",circ)
#defdisp(self):
#print(f"area{self.area}")
#print(f"circumference{self.circ}")
#calculation=circle(2)
#calculation.cal_area()
#calculation.calc_circumference()
#calculation.disp()


#classcircle:
#pi=3.1416#classvariable
#def__init__(self,r):
#self.radius=r
#defcal_area(self):
#self.area=circle.pi*(self.radius**2)#circle.piaccessingtheclassvariable
##print("areaofthecircleis",area)
#defcalc_circumference(self):
#self.circ=(2*circle.pi)*self.radius
##print("circumferenceofthecircleis",circ)
#defdisp(self):
#print(f"area{self.area}")
#print(f"circumference{self.circ}")
#calculation=circle(8)
#calculation.cal_area()
#calculation.calc_circumference()
#calculation.disp()

#classemp():
#arise_amount=float(input("enterthepercentageofthesalaryincrease"))
#def__init__(self,a,b,c):
#self.name=a
#self.age=b
#self.sal=c
#defdisp_bef(self):
#print(f"thesalaryof{self.name}is{self.sal}")
#defincrease_sal(self):
#self.sal+=((emp.arise_amount/100)*self.sal)

#defdisplay(self):
#print(f"theamountofthesalaryof{self.name}aftertheincreamentis{self.sal}")

#obj1=emp("sudarshan",12,30000)
#obj2=emp("aayush",13,5600)
#obj1.disp_bef()
#obj1.increase_sal()
#obj1.display()
#obj2.disp_bef()
#obj2.increase_sal()
#obj2.display()

