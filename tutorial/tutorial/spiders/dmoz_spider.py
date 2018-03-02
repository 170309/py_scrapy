import scrapy
from tutorial.items import DmozItem
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["www.circ.gov.cn"]
    start_urls = [
        "http://www.circ.gov.cn/web/site0/tab5202/info4095324.htm"
        ]

    def parse(self, response): 
    	node = response.xpath('//table[@class="MsoNormalTable"]/tbody/tr[3]').extract_first()
    	for sel in node
        	item = DmozItem()
     #    	# cid = 
     #    	# company = 
     #    	# income = 
     		catogery = sel.xpath('td[1]/p/text()').extract()
     		if catogery != "" :
				item['catogery'] = catogery
        	item['cid'] = sel.xpath('td[2]/p/text()').extract()
        	item['company'] = sel.xpath('td[3]/p/text()').extract()
        	item['income'] = sel.xpath('td[4]/p/text()').extract()
        	# item['cid'] = [i.encode('utf-8') for i in cid]
        	# item['company'] = [c.encode('utf-8') for c in company]
        	# item['income'] = [In.encode('utf-8') for In in income]
        	# yield item
		# for item in response.xpath('//table[@class="MsoNormalTable"]'):
		# 	print item.xpath('tbody/tr/td/p[@class="MsoNormal"]/text()').extract()
