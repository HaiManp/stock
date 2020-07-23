# -*- coding: utf-8 -*

#author:  Haker
#contact: HaiManp@163.com
#time:    2020/6/19 10:00

"""response 统一返回状态码"""
#请求成功返回code:200
CODE_SUCCESS = 200
MSG_SUCCESS = 'Request successful'
#token失效返回code:401
CODE_TOKEN_ERROR = 401
MSG_TOKEN_ERROR = 'Token error'
#服务器内部错误返回code:500
CODE_SERVER_ERROR = 500
MSG_SERVER_ERROR = 'Server error'
#资源以移动到其它url返回code:301
CODE_MOVE_OTHER = 301
MSG_MOVE_OTHER = 'Url error'
#访问页面不存在返回code=404
CODE_RESOURCE_ERROR = 404
MSG_RESOURCE_ERROR = 'Page error'
#api不存在返回code;402
CODE_API_ERROR = 402
MSG_API_ERROR = 'Api is not found'
#缺少参数返回code:502
CODE_PAR_ERROR = 502
MSG_PAR_ERROR = 'Missing necessary parameters'