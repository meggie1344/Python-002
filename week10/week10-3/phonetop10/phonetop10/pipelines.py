# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Phonetop10Pipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='user1',
            passwd='12345678',
            db='crawl',
            charset='utf8mb4'
        )
        cursor = conn.cursor() 
        
        product_title = item['product_title']   
        product_comment = item['product_comment']
        
        raw_data_insert = '''INSERT INTO showcomment_rawdata (product_title, product_comment) 
        SELECT %s, %s FROM DUAL 
        WHERE NOT EXISTS(SELECT product_title, product_comment FROM showcomment_rawdata 
        WHERE product_title = %s  AND product_comment = %s)'''

        cursor.execute(raw_data_insert, [str(product_title),str(product_comment),str(product_title),str(product_comment)])
        conn.commit()
        cursor.close()
        conn.close()
        return item

