import scrapy

from WallhavenCrawler.bean.WallItem import WallItem


class WallhavenSpider(scrapy.Spider):
    name = 'wallhaven'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['https://wallhaven.cc/hot?page=1']
    url = "https://wallhaven.cc/hot?page={}"
    page = 1

    def parse(self, response):
        res = response.xpath("//section[@class='thumb-listing-page']")[0].xpath("./ul/li")
        for item in res:
            wid = item.xpath("./figure/@data-wallpaper-id").get()
            yield scrapy.Request(url="https://wallhaven.cc/w/" + wid, callback=self.parseItem, meta={"wid": wid})

        if self.page < 10:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)

    def parseItem(self, response):
        # https://wallhaven.cc/w/rdrm7m
        swid = response.meta.get('wid')
        # print("wid======"+response.meta.get('wid'))
        item = WallItem()
        item['wid'] = swid
        dd = swid[0:2]
        item['width'] = response.xpath("//img[@id='wallpaper']/@data-wallpaper-width").get()
        item['height'] = response.xpath("//img[@id='wallpaper']/@data-wallpaper-height").get()
        item['src'] = response.xpath("//img[@id='wallpaper']/@src").get()
        item['tags'] = response.xpath("//ul[@id='tags']/li/a/text()").getall()
        yield item
