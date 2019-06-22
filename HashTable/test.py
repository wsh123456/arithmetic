class Student():
    def __init__(self, grade, cls, firstname, lastname):
        self.grade = grade
        self.cls = cls
        self.firstname = firstname
        self.lastname = lastname

    # 为自定义类 重写hash函数
    def __hash__(self):
        B = 31  # 随意取一个B
        hash = 0
        hash = hash * B + self.grade.__hash__()
        hash = hash * B + self.cls.__hash__()
        hash = hash * B + self.firstname.lower().__hash__()
        hash = hash * B + self.lastname.lower().__hash__()
        return hash

    # 判断两个类是否相等
    def __eq__(self, other):
        # if self == other:
        #     return True
        if other is None:
            return False
        if self.__class__ != other.__class__:
            return False

        return self.grade == other.grade \
               and self.cls == self.cls \
               and self.firstname.lower() == other.firstname.lower() \
               and self.lastname.lower() == other.lastname.lower()


a = 42
print(hash(a))
print(a.__hash__())

b = -42
print(b.__hash__())

c = 3.1415926
print(c.__hash__())

d = "str"
print(d.__hash__())

student = Student(3, 2, "BoBo", "Hua")
print(student.__hash__())
student2 = Student(3, 2, "bobo", "hua")
print(student2.__hash__())
# 当哈希值相等的时候，通过eq函数判断值是否相同
print(student.__eq__(student2))