#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 22:05
# @Author  : 至尊宝
# @Site    : 
# @File    : baidu_yq.py

import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from yqsj.items import YqsjChinaItem, YqsjProvinceItem


class YqsjSpider(scrapy.Spider):
    name = 'yqsj'
    # allowed_domains = ['blog.csdn.net']
    start_urls = ['https://voice.baidu.com/act/newpneumonia/newpneumonia#tab0']
    china_xpath = "//div[contains(@class, 'VirusSummarySix_1-1-317_2ZJJBJ')]/text()"
    province_xpath = "//*[@id='nationTable']/table/tbody/tr[{}]/td/text()"
    province_xpath_1 = "//*[@id='nationTable']/table/tbody/tr[{}]/td/div/span/text()"

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=chrome_options,
                                        executable_path="E:\\chromedriver_win32\\chromedriver.exe")
        self.browser.set_page_load_timeout(30)

    def parse(self, response, **kwargs):
        country_info = response.xpath(self.china_xpath)
        yq_china = YqsjChinaItem()
        yq_china['exist_diagnosis'] = country_info[0].get()
        yq_china['asymptomatic'] = country_info[1].get()
        yq_china['exist_suspecte'] = country_info[2].get()
        yq_china['exist_severe'] = country_info[3].get()
        yq_china['cumulative_diagnosis'] = country_info[4].get()
        yq_china['overseas_input'] = country_info[5].get()
        yq_china['cumulative_cure'] = country_info[6].get()
        yq_china['cumulative_dead'] = country_info[7].get()
        yield yq_china

        for x in range(1, 35):
            path = self.province_xpath.format(x)
            path1 = self.province_xpath_1.format(x)
            province_info = response.xpath(path)
            province_name = response.xpath(path1)
            yq_province = YqsjProvinceItem()
            yq_province['location'] = province_name.get()
            yq_province['new'] = province_info[0].get()
            yq_province['exist'] = province_info[1].get()
            yq_province['total'] = province_info[2].get()
            yq_province['cure'] = province_info[3].get()
            yq_province['dead'] = province_info[4].get()
            yield yq_province
