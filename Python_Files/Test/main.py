# # import random
# # # new_num = [n*2 for n in range(1, 5)]
# # #
# # # print(new_num)
# # # name =["akas", "maxyt","rok","akx" ]
# # # new = [iteam.capitalize() for iteam in name if len(iteam) >= 4]
# # # print(new)
# # import random
# #
# # names = ['Asha', 'Michael', 'Arjun', 'Roland']
# #
# # dict = {
# #     name: random.randrange(1, 100) for name in names
# # }
# # print(dict)
# #
# # pass_student = {
# #     student: score for (student, score) in dict.items() if score > 60
# # }
# # print(pass_student)
#
# def add(*args):
#     c = 1
#     for n in args:
#         c += n
#     return c
#
#
# print(add(2, 3, 5, 6))




# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
