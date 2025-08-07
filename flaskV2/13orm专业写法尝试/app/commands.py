"""
@File    :commands.py
@Editor  : 百年
@Date    :2025/8/6 17:05 
"""
import click
from flask.cli import with_appcontext
from .extensions import db

@click.command()
@with_appcontext
def init_db():
    '''初始化数据库'''
    db.create_all()
    click.echo('数据库已创建')

@click.command()
@with_appcontext
def drop_db():
    db.drop_all()
    click.echo('数据库已经清空')

@click.command()
@with_appcontext
def hello():
    click.echo('你好flask')

