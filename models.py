import settings
import sqlite3
import datetime
import re
conn=sqlite3.connect(settings.database)
cur = conn.cursor()


class ProductRecord(object):
    """docstring for ProductRecord"""
    def __init__(self, title, product_url, price, crawl_time):
        super(ProductRecord, self).__init__()
        self.title = re.sub('\W+','', title.text)
        self.product_url = ''.join(product_url['href']),
        self.price = price.text
        self.crawl_time = crawl_time

    def save(self):
        
        cur.execute("""INSERT INTO products (title, product_url, price, crawl_time) VALUES (?,?,?,?)""" , (
            self.title,
            """https://flipkart.com"""+''.join(self.product_url),
            self.price,
            self.crawl_time,
        ))
        conn.commit()
        



if __name__ == '__main__':

    # setup tables
    cur.execute("DROP TABLE IF EXISTS products")
    cur.execute("""CREATE TABLE products (
        id          serial PRIMARY KEY ,
        title       TEXT,
        product_url  TEXT,
        price       TEXT,
        crawl_time varchar(2056)
    );""")
    conn.commit()
