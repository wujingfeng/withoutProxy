#!/bin/sh
echo "begin stop scrapy projects......."
ps aux | grep noproxy | grep -v grep | cut -c 9-15 | xargs kill
echo "----------stop scrapy end----------"
