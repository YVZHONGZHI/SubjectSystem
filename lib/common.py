# lib放配置信息
# lib放常用的模块,包

# 登录认证有参装饰器
def auth(role):
    # 导入要放在装饰器里
    from core import admin, student, teacher

    def login_auth(func):
        def inner(*args, **kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()
            elif role == 'student':
                if student.student_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()
            elif role == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()
            else:
                print('未出示证明,无法执行功能服务!')
        return inner
    return login_auth