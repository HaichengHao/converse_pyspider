 

Flask中的[ORM](https://so.csdn.net/so/search?q=ORM&spm=1001.2101.3001.7020)（Object-Relational Mapping，对象关系映射）是一种编程技术，用于在关系数据库和对象程序语言之间转换数据。在Flask框架中，最常用的ORM工具是SQLAlchemy，通过Flask-SQLAlchemy扩展集成到Flask应用中。以下是Flask中ORM的详细介绍：

1.  **安装Flask-SQLAlchemy**：  
    要使用Flask的ORM功能，首先需要安装Flask-SQLAlchemy扩展。可以通过pip安装：
    
    ```
    pip install flask-sqlalchemy
    ```
    
    如果需要连接特定的数据库，比如MySQL，还需要安装对应的数据库驱动，例如：
    
    ```
    pip install mysqlclient
    ```
    
2.  **配置数据库URI**：  
    在Flask应用中，需要配置数据库连接URI，告诉SQLAlchemy如何连接到数据库。例如，对于SQLite数据库，配置可能如下：
    
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    ```
    
    对于MySQL数据库，配置可能如下：
    
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
    ```
    
3.  **初始化SQLAlchemy**：  
    在Flask应用中，导入并初始化SQLAlchemy：
    
    ```python
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)
    ```
    
4.  **定义模型**：  
    通过创建类来定义数据模型，这些类继承自`db.Model`。每个类对应数据库中的一个表，类的属性对应表的列。例如：
    
    ```python
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
    ```
    
5.  **创建数据库和表**：  
    在定义了模型后，可以使用`db.create_all()`来创建数据库和表：
    
    ```python
    with app.app_context():
        db.create_all()
    ```
    
6.  **CRUD操作**：
    
    *   **创建（Create）**：创建一个新的记录实例，并将其添加到会话中，然后提交会话以保存到数据库。
        
        ```python
        new_user = User(username='john_doe', email='john@example.com')
        db.session.add(new_user)
        db.session.commit()
        ```
        
    *   **读取（Read）**：查询数据库中的记录。
        
        ```python
        users = User.query.all()  # 获取所有用户
        user = User.query.get(user_id)  # 通过主键获取单个用户
        ```
        
    *   **更新（Update）**：修改记录的字段值，并提交会话以更新数据库。
        
        ```python
        user = User.query.get(user_id)
        user.username = 'new_username'
        db.session.commit()
        ```
        
    *   **删除（Delete）**：从数据库中删除记录。
        
        ```python
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        ```
        
7.  **查询操作**：  
    SQLAlchemy提供了丰富的查询功能，可以执行基本和复杂查询，包括排序和分页：
    
    ```python
    users = User.query.order_by(User.username).paginate(page=1, per_page=10)
    ```
    
8.  **数据库迁移**：  
    使用Flask-Migrate扩展管理数据库迁移，它基于Alembic。可以通过以下命令初始化迁移环境、创建迁移脚本和应用迁移：
    
    ```shell
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```
    
9.  **执行原始SQL**：  
    虽然推荐使用ORM方式操作数据库，但在某些情况下可能需要执行原始SQL语句。可以通过`db.session.execute()`方法执行：
    
    ```python
    result = db.session.execute('SELECT * FROM user')
    ```
    

通过上述步骤，可以在Flask应用中利用ORM进行数据库操作，从而提高开发效率并减少直接编写SQL语句带来的风险。

 

![](https://i-blog.csdnimg.cn/direct/ef5a9e4ec9dc4185a57ee2caa9c4d894.jpeg) 聪明的墨菲特i

![](https://g.csdnimg.cn/extension-box/2.0.0/image/weixin.png)微信名片

![](https://g.csdnimg.cn/extension-box/2.0.0/image/ic_move.png)

本文转自 <https://blog.csdn.net/weixin_39347873/article/details/142919341>，如有侵权，请联系删除。