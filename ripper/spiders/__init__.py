# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapy.loader import ItemLoader
import ripper.items


class imgSpider(scrapy.Spider):
    name = "imgRip"
    start_urls = [
        'https://mangakakalot.com/chapter/tomochan_wa_onnanoko/chapter_1'
    ]

    def parse(self, response):
        for img in response.css('div.vung-doc'):
            imgUrls = response.css('img').xpath('@src').getall()
            loader = ItemLoader(item=ripper.items.image, selector=img)
            loader.add_value('file_urls', imgUrls)
            yield loader.load_item()
