# class ParentClass:
#     def __init__(self):
#         print("parent Constructor")
#
#     def parent_meathod(self):
#         print("Parent Money function")
#
#     def money(self):
#         print("this is money function")
#
#
# class child(ParentClass):
#     pass
#
#
# # p= ParentClass()
# # p.parent_meathod()
#
#
# c = child()
# c.parent_meathod()
# c.money()

class parent:
    def __init__(self):
        print("Constructor")

    def function1(self):
        print("function1")

    def function2(self):
        try:
            x=int(input("Enter no x: "))
            y=int(input("Enter no y: "))
            if y==0:
                raise Exception("Y cannot be 0")
            print(x/y)


        except Exception as e:
            print(e)




class sibling(parent):

    def sibling1(self):
        print("this is sibling function")

test=sibling()
# test.sibling1()
test.function2()




# try:
#     print("add the number")
#     x=int(input("x"))
#     y=int(input("2nd number "))
#     if y==0:
#         raise Exception("Deniminatoe is 0")
#     print(x/y)
#
# except Exception as e:
#     print(e)
