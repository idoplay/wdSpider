# -*- coding: utf-8 -*-
import sys
import time
import re
import hashlib
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import TextResponse, Request
from scrapy.conf import settings
from wdSpider.utils.tools import sTools
from wdSpider.utils.db import sMysql
from wdSpider.items import WdspiderItem


class VisaSpider(BaseSpider):
    name = 'visa'
    allow_domains = ["visabao.com"]
    #start_urls = ["http://zhidao.baidu.com/"]
    start_urls = [
        'http://www.visabao.com/visa-AE.aspx',
        'http://www.visabao.com/visa-BD.aspx',
        'http://www.visabao.com/visa-BN.aspx',
        'http://www.visabao.com/visa-GE.aspx',
        'http://www.visabao.com/visa-IL.aspx',
        'http://www.visabao.com/visa-IN.aspx',
        'http://www.visabao.com/visa-IR.aspx',
        'http://www.visabao.com/visa-JO.aspx',
        'http://www.visabao.com/visa-JP.aspx',
        'http://www.visabao.com/visa-KH.aspx',
        'http://www.visabao.com/visa-KR.aspx',
        'http://www.visabao.com/visa-LA.aspx',
        'http://www.visabao.com/visa-LK.aspx',
        'http://www.visabao.com/visa-MM.aspx',
        'http://www.visabao.com/visa-MN.aspx',
        'http://www.visabao.com/visa-MY.aspx',
        'http://www.visabao.com/visa-NP.aspx',
        'http://www.visabao.com/visa-OM.aspx',
        'http://www.visabao.com/visa-PH.aspx',
        'http://www.visabao.com/visa-PK.aspx',
        'http://www.visabao.com/visa-SG.aspx',
        'http://www.visabao.com/visa-TH.aspx',
        'http://www.visabao.com/visa-TW.aspx',
        'http://www.visabao.com/visa-VN.aspx',
        'http://www.visabao.com/visa-AT.aspx',
        'http://www.visabao.com/visa-BE.aspx',
        'http://www.visabao.com/visa-BG.aspx',
        'http://www.visabao.com/visa-CH.aspx',
        'http://www.visabao.com/visa-CY.aspx',
        'http://www.visabao.com/visa-CZ.aspx',
        'http://www.visabao.com/visa-DE.aspx',
        'http://www.visabao.com/visa-DK.aspx',
        'http://www.visabao.com/visa-EE.aspx',
        'http://www.visabao.com/visa-ES.aspx',
        'http://www.visabao.com/visa-FI.aspx',
        'http://www.visabao.com/visa-FR.aspx',
        'http://www.visabao.com/visa-GR.aspx',
        'http://www.visabao.com/visa-HU.aspx',
        'http://www.visabao.com/visa-IE.aspx',
        'http://www.visabao.com/visa-IS.aspx',
        'http://www.visabao.com/visa-IT.aspx',
        'http://www.visabao.com/visa-LT.aspx',
        'http://www.visabao.com/visa-LU.aspx',
        'http://www.visabao.com/visa-LV.aspx',
        'http://www.visabao.com/visa-MT.aspx',
        'http://www.visabao.com/visa-NL.aspx',
        'http://www.visabao.com/visa-NO.aspx',
        'http://www.visabao.com/visa-PF.aspx',
        'http://www.visabao.com/visa-PL.aspx',
        'http://www.visabao.com/visa-PT.aspx',
        'http://www.visabao.com/visa-RU.aspx',
        'http://www.visabao.com/visa-SE.aspx',
        'http://www.visabao.com/visa-SI.aspx',
        'http://www.visabao.com/visa-TR.aspx',
        'http://www.visabao.com/visa-UK.aspx',
        'http://www.visabao.com/visa-BR.aspx',
        'http://www.visabao.com/visa-CA.aspx',
        'http://www.visabao.com/visa-CU.aspx',
        'http://www.visabao.com/visa-MX.aspx',
        'http://www.visabao.com/visa-US.aspx',
        'http://www.visabao.com/visa-DZ.aspx',
        'http://www.visabao.com/visa-ET.aspx',
        'http://www.visabao.com/visa-GH.aspx',
        'http://www.visabao.com/visa-KE.aspx',
        'http://www.visabao.com/visa-MG.aspx',
        'http://www.visabao.com/visa-TZ.aspx',
        'http://www.visabao.com/visa-ZA.aspx',
        'http://www.visabao.com/visa-AU.aspx',
        'http://www.visabao.com/visa-NZ.aspx',
    ]
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://www.visabao.com/"
    }

    def __init__(self, category=None):
        super(BaseSpider, self).__init__()

    def make_requests_from_url(self, url):
        return Request(url, callback=self.parse_list, headers=self.headers)

    def parse_list(self, response):
        hxs = HtmlXPathSelector(response)
        uk = response.url.split('/')
        uk = uk[3].replace(".aspx", "")
        #print uk
        all_links = hxs.select('//a[contains(@href, "%s")]/@href' % uk).extract()
        self.tools = sTools()
        '''
        link = 'http://www.visabao.com/visa-BR-100628.aspx'
        items = {}
        if 'items' in response.meta.keys():
            items = response.meta["items"]

        yield Request(url=link, meta={"items": items}, callback=self.get_page_parse, headers=self.headers)
        '''
        for link in all_links:
            link = 'http://www.visabao.com'+link
            #link = 'http://www.visabao.com/visa-BR-100628.aspx'
            items = {}
            if 'items' in response.meta.keys():
                items = response.meta["items"]

            yield Request(url=link, meta={"items": items}, callback=self.get_page_parse, headers=self.headers)

    def _change_type(self, sx):
        a = {
            '在职人员': 1,
            '自由职业': 2,
            '退休人员': 3,
            '已成年学生': 4,
            '未成年学生': 5,
            '学龄前儿童': 6,
            '所有人': 7
        }
        #print "============%s" % a[sx]
        return a[sx]

    def _visa_type(self, vt):
        res = 0
        if re.findall(re.compile(r'旅游'), vt):
            res = 1
        elif re.findall(re.compile(r'商务'), vt):
            res = 2
        elif re.findall(re.compile(r'探亲'), vt):
            res = 3
        elif re.findall(re.compile(r'留学'), vt):
            res = 4
        return res

    def get_page_parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = WdspiderItem()

        title = hxs.select('//h1/text()').extract()

        tags = self.tools.sMatch('<span class="tag">', '<\/span>', response.body, 0)
        handling_time = self.tools.sMatch('办理时间', '有效期', response.body, 1)
        expiration_date = self.tools.sMatch('有效期</td>', '停留期', response.body, 0)
        stay_date = self.tools.sMatch('停留期', '往返次数', response.body, 1)
        round_nums = self.tools.sMatch('往返次数', '受理范围', response.body, 1)
        msg = self.tools.sMatch('<td colspan="3">', '</td>', response.body, 0)

        service_fee = self.tools.sMatch('服务费：<i class="orange">', '元</i>', response.body, 0)
        consular_fee = self.tools.sMatch('领馆费：<i class="orange">', '元</i>', response.body, 0)
        center_fee = self.tools.sMatch('签证中心费：<i class="orange">', '元</i>', response.body, 0)

        _service_fee = 0
        if len(service_fee):
            _service_fee = service_fee[0]
        _consular_fee = 0
        if len(consular_fee):
            _consular_fee = consular_fee[0]
        _center_fee = 0
        if len(center_fee):
            _center_fee = center_fee[0]

        _exp_date = expiration_date[0].encode('utf-8')
        _exp_date = self.tools.strip_tags(_exp_date)
        _tip = ''
        if len(msg) == 3:
            _tip = msg[2].encode('utf-8')

        mysql = sMysql('127.0.0.1', 'root', '1234asdf', 'ch_trip')
        _xurl = response.url.split('-')
        _cou = mysql.getRecord("select * from  cms_area where code='%s'" % _xurl[1], 1)
        #print _cou
        #print self._visa_type(title[0].encode('utf-8'))
        #sys.exit()
        _tilte = title[0].encode('utf-8')
        item = {
            'title': _tilte,
            'area_id': _cou['continent'],
            'country_id': _cou['id'],
            'visa_type': self._visa_type(_tilte),
            'service_fee': _service_fee,
            'consular_fee': _consular_fee,
            'center_fee': _center_fee,
            'send_land': '',
            'handling_time': handling_time[0].encode('utf-8'),
            'expiration_date': _exp_date,
            'stay_date': stay_date[0].encode('utf-8'),
            'round_nums': round_nums[0].encode('utf-8'),
            'accept_range': msg[0].encode('utf-8'),
            'recent_msg': msg[1].encode('utf-8'),
            'tip_msg': _tip,
            'url': response.url,
            'dateline': time.time()
        }
        if len(tags):
            for i in range(0, len(tags)):
                if i > 3:
                    break
                _tx = self.tools.sMatch('<i>', '</i>', tags[i], 0)
                if len(_tx):
                    item['tag_%s' % i] = _tx[0].encode('utf-8')

        _hash = hashlib.md5(response.url).hexdigest()
        _has = mysql.getRecord("select * from  cms_visa where hash='%s'" % _hash, 1)

        visa_id = 0
        if _has is None:
            item['hash'] = _hash
            visa_id = mysql.dbInsert('cms_visa', item)
            visa_id = visa_id['LAST_INSERT_ID()']
        else:
            print "This Url exists....."

        print "============%s=======" % visa_id
        #sys.exit()
        #if visa_id == 0:
            #return False

        _type = self.tools.sMatch('<div class="tabMin" >', '</div>', response.body, 0)
        _type_span = self.tools.sMatch('<span(.*?)>', '</span>', _type[0], 0)
        #_type_content = self.tools.sMatch('<div class="tabMinBox" >', '</div>', response.body, 0)
        _type_table = self.tools.sMatch('<table class="tbF">', '</table>', response.body, 0)
        #print _type_table
        #print len(_type_table)
        #sys.exit()
        if len(_type_span):
            for k in range(0, len(_type_span)):
                _tdr_ti = self.tools.sMatch('<td class="bold" style="width:150px;">', '</td>', _type_table[k], 0)
                _tdr = self.tools.sMatch('<td>', '</td>', _type_table[k], 0)
                data_type = self._change_type(_type_span[k][1])
                if len(_tdr):
                    for j in range(0, len(_tdr)):
                        _key = _tdr_ti[j].find('<span class="orange">*</span>')
                        _xs = {
                            'visa_item_id': visa_id,
                            'data_type': data_type,
                            'data_key': _tdr_ti[j].replace('<span class="orange">*</span>', ''),
                            'data_value': _tdr[j],
                        }
                        _xs['is_require'] = 1
                        if _key == -1:
                            _xs['is_require'] = 0
                        mysql.dbInsert('cms_visa_data', _xs)

        '''
        _type_span = self.tools.sMatch('<span(.*?)>', '</span>', _type[0], 0)
        #print _type
        print _type_span
        sys.exit()


        _type_table = self.tools.sMatch('<table class="tbF">', '</table>', _type_content[0], 0)
        #ac = []
        if len(_type_table):
            for i in range(0, len(_type_table)):
                _tdr_ti = self.tools.sMatch('<td class="bold" style="width:150px;">', '</td>', _type_table[i], 0)
                _tdr = self.tools.sMatch('<td>', '</td>', _type_table[i], 0)
                data_type = self._change_type(_type_span[i][1])

                for j in range(0, len(_tdr)):
                    _key = _tdr_ti[j].find('<span class="orange">*</span>')
                    _xs = {
                        'visa_item_id': visa_id,
                        'data_type': data_type,
                        'data_key': _tdr_ti[j].replace('<span class="orange">*</span>', ''),
                        'data_value': _tdr[j],
                    }
                    _xs['is_require'] = 1
                    if _key == -1:
                        _xs['is_require'] = 0
                    mysql.dbInsert('cms_visa_data', _xs)
        #sys.exit()
        '''
