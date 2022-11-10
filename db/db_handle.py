# db放数据处理层
# db放数据库功能(读写功能)
# db_handle.py保存对象,查看对象

import os
import pickle
from conf import settings


# 保存数据
# 接受models.py数据处理层传过来的obj(对象)
def save(obj):
    # 把对象的类的名字返回class_name,class_name为文件夹的名字
    class_name = obj.__class__.__name__
    user_path = os.path.join(settings.DB_PATH, class_name)

    # 判断文件夹是否存在
    if not os.path.exists(user_path):
        # 不存在就创建
        os.mkdir(user_path)

    # 将用户名做为文件夹名放在类名文件夹下面
    user_dir_path = os.path.join(user_path, obj.user)

    # 打开文件保存
    with open(user_dir_path, 'wb') as w:
        pickle.dump(obj, w)


# 查看数据
# 接受models.py数据处理层传过来的cls(对象的类),username
def select(cls, username):
    # 把cls的名字返回class_name,class_name为文件夹的名字
    class_name = cls.__name__
    user_path = os.path.join(settings.DB_PATH, class_name)

    if not os.path.exists(user_path):
        os.mkdir(user_path)

    user_dir_path = os.path.join(user_path, username)

    if os.path.exists(user_dir_path):

        with open(user_dir_path, 'rb') as w:
            obj = pickle.load(w)
            return obj