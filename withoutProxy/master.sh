#!/bin/sh
#cd /usr/local/service/withoutProxy/withoutProxy
nohup scrapy crawl master > /dev/null 2>&1 &
