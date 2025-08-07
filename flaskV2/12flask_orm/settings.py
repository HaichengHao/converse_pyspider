"""
@File    :settings.py
@Editor  : 百年
@Date    :2025/8/6 10:28 
"""

# 公共配置
class Config:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:HHCzio20@127.0.0.1:3306/flaskv2' #配置sqlalchemy


#开发环境配置
class devConfig(Config):
    ENV = 'development'

#生产环境配置
class prodConfig(Config):
    ENV = 'production'
    DEBUG = False