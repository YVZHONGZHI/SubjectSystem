# interface放逻辑接口层
# common_interface.py放公共接口(多个接口(admin_interface.py、student_interface.py、teacher_interface.py)相似数据与功能的集合体)

import os
from conf import settings
from db import models


# 登录接口
def login_interface(username, password, user_type):
    if user_type == 'admin':
        obj = models.Admin.select(username)

    elif user_type == 'student':
        obj = models.Student.select(username)

    elif user_type == 'teacher':
        obj = models.Teacher.select(username)

    else:
        return False,'登录角色不对,请输入角色'

    if obj:
        if password == obj.pwd:
            return True,'登录成功!'
        else:
            return False,'密码错误!'
    else:
        return False,'用户名不存在!'


# 校区名称接口
def get_all_school_interface():
    school_dir = os.path.join(settings.DB_PATH,'School')

    if os.path.exists(school_dir):
        school_list = os.listdir(school_dir)
        return True, school_list

    else:
        return False, '没有校区,请先联系管理员'


# 课程名称接口
def get_course_in_school_interface(school_name):
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list

    if not course_list:
        return False, '该校区没有课程'

    return True, course_list