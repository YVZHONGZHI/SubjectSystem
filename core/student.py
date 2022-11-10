# core放用户视图层
# core放核心代码
# student.py放学生的视图

from interface import common_interface
from interface import student_interface
from lib import common


student_info = {'user': None}

# 注册功能
def register():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请确认密码:').strip()

        if password == re_password:
            flag, msg = student_interface.student_register_interface(username, password)

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

        flag, msg = common_interface.login_interface(username, password, user_type='student')

        if flag:
            print(msg)
            student_info['user'] = username
            break

        else:
            print(msg)


# 选择校区
@common.auth('student')
def choice_school():
    while True:
        flag, school_list = common_interface.get_all_school_interface()

        if not flag:
            print(school_list)
            break

        for index, school_name in enumerate(school_list):
            print(f'编号:{index}   校区名:{school_name}')

        choice = input('请输入选择的校区编号:').strip()

        if not choice.isdigit():
            print('请输入给定的功能编号!')
            continue

        choice = int(choice)

        if choice not in range(len(school_list)):
            print('请输入给定的功能编号!')
            continue

        school_name = school_list[choice]

        flag, msg = student_interface.add_school_interface(school_name, student_info.get('user'))

        if flag:
            print(msg)
            break

        else:
            print(msg)
            break


# 选择课程
@common.auth('student')
def choice_course():
    while True:
        flag, course_list = student_interface.get_course_list_interface(student_info.get('user'))

        if not flag:
            print(course_list)
            break

        for index, school_name in enumerate(course_list):
            print(f'编号:{index}   课程名:{school_name}')

        choice = input('请输入选择的课程编号:').strip()

        if not choice.isdigit():
            print('请输入给定的功能编号!')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('请输入给定的功能编号!')
            continue

        course_name = course_list[choice]

        flag, msg = student_interface.add_course_interface(course_name, student_info.get('user'))

        if flag:
            print(msg)
            break

        else:
            print(msg)
            break


# 查看成绩
@common.auth('student')
def check_score():
    score = student_interface.check_score_interface(student_info.get('user'))

    if not score:
        print('没有课程,请先选择课程')

    print(score)


func_dic = {
    '0': ['退出学生功能', None],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['选择校区', choice_school],
    '4': ['选择课程', choice_course],
    '5': ['查看成绩', check_score]
}


def student_view():
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