import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
from snownlp import SnowNLP

conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='user1',
            passwd='12345678',
            db='crawl',
            charset='utf8mb4'
        )

sql  =  'SELECT *  FROM showcomment_cleandata'


df = pd.read_sql(sql,conn)




conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='user1',
            passwd='12345678',
            db='crawl',
            charset='utf8mb4'
        )

    sql  =  'SELECT *  FROM showcomment_cleandata'
    df = pd.read_sql(sql,conn)
    title_comment_dict=df.groupby('product_title').aggregate({'product_comment':'count'}).to_dict()
    title_list = []
    comment_num_list = []
    
    for key in title_comment_dict:
        title_list.append(key)
        comment_num_list.append(title_comment_dict[key])