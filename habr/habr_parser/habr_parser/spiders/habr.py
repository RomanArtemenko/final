import scrapy
from habr_parser.items import HabrItem
from scrapy_redis.spiders import RedisSpider
import json

class HabrScrapy(RedisSpider):
    name = 'habr'
    root = 'https://habr.com/'
    start_urls = ['https://habr.com/']
    headers = {'Connection':'keep-alive', 'User-Agent:':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    def parse(self, response):
        articles_url = response.xpath('//h2[@class="post__title"]/a/@href').extract()

        for url in articles_url:
            yield scrapy.Request(url=url, callback=self.item_parse, headers=self.headers )

        next_page = response.xpath('//a[@id="next_page"]/@href').extract_first()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def item_parse(self, response):
        item = HabrItem()

        json_data = self.get_json(response)

        item['avatar'] = self.get_avatar(json_data)
        item['name'] = self.get_name(json_data)
        item['description'] = self.get_descriprion(json_data)
        item['keywords'] = self.get_keywords(response)
        item['url'] = self.get_url(response)
        item['date'] = self.get_date(json_data)

        yield item

    def get_avatar(self, jd):
        try:
            ava = jd['image'][0]
        except:
            ava = None

        return ava
     
    def get_name(self, jd):
        return jd['headline']
    
    def get_descriprion(self, jd):
        return jd['description']

    def get_keywords(self, response):
        return response.xpath('//meta[@name="keywords"]/@content').extract()

    def get_url(self, response):
        return response.xpath('//meta[@property="og:url"]/@content').extract_first()

    def get_date(self, jd):
        return jd['datePublished']

    def get_json(self, response):
        return json.loads(''.join(response.xpath('//script[@type="application/ld+json"]/text()').extract()))