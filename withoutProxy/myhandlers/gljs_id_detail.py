import re
import requests
import json
from withoutProxy.config.database import *

# # 公路建设 id
def gljs_id_detail(response):
    print('-----gljs_id_detail-----')
    html = response.text
    text = json.loads(html)
    for list in text['rows']:
        comp_id = list['id']
        gsmc = list['corpName']

    try:
        return_data = {
            'items': [
                {
                    'data': [
                        {
                            'comp_id': comp_id,
                            'gsmc': gsmc,

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

