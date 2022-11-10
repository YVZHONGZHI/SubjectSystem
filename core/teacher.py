# core放用户视图层
# core放核心代码
# teacher.py放讲师的视图

from interface import common_interface
from interface import teacher_interface
from lib import common


teacher_info = {'user': None}

# 登录功能
def login():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()

        flag, msg = common_interface.login_interface(username, password, user_type='teacher')

        if flag:
            print(msg)
            teacher_info['user'] = username
            break

        else:
            print(msg)


# 查看所教授课程
@common.auth('teacher')
def check_course():
    flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))

    if flag:
        print(course_list)

    else:
        print(course_list)


# 选择所教授课程
@common.auth('teacher')
def choose_course():
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

        flag2, course_list = common_interface.get_course_in_school_interface(school_name)

        if not flag2:
            print(course_list)
            break

        for index2, course_name in enumerate(course_list):
            print(f'编号:{index2}   课程名:{course_name}')

        choice2 = input('请输入选择的课程编号:').strip()

        if not choice2.isdigit():
            print('请输入给定的功能编号!')
            continue

        choice2 = int(choice2)

        if choice2 not in range(len(course_list)):
            print('请输入给定的功能编号!')
            continue

        course_name = course_list[choice2]

        flag3, msg = teacher_interface.add_course_interface(course_name, teacher_info.get('user'))

        if flag3:
            print(msg)
            break

        else:
            print(msg)


# 查看课程下学生
@common.auth('teacher')
def check_student_from_course():
    while True:
        flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))

        if not flag:
            print(course_list)
            break

        for index, course_name in enumerate(course_list):
            print(f'编号:{index}   课程名:{course_name}')

        choice = input('请输入选择的课程编号:').strip()

        if not choice.isdigit():
            print('请输入给定的功能编号!')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('请输入给定的功能编号!')
            continue

        course_name = course_list[choice]

        flag2, student_list = teacher_interface.get_student_interface(course_name, teacher_info.get('user'))

        if flag2:
            print(student_list)
            break

        else:
            print(student_list)
            break


# 给学生打分
@common.auth('teacher')
def change_score_from_student():
    while True:
        flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))

        if not flag:
            print(course_list)
            break

        for index, course_name in enumerate(course_list):
            print(f'编号:{index}   课程名:{course_name}')

        choice = input('请输入选择的课程编号:').strip()

        if not choice.isdigit():
            print('请输入给定的功能编号!')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('请输入给定的功能编号!')
            continue

        course_name = course_list[choice]

        flag2, student_list = teacher_interface.get_student_interface(course_name, teacher_info.get('user'))

        if not flag2:
            print(student_list)
            break

        for index2, student_name in enumerate(student_list):
            print(f'编号:{index2}   学生名:{student_name}')

        choice2 = input('请输入选择的学生编号:').strip()

        choice2 = int(choice2)

        if choice2 not in range(len(student_list)):
            print('请输入给定的功能编号!')
            continue

        student_name = student_list[choice2]

        score = input('请给学生打分:').strip()
        if not score.isdigit():
            continue

        score = int(score)

        flag3, msg = teacher_interface.change_score_interface(course_name, student_name, score, teacher_info.get('user'))

        if flag3:
            print(msg)
            break


func_dic = {
    '0': ['退出讲师功能', None],
    '1': ['登录', login],
    '2': ['查看所教授课程', check_course],
    '3': ['选择所教授课程', choose_course],
    '4': ['查看课程下学生', check_student_from_course],
    '5': ['给学生打分', change_score_from_student]
}


def teacher_view():
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