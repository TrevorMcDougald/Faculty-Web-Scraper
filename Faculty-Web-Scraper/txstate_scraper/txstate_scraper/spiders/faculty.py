# -*- coding: utf-8 -*-
import scrapy
import os.path


class FacultySpider(scrapy.Spider):
    # identifies the spider (unique within project)
    name = 'faculty'
    # if the domain URL is not in this setting, the URL will be ignored.
    allowed_domains = ['cs.txstate.edu/accounts/profiles/']
    # Spider starts by crawling the feed URLs
    start_urls = ['http://www.cs.txstate.edu/Personnel/Faculty/']

    def parse(self, response):

        save_path = "Faculty-Web-Scraper/Faculty-Pages/"
        file_name = response.url.split("/")[-2] + '.html'
        complete_name = os.path.join(save_path, file_name)
        with open(complete_name, 'wbx') as file:
            file.write(response.body)

