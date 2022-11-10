# conf放配置文件(日志的路径,数据库的路径)
# 不要去导入core的东西
# 获取项目根路径

import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR,'db')