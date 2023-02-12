# class Wow:
#     def __wow(self):
#         print("Wow")
#     def _hello(self):
#         print("Hello")
# some_obj = Wow()
# some_obj._hello()
# some_obj._Wow__wow()

# class Hello:
#     def __init__(self):
#         print("Hello!")
# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World!")
# hello_world = Hello_World()

# class Grandparent:
#     def about(self):
#         print("I am GrandParent")
#     def about_myself(self):
#         print("I am Grandparent")
# class Parent(Grandparent):
#     def about_myself(self):
#         print("I am Parent")
# class Child(Parent):
#     def __init__(self):
#         super().about()
#         super().about_myself()
# nick = Child

# try:
#     print("start code")
# except:
#     print("We have an error")
# else:
#     print("I am ELSE")
# finally:
#     print("I am FINALLY")

# def checker(var_1):
#     if type(var_1)!= str:
#         raise TypeError(f"Sorry, we can`t work with {type(var_1)}"), "
#                         f"we need class str"
#     else:
#         return var_1
#
# first_var = "10"
# checker(first_var)

import warnings
warnings.warn("Warning, no code here", SyntaxWarning)
