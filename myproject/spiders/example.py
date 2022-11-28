import asyncio

import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['habr.com']
    start_urls = [
        'https://habr.com/ru/post/308660/',
        'https://habr.com/ru/post/308661/',
        'https://habr.com/ru/post/701284/',
        'https://habr.com/ru/post/308662/',
        'https://habr.com/ru/post/308663/',
        'https://habr.com/ru/post/308664/',
        'https://habr.com/ru/post/701282/'
    ]

    async def parse(self, response, **kwargs):
        await asyncio.sleep(float('inf'))
        pass
