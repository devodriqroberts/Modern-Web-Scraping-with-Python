# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class CandlesScraperPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("candles.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS candles """)
        self.curr.execute(""" CREATE TABLE IF NOT EXISTS candles(
                            product_brand text,
                            product_link text,
                            product_heading text,
                            product_description text,
                            product_id text,
                            product_price text
                        )  """)

    def store_db(self, item):
        self.curr.execute("""  INSERT INTO candles VALUES (?, ?, ?, ?, ?, ?) """, (
            item["product_brand"],
            item["product_link"],
            item["product_heading"],
            item["product_description"],
            item["product_id"],
            item["product_price"],
        ))

        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
