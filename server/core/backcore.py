# -*- coding: utf-8 -*

from flask import request, Blueprint, jsonify
from ..restful.code import *
from ..config.conf import url
from ..spider.spidercore import Getdata
from ..config.codeconf import *


api = Blueprint('api', __name__)

@api.route('/result', methods=['GET'])
def core():
    """请求成功返回"""
    if request.method == 'GET':
        param = request.args
        codetype = str(param.get('keyword'))
        urls = url + codetype
        return_data = Getdata(urls)
        """"返回数据到前端"""
        requestdata = Response(code=CODE_SUCCESS,
                               status=0,message=MSG_SUCCESS,data={
            "keyword": return_data
        })
        if requestdata:
            print(requestdata.content)
            return jsonify(requestdata.content)
        else:
            """请求失败返回"""
            return jsonify(Response(code=CODE_SUCCESS,
                                    status=0,message=MSG_SUCCESS,data={
                "keworld": "查询失败请输入正确的股票代码!",
            }))
    else:
        return jsonify(Response(code=CODE_RESOURCE_ERROR,
                                status=0,message=CODE_RESOURCE_ERROR,data={
                "keyword": "请求方式错误，访问页面不存在"
            }))

