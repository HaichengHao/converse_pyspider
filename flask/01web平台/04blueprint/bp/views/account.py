from flask import Blueprint, render_template
from .db_helper import dbverify

account = Blueprint(name='account', import_name=__name__)


@account.route('/getall_info')
def getall_info():
    info = dbverify(sql="select * from user_info")
    return render_template('userinfo.html', info=info)
