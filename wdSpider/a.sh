#! /bin/sh
export PATH=$PATH:/usr/local/bin
cd /home/wwwroot/wdSpider/
/root/anaconda2/bin/scrapy runspider  /home/wwwroot/wdSpider/wdSpider/spiders/ZhihuSpider.py --set LOG_FILE=/tmp/zhihu.log
TODAY=`date +%Y%m%d%H%i`
echo $TODAY
