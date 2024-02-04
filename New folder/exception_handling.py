#  exception and  handling in the python are done to 
# make code error free and get the required result for the code
# the error like intendentation error and syntax error are under the
# compile time error and error comes in the time of getting output or
# like dividing the number by 0 comes into the run time error 
# handking error at the compile time is call error handling 
# handling the error at the time of run i called exception handling 


# exception handling can be done by using the some ways
# 1) except 
# 2) try 
# 3)else
# 4) raise
# 5) finally


# under syntax error errror like missing the brackets 
# wrong IndentationError etc comes

# for exception handling we use above mention ways and solve them 

# a=int(input("enter the number "))
# b=int(input("enter the number"))
# c=a/b
# print(c)

# in this program example if we use the value of b is other number 
# except 0 that will work but for zero it will give error called ZeroDivisionError

# # to solve this problem we do i following way 

# try:
#     a=int(input("enter the number "))
#     b=int(input("enter the number"))
#     c=a/b
#     print("division is ",c)
# except:
#     print("b should not be zero ")

# inside try the given statement will be executed and if any ZeroDivisionError occur then the except will be executed 


# in python there are some class avialable for error handling 
# ther ther are 
# ArithmeticError
# ZeroDivisionError
# ValueError
# LookupError
# IndentationError and many others


# in the above program we can use the above mention class to especify what kind of the exception we are handling 


# try:
#     a=int(input("enter the number "))
#     b=int(input("enter the number"))
#     c=a/b
#     print("division is ",c)
# except ZeroDivisionError:
#     print("b should not be zero ")


# in the above program we espicifically handling the zerodivision error 
# but if we use enter the input number like 2q and zero it wont because we will now facing the value error and we have not define for this error


# try:
#     a=int(input("enter the number "))
#     b=int(input("enter the number"))
#     c=a/b
#     print("division is ",c)
# except ZeroDivisionError:
#     print("dividing number should not be zero ") 
# except ValueError:
#     print("the number must be integer ")

# a=int(input("enter the number "))
# # b=int(input("enter the number"))



# we are putting the above code in loop so that we get output and exit the code
# while True:
#     try:
#         a=int(input("enter the number "))
#         b=int(input("enter the number"))
#         c=a/b
#         print("division is ",c)
#         break
#     except ZeroDivisionError:
#         print("dividing number should not be zero ") 
#     except ValueError:
#         print("the number must be integer ")

# in the below program we use "e" to get the by default message set for the designated error 
# while True:
#     try:
#         a=int(input("enter the number "))
#         b=int(input("enter the number"))
#         c=a/b
#         print("division is ",c)
#         break
#     except (ZeroDivisionError,ValueError) as e:
#         print(e)  # it will print the default message set by python builder 
   

# import sys 
# print(dir(sys))
#  below are the different methods and attribute we are getting while we import the library caller "sys"
# ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__',
# '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding',
#  '_framework', '_getframe', '_getframemodulename', '_git', '_home', '_setprofileallthreads', '_settraceallthreads', '_stdlib_dir', '_vpath', '_xoptions', 'activate_stack_trampoline', 
#   'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'deactivate_stack_trampoline',
#     'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks',
#       'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 
#        'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getunicodeinternedsize', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 
#        'is_stack_trampoline_active', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'monitoring', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix',
#          'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout',
#           'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']

# import sys
# while True:
#     try:
#         a=int(input("enter the number "))
#         b=int(input("enter the number"))
#         c=a/b
#         print("division is ",c)
#         break
#     except:
#         a,b,c=sys.exc_info()
#         print("exception class",a)
#         print("exception message",b)
#         print("line number ",c.tb_lineno) # from the sys library it will give the line where the exception error is occuring 


# 1) except 
# 2) try 
# 3)else
# 4) raise
# 5) finally


# try:
#     a=int(input("enter the number "))
#     b=int(input("enter the number"))
#     c=a/b
#     print("division is ",c)
# except:
#     print("b should not be zero")
# finally:
#     print("this bock will always run and use for keeping the imp code need to be executed will be kept here")



# using the raise in program 


# while True:
#     try:
#         a=int(input("enter the number "))
#         b=int(input("enter the number"))
#         if a<0 or b<0:
#             raise Exception("negative number not allowed")
#         c=a/b
#         print("division is ",c)
#         break
#     except ZeroDivisionError:
#         print("dividing number should not be zero ") 
#     except ValueError:
#         print("the number must be integer ")

# we are using the parent class i.e Exception 

# while True:
#     try:
#         a=int(input("enter the number "))
#         b=int(input("enter the number"))
#         if a<0 or b<0:
#             raise Exception("negative number not allowed")
#         c=a/b
#         print("division is ",c)
#         break
#     except Exception as e:
#         print(e)




# ---------------------------------------------------
#  zip function 

# mylist=['a','b','c','d','e']
# mylist2=[1,2,3,4,5]

# for i in zip(mylist,mylist2):
#     print(i)

# output
# ('a', 1)
# ('b', 2)
# ('c', 3)
# ('d', 4)
# ('e', 5)

# dict with the zip function 

# mylist=['a','b','c','d','e']
# mylist2=[1,2,3,4,5]
# dict={}
# for x,y in zip(mylist,mylist2):
#     dict[x]=y
# print(dict)

# output
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}



# reduced function  is avilable at import functools
# import functools

# functools.reduce()


# map(fun,seq)  # it will give value according to the logic
# filter(fun,seq) # it will give value according to the logic
# reduce(fun,seq) # it will provide me the single value

# in the fun we can use the lambda funtion 


# import functools

# mylist=[1,2,3,4,5]
# print(functools.reduce(lambda a,b:a+b,mylist))

# # it will give me the single value 15

# def sq_number(n):
#     for i in range(1,n+1):
#         yield i*i  # it is giving us the value of the square of the in list form 

# a=sq_number(3)

# print("the square of the numbera 1,2,3 are: ")
# # for i in a:
#     print(i)

# print(next(a))
# print(next(a))
# print(next(a))
 



