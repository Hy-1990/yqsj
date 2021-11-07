# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from yqsj.items import YqsjChinaItem, YqsjProvinceItem


class YqsjPipeline:
    def __init__(self):
        self.file = open('result.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item, YqsjChinaItem):
            self.file.write(
                "国内疫情\n现有确诊\t{}\n无症状\t{}\n现有疑似\t{}\n现有重症\t{}\n累计确诊\t{}\n境外输入\t{}\n累计治愈\t{}\n累计死亡\t{}\n".format(
                    item['exist_diagnosis'],
                    item['asymptomatic'],
                    item['exist_suspecte'],
                    item['exist_severe'],
                    item['cumulative_diagnosis'],
                    item['overseas_input'],
                    item['cumulative_cure'],
                    item['cumulative_dead']))
        if isinstance(item, YqsjProvinceItem):
            self.file.write(
                "省份:{}\t新增:{}\t现有:{}\t累计:{}\t治愈:{}\t死亡:{}\n".format(
                    item['location'],
                    item['new'],
                    item['exist'],
                    item['total'],
                    item['cure'],
                    item['dead']))
        return item

    def close_spider(self, spider):
        self.file.close()
