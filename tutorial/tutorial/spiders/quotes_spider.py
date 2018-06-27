import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "yelp"
    start_urls = ['https://www.yelp.com/search?find_desc=carpenter+handyman&find_loc=San+Francisco%2C+CA&ns=0',
              'https://www.yelp.com/search?find_desc=carpenter+handyman&find_loc=San+Francisco%2C+CA&ns=1'
              'https://www.yelp.com/search?find_desc=Carpenter+Handyman&find_loc=San+Francisco,+CA&start=10',
              'https://www.yelp.com/search?find_desc=Carpenter+Handyman&find_loc=San+Francisco,+CA&start=20']

    def parse(self, response):
        for each_item in response.css('li.regular-search-result'):

            item = {
                'handyman_name': each_item.css('span.indexed-biz-name >a> span::text').extract_first(),
                'Address': re.sub(" +\n+", " +", each_item.css('div.service-area::text').extract_first()).strip(),
                'Phone number': re.sub("\n", " ", each_item.css('span.biz-phone::text').extract_first()).strip()
            }
            yield item

        next_page_url = response.xpath("//div[@class='arrange_unit page-option current']/following-sibling::div/a/@href").extract_first()

        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
