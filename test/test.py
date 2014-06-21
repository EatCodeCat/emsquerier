'''
Created on 2014-6-19

@author: Administrator
'''
from util.httpclient import HttpClient;
import util.util as util;
import Image;
def testgetRequest():
    """url:http://it.11185.cn/chinapostintegrate/mailqueries.a"""
    httpclient = HttpClient();
    httpclient.setHost("it.11185.cn");
    buff = httpclient.getRequest("/chinapostintegrate/servlet/imageValidate");
    file = open("imageValidate", "wb");
    file.write(buff);
    #myfile = open("testit.j")
    print type(buff);


#testgetRequest();

print util.getImageText("../validateimage/imageValidate");


    
    
    