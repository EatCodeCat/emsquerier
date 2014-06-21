'''
Created on 2014-6-19

@author: Administrator
'''
from util.httpclient import HttpClient;
import util.util as util;
import json;
import random;

class EmsQuerier:
    '''"url:http://it.11185.cn
        query: http://it.11185.cn/chinapostintegrate/trackmailById.a?mailId=RC239790185CN&imageValid=8065
        validateimage: /chinapostintegrate/servlet/imageValidate
    '''
   
    IMAGEERROR = "imgError"
    IMAGEPATH = 'validateimage\\'
    FILEPREFIX = 'validateimage';
    HOST = 'it.11185.cn'
    QUERYIMAGEVALIDATEURL = '/chinapostintegrate/servlet/imageValidate?t=%s';
    MAILQUERYURL =  "/chinapostintegrate/trackmailById.a?mailId=%s&imageValid=%s";
    checkcodeUrl ="/chinapostintegrate/checkCode.a?imageValid=%s";

    def __init__(self):
        self.httpClient = HttpClient();
        self.httpClient.setHost(EmsQuerier.HOST);
        self.headers = {'Referer':'http://it.11185.cn/chinapostintegrate/mailqueries.a','Cookie':'JSESSIONID=xK2nTlZJ8GTwZ0VL27DbWnyfLQ5Gwg780Fn1jtwLsZfp1JF2MsyZ!-629284288'}
    
    def query(self, id):
       filename = EmsQuerier.FILEPREFIX + id;
       checkcode = self.checkImageValidate(filename);
       if  checkcode:
            checkcode = checkcode.strip();
            url = EmsQuerier.MAILQUERYURL %(id, checkcode);
            jsonResult = self.httpClient.getRequest(url, self.headers);
            if jsonResult == '':
                return {"code":-1, 'reasion':util.appContent['neterror']};
            data = json.loads(jsonResult)
            if data["jsonStr"] == EmsQuerier.IMAGEERROR:
                return {"code":-1, 'reasion':util.appContent['imagevalidateerror']};
            return {"code":0, 'data':data['jsonStr']};
       else :
           return {"code":-1, 'reasion':util.appContent['imagevalidateerror']};

    def checkImageValidate(self, filename):
        
        buff = self.httpClient.getRequest(EmsQuerier.QUERYIMAGEVALIDATEURL %random.random(), self.headers);
        return util.getImageTextBuff(buff);