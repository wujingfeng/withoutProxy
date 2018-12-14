import datetime

import re

from scrapy import Request, FormRequest
from scrapy_redis.spiders import RedisSpider

from withoutProxy import test_settings
from withoutProxy.myhandlers import *
from withoutProxy.myitems import *

class NoproxySpider(RedisSpider):
    """Spider that reads urls from redis queue (noproxy:start_urls)."""
    name = 'test_noproxy'
    redis_key = 'noproxy:start_urls'
    # allowed_domains = ['cnblogs.com']

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(NoproxySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        self.logger.info('parse start with url: '+response.url)
        start = datetime.datetime.now()

        found_rule = False
        for rule in test_settings.rules:
            pattern = re.compile(rule['re'])
            ret = re.search(pattern, response.url)
            # print(rule['re'], response.url, ret)
            if (ret):
                found_rule = True
                # print(rule['func'])
                break
        if found_rule:
            #按配置做解析动作
            self.logger.info("start handle data for url: " + response.url)
            data = eval(rule['func'] + '.' + rule['func'] + '(response)')
            # print(data)
            self.logger.info("handled data for url: " + response.url)
            self.logger.info("return data: " + str(data))
            print(str(data))
            self.logger.info("start yield requests: " + response.url)
            if ('requests' in data):
                for url in data['requests']:
                    yield Request(
                        url = url,
                        dont_filter = True
                    )
            # print('meta = ', response.meta)
            self.logger.info("end yield requests: " + response.url)
            self.logger.info("start yield form requests: " + response.url)
            if ('form_requests' in data):
                for post in data['form_requests']:
                    yield FormRequest(
                        url = post['url'],
                        formdata = post['post_params'],
                        meta = {'post_params' : post['post_params']},
                        dont_filter = True
                    )
            self.logger.info("end yield form requests: " + response.url)
            self.logger.info("start yield items: " + response.url)
            if ('items' in data):
                for tmp_items in data['items']:
                    # print(tmp_items)
                    if ('item_cfg' in tmp_items):
                        item = eval(tmp_items['item_cfg'] + '_item.' + tmp_items['item_cfg'] + '_item()')
                    else:
                        item = eval(rule['func'] + '_item.' + rule['func'] + '_item()')
                    for tmp_item in tmp_items['data']:
                        for item_key in tmp_item:
                            item[item_key] = tmp_item[item_key]
                            if ('item_cfg' in tmp_items):
                                item['pipline_func'] = tmp_items['item_cfg'] + '_pipline.' + tmp_items['item_cfg'] + '_pipline'
                            else:
                                item['pipline_func'] = rule['func'] + '_pipline.' + rule['func'] + '_pipline'
                        # print(item)
                        yield item
            self.logger.info("end yield items for url: " + response.url)

        else:
            self.logger.warning('no rule matched for url: ' + response.url)

        end = datetime.datetime.now()
        self.logger.info("parse end for url: " + response.url + ', cost ' + str((end - start).seconds) + ' seconds')

