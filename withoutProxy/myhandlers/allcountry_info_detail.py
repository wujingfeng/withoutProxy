#彭青山
#全国奖惩记录
import re
import datetime
import json

import requests

from withoutProxy.config.database import *

def allcountry_info_detail(response):
    print('-----allcountry_info_detail-----')
    data_list = []
    js = json.loads(response.text)['rows']
    pages = json.loads(response.text)['pageObj']['maxPage']
    for i in range(int(pages)):
        title = js[i]['itemname']
        xmmc = js[i]['projectname']
        qymc = js[i]['corpname']
        jddw = js[i]['publicUnit']
        jddate = js[i]['subTime']
        dlink = response.url
        type = js[i]['rewardType']
        fnumber = js[i]['dispatchNumber']
        content = js[i]['content']
        tmp_data = {
            'title': title,
            'xmmc': xmmc,
            'qymc': qymc,
            'jddw': jddw,
            'jddate':jddate,
            'dlink': dlink,
            'type': type,
            'fnumber': fnumber,
            'nr': content,
        }
        data_list.append(tmp_data)
    return_data = {'items': [{'data': data_list}]}
    return return_data