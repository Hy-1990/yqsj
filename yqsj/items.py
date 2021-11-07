# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YqsjProvinceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location = scrapy.Field()
    new = scrapy.Field()
    exist = scrapy.Field()
    total = scrapy.Field()
    cure = scrapy.Field()
    dead = scrapy.Field()


class YqsjChinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 现有确诊
    exist_diagnosis = scrapy.Field()
    # 无症状
    asymptomatic = scrapy.Field()
    # 现有疑似
    exist_suspecte = scrapy.Field()
    # 现有重症
    exist_severe = scrapy.Field()
    # 累计确诊
    cumulative_diagnosis = scrapy.Field()
    # 境外输入
    overseas_input = scrapy.Field()
    # 累计治愈
    cumulative_cure = scrapy.Field()
    # 累计死亡
    cumulative_dead = scrapy.Field()
