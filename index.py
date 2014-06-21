#!/usr/bin/python  
#-*-coding:utf-8-*-
from flask import Flask
import json;
from ems.querier import EmsQuerier;
from flask import jsonify 
#sucess:{code:0,data:{}}

app = Flask(__name__)

#请求ems邮件信息<id>邮件id
@app.route('/emsquery/<id>')
def emsQuery(id):
    '''fail: {code: -1, reason:0. 物流单号为空 1. 验证码错误，2. 请求错误，3. 网络错误, 4. 系统错误}
       sucess:{code:0,data:{}}
    '''
    if not id:
       return '{"code": -1, "reason":0. }';
    q = EmsQuerier()
    data = q.query(id);
    return jsonify(data);
@app.route('/emsbatchquery/<ids>')
def emsBatchQuery(ids):
    if not ids:
       return '{"code": -1, "reason":0. }';
    arr  = ids.split(',');
    dataArray = {};
    i = 0;
    for id in arr:
        if not id:
            continue;
        q = EmsQuerier()
        data = q.query(id);
        i += 1;
        dataArray[i] = data;
    return jsonify(dataArray);

@app.route("/")
def index():
    return 'ems query!!!!'

if __name__ == '__main__':
    #app.debug = True
    app.run();