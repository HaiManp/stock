# -*- coding: utf-8 -*-

import random
import requests
from lxml import etree
from server.config.conf import headers


def Request(url):
    """Get data"""
    header = random.choice(headers)[0]
    response = requests.get(url, headers=header)
    try:
        if response.status_code == 200:
            # print(response.text)
            return response.text
    except:
        print("request erro!")

def Getdata(url):
    """获取股票数据"""
    result = etree.HTML(Request(url))
    retdatas = []
    try:
        title = result.xpath('//*[@id="divContent"]/center/table/tr[2]/td/text()')[0]
        print(title)
        for item in result.xpath('//*[@id="ctl16_contentdiv"]/table/tr')[1:1095]:
            time = item.xpath('td[1]/a/text()')[0]
            open = float(item.xpath('td[2]/text()')[0])
            close = float(item.xpath('td[5]/text()')[0])
            lowest = float(item.xpath('td[4]/text()')[0])
            highest = float(item.xpath('td[3]/text()')[0])
            retdata = [time, open, close, lowest, highest]
            retdatas.append(retdata)
        # print(retdatas)
        return retdatas[::-1]
    except:
        print("erro")


















