# 基于Python的选课系统
管理员

    注册功能
    
        1.用户在视图层输入用户名与密码,交给接口层
        
        2.接口层调用数据层中的models.select进行校验
        
        3.若不存在则创建,并将注册成功返回给视图层
        
    登录功能
    
        1.用户在视图层输入用户名与密码,交给接口层
        
        2.接口层调用数据层中的models.select进行校验
        
        3.若存在则校验密码,并将登录成功返回给视图层
        
    创建校区
    
        1.让用户输入校区名与校区地址
        
        2.调用管理员创建校区接口
        
        3.判断校区是否存在,若存在不让创建
        
        4.若不存在,则调用接口层创建校区,获取管理员对象的创建校区方法保存校区
        
        5.将结果返回给视图层
        
    创建课程
    
        1.获取所有校区,并打印,让用户选择
        
        2.获取用户选择的校区与创建的课程,交给接口层
        
        3.接口层调用管理员对象中的创建课程方法,保存课程对象
        
        4.课程需要绑定给校区对象,最终将创建成功的结果返回给视图层
        
    创建讲师
    
        1.让用户输入讲师名称
        
        2.调用接口层,接口层中设置默认密码123,调用数据层
        
        3.判断讲师是否存在,不存在则调用管理员对象中的创建讲师方法
        
        4.保存讲师对象,并将结果返回视图层
***
学生

    注册功能
    
        1.用户在视图层输入用户名与密码,交给接口层
        
        2.接口层调用数据层中的models.select进行校验
        
        3.若不存在则创建,并将注册成功返回给视图层
        
    登录功能
    
        1.用户在视图层输入用户名与密码,交给接口层
        
        2.接口层调用数据层中的models.select进行校验
        
        3.若存在则校验密码,并将登录成功返回给视图层
        
    选择校区
    
        1.获取所有校区,让学生选择,将选择的校区传给接口层
        
        2.接口层判断当前学生是否选择过校区
        
        3.若没有选择,则调用学生对象中的添加校区方法
        
        4.将添加后消息返回给视图层
        
    选择课程
    
        1.先获取当前学生所在校区的所有课程并选择
        
        2.接口层将选择后课程,调用数据层的添加课程方法保存
        
        3.学生对象中课程列表添加该课程,设置课程分数默认值为0
        
        4.最终将结果返回给视图层
        
    查看成绩
    
        1.直接调用接口层
        
        2.接口层调用数据层中的查看成绩方法
        
        3.返回成绩给视图层并打印
***
讲师

    登录功能
    
        1.用户在视图层输入用户名与密码,交给接口层
        
        2.接口层调用数据层中的models.select进行校验
        
        3.若存在则校验密码,并将登录成功返回给视图层
        
    查看所教授课程
    
        1.直接调用接口层,获取讲师对象下课程列表数据
        
        2.若有则打印,没有则退出
        
    选择所教授课程
    
        1.调用接口层中的选择所教授课程接口,调用数据层中该课程下所有的学生返回给视图层
        
        2.打印所有的课程,让讲师选择,若讲师课程中有该课程则不让添加
        
        3.没有则调用讲师对象中的添加课程方法进行添加
        
    查看课程下学生
    
        1.直接获取讲师对象下所有的课程,选择课程
        
        2.从讲师对象中,调用查看课程下学生方法,获取课程对象下所有的学生,返回给视图层
        
        3.视图层打印该课程下所有的学生
        
    给学生打分
    
        1.直接获取讲师对象下所有的课程,选择课程
        
        2.从讲师对象中,调用查看课程下学生方法,获取课程对象下所有的学生,返回给视图层
        
        3.视图层打印该课程下所有的学生,并让用户选择给学生打分方法
        
        4.调用讲师给学生打分接口,获取讲师对象,调用对象中的给学生打分方法
        
        5.获取学生对象中的score_dict分数字典,进行修改
