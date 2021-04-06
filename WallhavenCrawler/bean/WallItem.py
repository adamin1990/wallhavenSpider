import  scrapy

class WallItem(scrapy.Item):
    wid = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    tags = scrapy.Field()
    src = scrapy.Field()