# @Author    : 百年
# @FileName  :upload.py
# @DateTime  :2025/7/4 19:13
from flask import Blueprint,request,redirect,url_for

uPload = Blueprint(name='upload',import_name=__name__)

@uPload.route('/upload',methods=['POST'])

def upload_route():
    file = request.files.get('file')
    if file:
        filename = file.filename
        file.save(f'uploads/{filename}')
        return f'File upload success'
    return 'No file upload'
