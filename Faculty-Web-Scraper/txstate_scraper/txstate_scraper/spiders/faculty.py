# -*- coding: utf-8 -*-
import scrapy
import os.path


class FacultySpider(scrapy.Spider):
    # identifies the spider (unique within project)
    name = 'faculty'
    # if the domain URL is not in this setting, the URL will be ignored.
    allowed_domains = ['cs.txstate']
    # Spider starts by crawling the feed URLs
    start_urls = ['https://cs.txstate.edu/accounts/profiles/hs15/',
                  'https://cs.txstate.edu/accounts/profiles/ma04/',
                  'https://cs.txstate.edu/accounts/profiles/vla37/',
                  'https://cs.txstate.edu/accounts/profiles/mb92/',
                  'https://cs.txstate.edu/accounts/profiles/xc10/',
                  'https://cs.txstate.edu/accounts/profiles/d_c426/',
                  'https://cs.txstate.edu/accounts/profiles/hd01/',
                  'https://cs.txstate.edu/accounts/profiles/jg66/',
                  'https://cs.txstate.edu/accounts/profiles/hag10/',
                  'https://cs.txstate.edu/accounts/profiles/qg11/',
                  'https://cs.txstate.edu/accounts/profiles/mg65/',
                  'https://cs.txstate.edu/accounts/profiles/lbh31/',
                  'https://cs.txstate.edu/accounts/profiles/ch01/',
                  'https://cs.txstate.edu/accounts/profiles/ck1224/',
                  'https://cs.txstate.edu/accounts/profiles/lk04/',
                  'https://cs.txstate.edu/accounts/profiles/ok11/',
                  'https://cs.txstate.edu/accounts/profiles/gl1082/']

    def parse(self, response):

        save_path = "Faculty-Web-Scraper/Faculty-Pages/"
        file_name = response.url.split("/")[-1] + '.html'
        complete_name = os.path.join(save_path, file_name)
        with open(complete_name, 'wb') as file:
            file.write(response.body)

