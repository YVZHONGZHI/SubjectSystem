# interface放逻辑接口层
# teacher_interface.py放讲师接口

from db import models


# 讲师查看所教授课程接口
def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    course_list = teacher_obj.show_course()

    if not course_list:
        return False, '没有所教授课程'

    return True, course_list


# 讲师选择所教授课程接口
def add_course_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    course_list = teacher_obj.course_list_from_teacher

    if course_name in course_list:
        return False, '该课程已存在!'

    # 把teacher_obj,course_name传给models.py数据处理层的讲师类中的讲师选择所教授课程方法调用models.py数据处理层的讲师类
    teacher_obj.add_course(course_name)
    return True, f'添加课程[{course_name}]成功!'


# 讲师查看课程下学生接口
def get_student_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    student_list = teacher_obj.get_student(course_name)

    if not student_list:
        return False, '学生没有选择该课程'

    return True, student_list


# 讲师给学生打分接口
def change_score_interface(course_name, student_name, score, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    # 把teacher_obj,course_name,student_name,score传给models.py数据处理层的讲师类中的讲师给学生打分方法调用models.py数据处理层的学生类
    teacher_obj.change_score(course_name, student_name, score)
    return True, '给学生打分完成!'