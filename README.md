根据ems物流单号查询物流信息
=====================================
###   [ems站点](http://it.11185.cn/chinapostintegrate/mailqueries.a)

###  接口http://youhost/emsquery/id
	 HTTP请求方式 GET;
	 请求参数： id String
	 返回结果格式: json；
	 result: {code:Number, data:Object, reason:Number};
	 说明：code:0 成功，-1 失败 data:物流信息，reason: 1. 验证码错误，2. 请求错误，3. 网络错误, 4. 系统错误
	示例:{code: 0,
	data: "[{"mailnum":"RC239790185CN","source":"international","tracks":[{"iTEMID":"395202120","iTEMEVENTDATE":"20140402","iTEMEVENTOFFICE":"51805300","iTEMEVENTOFFICE_ZH":"深圳国际","cODE":"0","iTEMEVENTNAME":"出口总包互封开拆","iTEMEVENTTIME":"2003 ","iTEMNO":"RC239790185CN","iTEM_DEST_COUNTRY":"GB","iTEMEVENTCODE":"OP_TRNO","iTEM_DEST_COUNTRY_ZH":"英国"},{"iTEMID":"395202120","iTEMEVENTDATE":"20140402","iTEMEVENTOFFICE":"51810302","iTEMEVENTOFFICE_ZH":"深圳市国际大宗邮件处理中心","cODE":"0","iTEMEVENTNAME":"收寄局收寄","iTEMEVENTTIME":"2128 ","iTEMNO":"RC239790185CN","iTEM_DEST_COUNTRY":"GB","iTEMEVENTCODE":"A","iTEM_DEST_COUNTRY_ZH":"英国"},{"iTEMID":"395202120","iTEMEVENTDATE":"20140403","iTEMEVENTOFFICE":"51805300","iTEMEVENTOFFICE_ZH":"深圳国际","cODE":"0","iTEMEVENTNAME":"出口总包直封封发","iTEMEVENTTIME":"1022 ","iTEMNO":"RC239790185CN","iTEM_DEST_COUNTRY":"GB","iTEMEVENTCODE":"PK_EXO","iTEM_DEST_COUNTRY_ZH":"英国"},{"rEMARKS":" ","iTEMID":"395202120","iTEMEVENTDATE":"20140410","iTEMEVENTOFFICE":"GB ","iTEMEVENTOFFICE_ZH":"英国","cODE":"0","iTEMEVENTNAME":"到达进口互换局","iTEMEVENTTIME":"1557 ","iTEMNO":"RC239790185CN","iTEM_DEST_COUNTRY":"GB","iTEMEVENTCODE":"D","iTEM_DEST_COUNTRY_ZH":"英国"},{"rEMARKS":" ","iTEMID":"395202120","iTEMEVENTDATE":"20140414","iTEMEVENTOFFICE":"GB ","iTEMEVENTOFFICE_ZH":"英国","cODE":"0","iTEMEVENTNAME":"妥投","iTEMEVENTTIME":"0839 ","iTEMNO":"RC239790185CN","iTEM_DEST_COUNTRY":"GB","iTEMEVENTCODE":"I","iTEM_DEST_COUNTRY_ZH":"英国"}]}] "
	}
	 
###  接口http://youhost/emsbatchquery/ids		
	 响应： type: json；
	 说明：批量查询物流信息, ids为物流订单号用','做分隔符
	 
### todo: 根据用户指定条件进行消息推送
	
	 	   
