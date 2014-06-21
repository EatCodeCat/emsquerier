根据ems物流单号查询物流信息
=====================================
###   [ems站点](http://it.11185.cn)

###  接口http://youhost/emsquery/<id>		
	 响应： type: json；
	 result: {code:Number, data:Object, reason:Number};
	 说明：code:0 成功，-1 失败.
	 	   data:物流信息，reason: 1. 验证码错误，2. 请求错误，3. 网络错误, 4. 系统错误
	 	   