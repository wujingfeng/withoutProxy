#!/bin/sh
echo "begin start scrapy projects......."
#nohup scrapy crawl master > /dev/null 2>&1 &
# 循环启动 scrapy project name 进程，后台运行.
for((i=0;i<2;i++))
do
        for((j=0;j<20;j++))
        do
                nohup scrapy crawl noproxy > /dev/null 2>&1 &
        done
        echo "sleep 60 second"
        sleep 60
done
echo "----------start scrapy end----------"