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

sql  =  'SELECT *  FROM showcomment_rawdata'
#测试，sql  = 'SELECT *  FROM showcomment_rawdata  LIMIT 80,4'

df = pd.read_sql(sql,conn)
#判断若为空格，则处理为NaN, 并填充替换空值
df['product_comment'] = df['product_comment'].apply(lambda x: np.NaN if str(x).isspace() else x)
df['product_comment'] = df['product_comment'].fillna('该用户暂无评论')

comment_list = df['product_comment'].values.tolist()

#分析得出情感分数，pandas的dataframe追加一列
sentiment_score_list = []
for i in comment_list:
    s = SnowNLP(i)
    score = s.sentiments
    sentiment_score_list.append(score)

df['sentiment'] = sentiment_score_list

conn.close()


#清洗后数据重新入库到mysql
engine = create_engine("mysql+pymysql://user1:12345678@localhost:3306/crawl?charset=utf8mb4")

df.to_sql("showcomment_cleandata", engine, schema="crawl", if_exists='append', index=False,
            chunksize=None, dtype=None)