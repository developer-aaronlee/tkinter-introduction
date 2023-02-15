# def add(*args):
#     print(type(args))
#     print(args[0])
#     total = 0
#     for x in args:
#         total += x
#     return total
#
#
# print(add(3, 5, 6, 7, 10, 100))
#
#
# def calculate(num, **kwargs):
#     print(type(kwargs))
#     # for x, y in kwargs.items():
#         # print(x)
#         # print(y)
#     # print(kwargs["add"])
#     num += kwargs["add"]
#     num *= kwargs["multiply"]
#     print(num)
#
# print(calculate(2, add=1, multiply=2))


class StudentScore:
    def __init__(self, **kwargs):
        # self.student_name = kwargs["student_name"]
        # self.student_score = kwargs["student_score"]
        self.student_name = kwargs.get("student_name")
        self.student_score = kwargs.get("student_score")
        print(self.student_name)
        print(self.student_score)
        print(kwargs)


score = StudentScore(student_name="a")
print(score.student_score)


