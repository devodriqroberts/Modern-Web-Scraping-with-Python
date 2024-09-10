# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import sqlite3


class MongodbPipeline:
    collection_name = "best_movies"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://imdb_crawler:testpassword@imdbcluster.jodoy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item

class SqlitePipeline:

    def open_spider(self, spider):
        self.connection = sqlite3.connect("imdb.db")
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("""
                DROP TABLE IF EXIST best_movies
            """)
            self.cursor.execute("""
                CREATE TABLE best_movies(
                    title TEXT,
                    year TEXT,
                    film_rating TEXT,
                    duration TEXT,
                    genre TEXT,
                    rating TEXT,
                    movie_url TEXT
                )
            """)
            self.connection.commit()
        except:
            pass


    def close_spider(self, spider):
        self.connection.close()


    def process_item(self, item, spider):
        self.cursor.execute("""
        INSERT INTO best_movies (title,year,film_rating,duration,genre,rating,movie_url) VALUES(?,?,?,?,?,?,?)
        """, (
            item.get('title'),
            item.get('year'),
            item.get('film_rating'),
            item.get('duration'),
            item.get('genre'),
            item.get('rating'),
            item.get('movie_url')
        ))
        self.connection.commit()
        return item
