# -*- coding: utf-8 -*-
import scrapy

from ..items import JosaItem


class ExampleSiteSpider(scrapy.Spider):
    name = 'example_site'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']
    BASE_URL = "http://example.webscraping.com"

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse_index)

    def parse_index(self, response):
        urls = response.xpath("//div[@id=\"results\"]//tr//a/@href").extract()
        for url in urls:
            yield scrapy.Request(self.BASE_URL + url)
            break

    def parse(self, response):
        item = JosaItem()
        item["image_url"] = response.xpath("//tr[@id=\"places_national_flag__row\"]//img/@src").extract()

        yield item


