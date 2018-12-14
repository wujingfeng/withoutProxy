from withoutProxy.piplines import *


class CommPipeline(object):
    def process_item(self, item, spider):
        if ('pipline_func' in item):
            spider.logger.info("commpipline start, item type is: " + item['pipline_func'])
            eval(item['pipline_func'] + '(item)')
        else:
            spider.logger.warning("commpipline start, but no item cfg")
        spider.logger.info("commpipline end, item type is: " + item['pipline_func'])
        return item