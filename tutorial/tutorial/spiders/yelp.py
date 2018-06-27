import scrapy
#import re
from scrapy.spider import BaseSpider
#from scrapy.selector import HtmlXPathSelector
from scrapy.loader import ItemLoader
from tutorial.items import Yelp


class YelpSpider(BaseSpider):
    name = "yelp"
    start_urls = ['https://www.yelp.com/search?find_desc=carpenter+handyman&find_loc=San+Francisco%2C+CA&ns=0',
              'https://www.yelp.com/search?find_desc=carpenter+handyman&find_loc=San+Francisco%2C+CA&ns=1',
              'https://www.yelp.com/search?find_desc=Carpenter+Handyman&find_loc=San+Francisco,+CA&start=10',
              'https://www.yelp.com/search?find_desc=Carpenter+Handyman&find_loc=San+Francisco,+CA&start=20']

    def parse(self, response):
        yelpitems = response.css('li.regular-search-result')
        for each_item in yelpitems:
            handyman = ItemLoader(item=Yelp(), selector=each_item)
            handyman.add_css('handyman_name', 'span.indexed-biz-name >a> span::text')
            handyman.add_css('handyman_address', 'span.indexed-biz-name >a> span::text')
            handyman.add_css('handyman_contact', 'span.biz-phone::text')
            yield handyman.load_item()


        '''
        next_page_url = response.xpath("//div[@class='arrange_unit page-option current']/following-sibling::div/a/@href").extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        '''