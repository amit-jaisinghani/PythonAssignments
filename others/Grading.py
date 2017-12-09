# grade = int(input("Grade? "))
#
# """if else"""
# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("D")
# else:
#     print("F")
#
# """While Loop"""
#
# while grade > 50:
#     print(grade)
#     grade = int(input("Grade? "))
#
# print("while end")

# """For Loop"""
#
# for x in (1,10,3):
#     print(type(x))
#
# """range(from,to,skip) - skip is like i++"""
# for x in range(1,10,3):
#     print(type(x))
#
# def gradeIt(x, y="thand"):
#     print("test() ",x, y)
#
# gradeIt(1)
# gradeIt(2)
# gradeIt(13,"c")

def add(x,y):
    print("add(): ",x,"+",y)
    return x+y

# def add(x):
#     print("add(): ", x)
#     return x
#
# add(1)
add(1,2)