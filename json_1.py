import os
import json
import datetime
from bottle import route,run , post,request


port = int(os.getenv("PORT"))

@route('/',mehtod="GET")
def input():
    now = datetime.datetime.now()
    try:
        a = int(request.query['a'])
        b = int(request.query['b'])
        c = a + b
        return str(c),"   ",str(now)
    except:
        return ("กรุณาระบุตัวเลข")
 #if__name__ == '__name__':
run(host='0.0.0.0',port=port)
