# # set_1 = {"ram","shyam","hari"}
# # set_2 = {"ram", "shyam","akash","patal"}
# #
# # set_3 = set_1.intersection(set_2)
# # set_4 = set_1.union(set_2)
# # set_5 = set_1.difference(set_2)
# # print(set_3)
# # print(set_4)
# # print(set_5)
# # dict_1 = {'name':'ram','age':33}
#
# # list_1 = list(dict_1)
# #
# # print(list_1)
# # print(dict_1.get('height','height not found'))
# #
# # key = dict_1.values()
# # print(key)
# # print(set(key))
# # all = dict_1.items()
# # print(all)
# # for key,value in all:
# #     print(key, value)
#
#
# dict_1 = {
#     1:{'item1':50,
#        'item2':100,
#        'item3':20} ,
#     2:{'item1':40,
#        'item5':80}
# }
# print(dict_1)
# output = {}
# all = dict_1.items()
# for key,value in all:


#     for key1,value1 in value.items():
#         # print(key1, value1)

#         if key1 in output:
#             output[key1] += value1
#         else:
#             output[key1] = value1
# print(output)
#
# # value_1 = dict_1[1].values()
# # value_2 = dict_1[2].values()
# # key_1 = dict_1[1].keys()
# # key_2 = dict_1[2].keys()
# # print(key_1)
# # print(key_2)
# # print(value_1)
# # print(value_2)
# # print(sum)


# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def Email(self):
#         return '{}@gmail.com'.format(self.name)
#
# ramu = Person("rupeshram",20,"M")
# #
# # print(ramu.name)
# # print(ramu.age)
# # print(ramu.gender)
#
# print(ramu.Email())
# principle = int(input("Enter principle"))
# time = int(input("Enter time"))
# rate = int(input("Enter rate"))

# class Account:
#     rate = 6.5
#
#     def __init__(self, principle, time):
#         self.p = principle
#         self.t = time
#
#     def calculate(self):
#         return (self.p * self.t * Account.rate )/ 100
#
# ram = Account(100, 5)
# sita = Account(200, 3)
#
# print(ram.calculate())
# print(sita.calculate())


# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# class Teacher(Person):
#     def __init__(self,name,age,gender,subject):
#         super().__init__(name,age,gender)
#         self.subject = subject
#
#     def Subject(self):
#         return '{} is a subject'.format(self.subject)
# ram = Teacher("Ram",20,"male","Math")
# print(ram.name)
# print(ram.age)
# print(ram.gender)
# print(ram.subject)
# print(ram.subject())


# class Rectangle:
#     def __init__(self,length,bredth):
#         self.l = length
#         self.b = bredth
#     def Area(self):
#         return self.l * self.b
#
# class Square(Rectangle):
#     def __init__(self,length):
#         super().__init__(length,length)
#
#
# # length = Rectangle(20,30)
# square = Square(20)
#
# # print(length.Area())
# print(square.Area())













