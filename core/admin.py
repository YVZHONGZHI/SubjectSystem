# core放用户视图层
# core放核心代码
# admin.py放管理员的视图

from interface import admin_interface
from interface import common_interface
from lib import common


admin_info = {'user': None}

# 注册功能
def register():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请确认密码:').strip()

        if password == re_password:
            flag, msg = admin_interface.admin_register_interface(username, password)

            if flag:
                print(msg)
                break

            else:
                print(msg)

        else:
            print('两次密码不一致,请重新注册')


# 登录功能
def login():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()

        flag, msg = common_interface.login_interface(username, password, user_type='admin')

        if flag:
            print(msg)
            admin_info['user'] = username
            break

        else:
            print(msg)


# 创建校区
@common.auth('admin')
def create_school():
    while True:
        school_name = input('请输入校区名称:').strip()
        school_addr = input('请输入校区地址:').strip()

        flag, msg = admin_interface.create_school_interface(school_name, school_addr, admin_info.get('user'))

        if flag:
            print(msg)
            break

        else:
            print(msg)


# 创建课程
@common.auth('admin')
def create_course():
    while True:
        flag, school_list_or_msg = common_interface.get_all_school_interface()

        if not flag:
            print(school_list_or_msg)
            break

        for index, school_name in enumerate(school_list_or_msg):
            print(f'编号:{index}   校区名:{school_name}')

        choice = input('请输入校区编号:').strip()

        if not choice.isdigit():
            print('请输入数字')
            continue

        choice = int(choice)

        if choice not in range(len(school_list_or_msg)):
            print('请输入正确编号')
            continue

        school_name = school_list_or_msg[choice]
        course_name = input('请输入需要创建的课程名称:').strip()

        flag, msg = admin_interface.create_course_interface(school_name, course_name, admin_info.get('user'))

        if flag:
            print(msg)
            break

        else:
            print(msg)


# 创建讲师
@common.auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入讲师的名字:').strip()

        flag, msg = admin_interface.create_teacher_interface(teacher_name, admin_info.get('user'))

        if flag:
            print(msg)
            break

        else:
            print(msg)


func_dic = {
    '0': ['退出管理员功能', None],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['创建校区', create_school],
    '4': ['创建课程', create_course],
    '5': ['创建讲师', create_teacher]
}


def admin_view():
    while True:
        print('===========================================')
        for w in func_dic:
            print('               ', ".".join([w, func_dic[w][0]]))
        print('===========================================')

        choice = input('请输入功能编号:').strip()
        if not choice.isdigit():
            print('功能编号非数字,请重输')
            continue

        if choice == '0':
            break

        if choice in func_dic:
            func_dic[choice][1]()

        else:
            print('请输入给定的功能编号!')