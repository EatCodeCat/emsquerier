'''
Created on 2014-6-19

@author: Administrator
'''
import httplib;

class HttpClient:
    
    def setHost(self, host):
        self.host = host;
        self.httpClient = httplib.HTTPConnection(self.host, 80, timeout=30);
        
    def getRequest(self, url, headers = {}):
        try:
            self.httpClient.request("GET", url, headers = headers);
            print url;
            response = self.httpClient.getresponse();
            if response.status == 200:
                return response.read();
            else:
                return "";
        except Exception, e:
            print e;
        finally:
            if self.httpClient:
                self.httpClient.close();
            
        
        