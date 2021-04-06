# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WallhavencrawlerPipeline:


    def __init__(self) -> None:
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='wallhaven', charset='utf8'
                                  ,port=3306)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = "select * from sz_wallhaven where wid = %s "
        self.cursor.execute(sql,item['wid'])
        result = self.cursor.fetchone()
        if result is None:
            sqlInsert = " insert into sz_wallhaven(wid,src,width,height,tags) VALUES(%s,%s,%s,%s,%s)"
            self.cursor.execute(sqlInsert,(item["wid"],item["src"],item["width"],item["height"],"$$$".join(item['tags'])))
            self.db.commit()
            return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
