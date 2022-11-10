# interface放逻辑接口层
# admin_interface.py放管理员接口

from db import models


# 管理员注册接口
# 接受admin.py管理员的视图传过来的username和password
def admin_register_interface(username, password):
    # 把Admin,username传给models.py数据处理层的Admin类中的select方法调用db_handle.py数据处理层的select方法
    admin_obj = models.Admin.select(username)

    # 根据admin_obj判断
    if admin_obj:
        # 把结果传给admin.py管理员的视图
        return False, f'用户名[{username}]已存在!'

    # 把username,password传给models.py数据处理层的管理员类后结果实例化admin_obj对象
    admin_obj = models.Admin(username, password)
    # 把admin_obj传给models.py数据处理层的管理员类中的save方法调用db_handle.py数据处理层的save方法
    admin_obj.save()
    # 把结果传给admin.py管理员的视图
    msg = f'[{username}]注册成功!'
    return True, msg


# 管理员创建校区接口
def create_school_interface(school_name, school_addr, admin_name):
    school_obj = models.School.select(school_name)

    if school_obj:
        return False,'当前校区已存在!'

    admin_obj = models.Admin.select(admin_name)
    # 把admin_obj,school_name,school_addr传给models.py数据处理层的管理员类中的管理员创建校区方法调用models.py数据处理层的校区类
    admin_obj.create_school(school_name, school_addr)
    return True, f'校区[{school_name}]创建成功!'


# 管理员创建课程接口
def create_course_interface(school_name, course_name, admin_name):
    school_obj = models.School.select(school_name)

    if course_name in school_obj.course_list:
        return False, '当前课程已存在!'

    admin_obj = models.Admin.select(admin_name)
    # 把admin_obj,school_obj,course_name传给models.py数据处理层的管理员类中的管理员创建课程方法调用models.py数据处理层的课程类
    admin_obj.create_course(school_obj, course_name)
    return True, f'[{course_name}]课程创建成功,绑定给[{school_name}]校区!'


# 管理员创建讲师接口
def create_teacher_interface(teacher_name, admin_name, teacher_pwd='123'):
    teacher_obj = models.Teacher.select(teacher_name)

    if teacher_obj:
        return False, '当前讲师已存在!'

    admin_obj = models.Admin.select(admin_name)
    # 把admin_obj,teacher_name,teacher_pwd传给models.py数据处理层的管理员类中的管理员创建讲师方法调用models.py数据处理层的讲师类
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True, f'[{teacher_name}]讲师创建成功!'