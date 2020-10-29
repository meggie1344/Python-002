# -*- coding: utf-8 -*-
import scrapy
from week10.lastproject.phonetop10.phonetop10.items import Phonetop10Item
from scrapy.selector import Selector

class Getphonetop10Spider(scrapy.Spider):
    name = 'getphonetop10'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/']

    def start_requests(self):       
        url = 'https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        all_product_title = Selector(response=response).xpath('//h5[@class="feed-block-title"]')
        #取前10的商品
        for i in range(10):
            item = Phonetop10Item()
            product_title = all_product_title[i].xpath('./a/text()').extract_first()
            product_comment_url = all_product_title[i].xpath('./a/@href').extract_first()
            #获取到商品名字
            item['product_title'] = product_title
            #这个商品的评论页面，二次请求分析
            
            yield scrapy.Request(url=product_comment_url, meta={'item': item}, callback=self.parse2)
            #调试打印
            #print(product_comment_url)
    

    def parse2(self, response):
        current_page_comment_list = Selector(response=response).xpath('//div[@id="commentTabBlockNew"]/ul/li/div[@class="comment_conBox"]/div[@class="comment_conWrap"]/div[@class="comment_con"]')
        item = response.meta['item']
       
        for i in range(len(current_page_comment_list)):
            single_comment = current_page_comment_list[i].xpath('./p/span/text()').extract_first()
            
            item['product_comment'] = single_comment
            yield item
            #print(single_comment)
        
        #是否存在多页评论，自动翻页，再次请求
        more_page_label = Selector(response=response).xpath('//div[@id="commentTabBlockNew"]/ul[@class="pagination"]')
        
        if more_page_label:
            page_num_list = more_page_label.xpath('./li')
            page_num = page_num_list[-4].xpath('./a/text()').extract_first()
            #print(page_num)

            for i in range(2,int(page_num)+1):
                next_comment_page_url = ("https://www.smzdm.com/p/25708400/p%d/#comments" %i)
                yield scrapy.Request(url=next_comment_page_url, meta={'item': item}, callback=self.parse3)

    def parse3(self, response):
        current_page_comment_list = Selector(response=response).xpath('//div[@id="commentTabBlockNew"]/ul/li/div[@class="comment_conBox"]/div[@class="comment_conWrap"]/div[@class="comment_con"]')
        item = response.meta['item']

        for i in range(len(current_page_comment_list)):
            single_comment = current_page_comment_list[i].xpath('./p/span/text()').extract_first()
            item['product_comment'] = single_comment
            #print(single_comment)
            yield item




