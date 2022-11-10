# interface放逻辑接口层
# student_interface.py放学生接口

from db import models


# 学生注册接口
def student_register_interface(username, password):
    student_obj = models.Student.select(username)

    if student_obj:
        return False, f'用户名[{username}]已存在!'

    student_obj = models.Student(username, password)
    student_obj.save()
    msg = f'[{username}]注册成功!'
    return True, msg


# 学生选择校区接口
def add_school_interface(school_name, student_name):
    student_obj = models.Student.select(student_name)

    if student_obj.school:
        return False, '当前学生已经选择过校区了!'

    # 把student_obj,school_name传给models.py数据处理层的学生类中的学生选择校区方法调用models.py数据处理层的学生类
    student_obj.add_school(school_name)
    return True, f'选择校区[{school_name}]成功!'


# 学生选择课程接口
def add_course_interface(course_name, student_name):
    student_obj = models.Student.select(student_name)

    if course_name in student_obj.course_list:
        return False, '当前学生已经选择过课程了!'

    # 把student_obj,course_name传给models.py数据处理层的学生类中的学生选择课程方法调用models.py数据处理层的学生类
    student_obj.add_course(course_name)
    return True, f'添加课程[{course_name}]成功!'


# 学生查看成绩接口
def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)

    if student_obj.score:
        return student_obj.score


# 学生课程接口
def get_course_list_interface(student_name):
    # 获取学生对象
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school

    if not school_name:
        return False, '没有校区,请先选择校区'

    # 获取校区对象的课程列表
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list

    if not course_list:
        return False, '没有课程,请先联系管理员创建'

    return True, course_list