import scrapy
from scrapy.crawler import CrawlerProcess
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker

from models import Author, Tag, Quote, Link, db_connect, create_table


class QuoteItem(scrapy.Item):
    author = scrapy.Field()
    quote = scrapy.Field()
    about = scrapy.Field()
    tags = scrapy.Field()


class AuthorItem(scrapy.Item):
    fullname = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
    bio = scrapy.Field()


class SpiderPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        adapter = ItemAdapter(item)
        if 'author' in adapter.keys():
            session = self.Session()
            author = Author()
            author.name = item["author"]
            author.ref = item["about"]
            quote = Quote()
            quote.quote_content = item["quote"].strip().replace('“','').replace('”','')

            # check whether the author exists
            exist_author = session.query(Author).filter_by(name=author.name).first()
            try:
                if exist_author is None:  # the current author exists

                    session.add(author)

                # print(f"--------->  {session.query(Author).filter_by(name=author.name).first().id}")
                quote.author_id = session.query(Author).filter_by(name=author.name).first().id
                session.add(quote)
                session.commit()

                for tag_item in item["tags"]:
                    exist_tag = session.query(Tag).filter_by(name=tag_item).first()
                    if exist_tag is None:
                        tag = Tag()
                        tag.name = tag_item
                        tag.quote_id = session.query(Quote).filter_by(quote_content=quote.quote_content).first().id
                        session.add(tag)
                        session.commit()


            except:
                session.rollback()
                raise

            finally:
                session.close()

        if 'fullname' in adapter.keys():
            session = self.Session()
            new_author = Author()
            new_author.name = item["fullname"]
            new_author.id = session.query(Author).filter_by(name=new_author.name).first().id
            new_author.ref = session.query(Author).filter_by(name=new_author.name).first().ref
            new_author.birthday = item["born_date"]
            new_author.bornlocation = item["born_location"]

            # check whether the author exists
            exist_author = session.query(Author).filter_by(name=new_author.name).first()
            try:
                if exist_author is not None:  # the current author exists
                    session.delete(exist_author)
                    session.commit()
                    session.add(new_author)
                    session.commit()
            except:
                session.rollback()
                raise

            finally:
                session.close()

        return item
    def close_spider(self, spider):
        pass


class Spider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {
        'ITEM_PIPELINES': {
            SpiderPipeline: 300,

        }

    }

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            tags = quote.xpath("div[@class='tags']/a/text()").extract()
            author, = quote.xpath("span/small/text()").get(),
            about = self.start_urls[0] + quote.xpath('span/a/@href').get()
            quote = quote.xpath("span[@class='text']/text()").get()
            yield QuoteItem(author=author, quote=quote, tags=tags, about=about)

        for quote in response.xpath("/html//div[@class='quote']"):
            yield response.follow(url=self.start_urls[0] + quote.xpath('span/a/@href').get(),
                                  callback=self.parse_author)

        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse_author(self, response):
        content = response.xpath("/html//div[@class='author-details']")
        fullname = content.xpath("h3/text()").get().strip()
        born_date = content.xpath("p/span[@class='author-born-date']/text()").get().strip()
        born_location = content.xpath("p/span[@class='author-born-location']/text()").get().strip()
        bio = content.xpath("div[@class='author-description']/text()").get().strip()
        yield AuthorItem(fullname=fullname, born_date=born_date, bio=bio, born_location=born_location)


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(Spider)
    process.start()