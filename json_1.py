import os
import json
import datetime
from bottle import route,run , post,request


port = int(os.getenv("PORT"))

@route('/',method="POST")
def input():
    now = datetime.datetime.now()
    try:
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        c = a + b
        return {"message":str(c)+"   "+str(now)}
    except:
        return ("error")
@route('/',method="GET")
def input():
    return '<html><head><script>function loadDoc() {var xhttp = new XMLHttpRequest();xhttp.onreadystatechange = function() {if (this.readyState == 4 && this.status == 200) {var obj = JSON.parse(this.responseText);document.getElementById("demo").innerHTML = obj.message;}};xhttp.open("POST", "/", true);var formData = new FormData();formData.append("a",document.getElementById("a").value);formData.append("b",document.getElementById("b").value);xhttp.send(formData);}</script></head><body><form action = "/" method = "POST"><input type = "text" name="a" id = "a"><input type = "text" name="b" id = "b"><input type = "button" value="send" onclick = "loadDoc()"></form><div id = "demo"></div></body></html>'
 #if__name__ == '__name__':
run(host='0.0.0.0',port=port)
