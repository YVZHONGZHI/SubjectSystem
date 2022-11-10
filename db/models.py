# db放数据处理层
# db放数据库功能(读写功能)
# models.py管理所有的类

from db import db_handle


# 父类
class Base:

    # 把cls(对象的类),username传给db_handle.py数据处理层的select方法
    @classmethod
    def select(cls, username):
        obj = db_handle.select(cls, username)
        # 接受db_handle.py数据处理层的select方法传过来的obj
        return obj

    # 把obj(对象)传给db_handle.py数据处理层的save方法
    def save(self):
        db_handle.save(self)


# 校区类
class School(Base):

    def __init__(self, school_name, school_addr):
        self.user = school_name
        self.addr = school_addr

        self.course_list = []


# 课程类
class Course(Base):

    def __init__(self, course_name):
        self.user = course_name

        self.student_list = []


# 管理员类
class Admin(Base):

    def __init__(self, admin_user, admin_pwd):
        self.user = admin_user
        self.pwd = admin_pwd

    # 管理员创建校区方法
    def create_school(self, school_name, school_addr):
        # 把school_obj,school_name,school_addr传给models.py数据处理层的校区类
        school_obj = School(school_name, school_addr)
        school_obj.save()

    # 管理员创建课程方法
    def create_course(self, school_obj, course_name):
        # 把course_obj,course_name传给models.py数据处理层的课程类
        course_obj = Course(course_name)
        course_obj.save()
        # 把school_obj,course_name传给models.py数据处理层的校区类
        school_obj.course_list.append(course_name)
        school_obj.save()

    # 管理员创建讲师方法
    def create_teacher(self, teacher_name, teacher_pwd):
        # 把teacher_obj,teacher_name,teacher_pwd传给models.py数据处理层的讲师类
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()


# 学生类
class Student(Base):

    def __init__(self, student_name, student_pwd):
        self.user = student_name
        self.pwd = student_pwd

        self.school = None
        self.course_list = []
        self.score = {}

    # 学生选择校区方法
    def add_school(self, school_name):
        # 把student_obj,school_name传给models.py数据处理层的学生类
        self.school = school_name
        self.save()

    # 学生选择课程方法
    def add_course(self, course_name):
        # 把student_obj,course_name传给models.py数据处理层的学生类
        self.course_list.append(course_name)
        # 给学生选择的课程设置默认成绩为0
        self.score[course_name] = 0
        self.save()

        course_obj = Course.select(course_name)
        # 把course_obj,student_name传给models.py数据处理层的课程类
        course_obj.student_list.append(self.user)
        course_obj.save()


# 讲师类
class Teacher(Base):

    def __init__(self, teacher_name, teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd

        self.course_list_from_teacher = []

    # 讲师查看所教授课程方法
    def show_course(self):
        return self.course_list_from_teacher

    # 讲师选择所教授课程方法
    def add_course(self, course_name):
        # 把teacher_obj,course_name传给models.py数据处理层的讲师类
        self.course_list_from_teacher.append(course_name)
        self.save()

    # 讲师查看课程下学生方法
    def get_student(self, course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list

    # 讲师给学生打分方法
    def change_score(self, course_name, student_name, score):
        student_obj = Student.select(student_name)
        # 把student_obj,course_name,score传给models.py数据处理层的学生类
        student_obj.score[course_name] = score
        student_obj.save()