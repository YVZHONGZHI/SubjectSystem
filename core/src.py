# core放用户视图层
# core放核心代码

from core import admin
from core import student
from core import teacher


func_dic = {
    '0': ['退出', None],
    '1': ['管理员功能', admin.admin_view],
    '2': ['学生功能', student.student_view],
    '3': ['讲师功能', teacher.teacher_view]
}


def run():
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