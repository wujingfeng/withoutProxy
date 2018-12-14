from redis import Redis
import pymysql

from withoutProxy import test_settings
from scrapy.exceptions import DontCloseSpider
from scrapy_redis.spiders import RedisSpider

class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'test_master'
    redis_key = 'master:start_urls'

    def spider_idle(self):
        """Schedules a request if available, otherwise waits."""
        # XXX: Handle a sentinel to close the spider.
        print('add')

        self.add_url()
        # self.schedule_next_requests()
        raise DontCloseSpider

    def add_url(self):
        print('in add')
        r = Redis(
            host = test_settings.REDIS_HOST,
            port = test_settings.REDIS_PORT,
            password = test_settings.REDIS_PASSWORD,
            db = test_settings.DB
        )
        url = 'http://glxy.mot.gov.cn/awards/getAwardsList.do?comId=357fb052cae44e45984ed1e77775a643'

        r.lpush('noproxy:start_urls', url)