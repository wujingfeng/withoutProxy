import pymysql
from redis import Redis
from scrapy.exceptions import DontCloseSpider
from scrapy_redis.spiders import RedisSpider

from withoutProxy import settings
from withoutProxy.config.cj_database import *


class MasterSpider(RedisSpider):
    name = 'master'
    redis_key = 'master:start_urls'

    def spider_idle(self):
        print('add')
        self.add_urls()

        raise DontCloseSpider

    def add_urls(self):
        print('in add')

        r = Redis(
            host = settings.REDIS_HOST,
            port = settings.REDIS_PORT,
            password = settings.REDIS_PASSWORD,
            db = settings.DB,
        )

        try:
            my_len = r.llen('noproxy:start_urls')
        except Exception as e:
            print(e)
        # print(my_len)
        my_len1 = r.zcard('noproxy:requests')
        # print(my_len1)
        total = my_len + my_len1
        print(total)
        if (total < 1024):#64进程*每次获取16个
            conn = pymysql.connect(
                host = MYSQL_HOST,
                user =  MYSQL_USER,
                password =  MYSQL_PASSWORD,
                db =  MYSQL_DB,
                charset =  MYSQL_CHATSET,
                port =  MYSQL_PORT
            )
            cursor = conn.cursor()

            sql = 'select site from bad_site'
            print(sql)
            cursor.execute(sql)    #执行sql语句
            results = cursor.fetchall()
            if (len(results) > 0):
                sql = 'select id, url from task where status = 1 or status = 2'
                for row in results:
                    sql += ' and url not like "' + row[0] + '%"'
                sql += ' order by pri_level desc, created limit 1024'
                print(sql)
                cursor.execute(sql)    #执行sql语句
                results = cursor.fetchall()
                print(len(results))
            if (len(results) == 0):
                sql = 'select id, url from task where status = 1 or status = 2 order by pri_level desc, created limit 1024'
                print(sql)
                cursor.execute(sql)    #执行sql语句
                results = cursor.fetchall()
            print(len(results))
            ids = []
            if results:
                for row in results:
                    url = row[1]
                    ids.append(row[0])
                    r.lpush('noproxy:start_urls', url)
                # sql = 'update task set status = 3 where id in %s and status != 2'
                sql = 'delete from  task  where id in %s and status != 2'
                cursor.execute(sql, [ids])
                conn.commit()

            cursor.close()
            conn.close()
