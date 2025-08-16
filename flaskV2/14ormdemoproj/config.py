"""
@File    :config.py
@Editor  : 百年
@Date    :2025/8/6 16:48
"""
import os
#读取env中的配置项

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') #读取.env文件中的配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 2. 禁用追踪修改（强烈建议关闭，节省性能）
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 3. 是否打印 SQL 语句（开发时有用）
    SQLALCHEMY_ECHO = True  # 开发时打开，生产关闭

    # 4. 连接池大小（默认 5）
    SQLALCHEMY_POOL_SIZE = 10

    # 5. 连接池超时时间（秒）
    SQLALCHEMY_POOL_TIMEOUT = 30

    # 6. 连接空闲多久后自动断开（秒）
    SQLALCHEMY_POOL_RECYCLE = 1800  # 30分钟

    # 7. 启用连接池预检（防止 MySQL 8小时断开）
    SQLALCHEMY_POOL_PRE_PING = True  # 推荐开启

    # 8. 是否自动提交事务（一般不开启，手动控制更好）
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = False  # 已废弃，不推荐使用
# 配置开发配置
class devConfig(Config):
    DEBUG = True
    ENV = 'development'

# 配置生产配置
class prodConfig(Config):
    DEBUG = False
    ENV = 'production'

#映射字典
config = {
    'development':devConfig,
    'production':prodConfig,
    'default':devConfig
}
