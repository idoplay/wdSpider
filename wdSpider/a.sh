#! /bin/sh
export PATH=$PATH:/usr/local/bin
cd /htdocs/wdSpider/wdSpider
scrapy crawl zhihu --set LOG_FILE=/tmp/zhihu.log
TODAY=`date +%Y%m%d%H%i`
echo $TODAY
