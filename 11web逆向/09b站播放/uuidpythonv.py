"""
@File    :uuidpythonv.py
@Editor  : 百年
@Date    :2025/4/6 17:45 
"""
import uuid
import time
# print(uuid.uuid4())

def gen_uuid():
    uuid_sec = str(uuid.uuid4())
    time_sec = str(int(time.time()*1000 % 1e5))
    time_sec = time_sec.ljust(5,"0")

    return f"{uuid_sec}{time_sec}".upper() + 'infoc'
_uuid = gen_uuid()
print(_uuid)