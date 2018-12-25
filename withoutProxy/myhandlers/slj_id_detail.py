import re
import requests
import json
from withoutProxy.config.database import *

# 水利建设 公司id
def slj_id_detail(response):
    print('-----gljs_id_detail-----')
    comp =  response.xpath('//*[@id="divgrid"]/table/tbody/tr[1]/td[2]/a/@href')
    comp_id = re.findall(r'id=(.*?)$', comp[0].root, re.S)[0]
    try:
        return_data = {
            'items': [
                {
                    'data': [
                        {
                            'comp_id': comp_id,


                        }
                    ]
                }
            ]
        }
        return return_data
    except:
        rtn_data = {
            'msg': 'find empty comp: '+response.url
        }
        return rtn_data

