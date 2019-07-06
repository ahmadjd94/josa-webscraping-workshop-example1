# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class JosaPipeline(object):
    conn = sqlite3.connect('example.db')
    try:
        conn.execute("create table items (img_url Text)")
    except:
        pass
    def process_item(self, item, spider):
        print ("We are within the pipeline stage")
        print(item)
        sql_statement = "insert into items values (\"%s\")" % item["image_url"][0]
        self.conn.execute(sql_statement)
        self.conn.commit()
        return item
