# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#À ajouter au fichier items.py
class ReviewsAllocineItem(scrapy.Item):
    title= scrapy.Field()
    img= scrapy.Field()
    author= scrapy.Field()
    time= scrapy.Field()
    genre= scrapy.Field()
    score= scrapy.Field()
    desc= scrapy.Field()
    release= scrapy.Field()
    page=scrapy.Field()
    pass