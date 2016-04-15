# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy import Selector
from bs4 import BeautifulSoup
from scrapy.utils.response import open_in_browser

from .. import items


class DirectorySpider(Spider):
    name = "directory"
    allowed_domains = ["americanforkchamber.org"]
    start_urls = (
        # 'http://americanforkchamber.org/directory.htm',
        'http://americanfork.chamberofcommerce.me/members/directory/search_1_column.php?org_id=AFCC&view_all_flag=X',
    )

    # def create_ajax_request(self):
    #     """
    #     Create new Ajax request to page
    #     :return:
    #     """
    #
    #     ajax_template = 'http://americanfork.chamberofcommerce.me/members/directory/search_1_column.php?org_id=AFCC&view_all_flag=X'
    #     return Request(ajax_template, callback=self.parse, method='POST')

    def parse(self, response):
        """
        Parsing of each page.
        :param response:
        :return:
        """

        soup = BeautifulSoup(response.body, 'html.parser')

        content = soup.find('span', attrs={'style': 'font-family:Verdana;font-size:11;'})

        for i in content.find_all('div', attrs={'style': 'border:1px solid #00a800; padding:10px;'}):
            d = 'sadsad'
            pass

        # dd = self.create_ajax_request()
        # yield dd

    # def parse_item(self, response):
    #     """
    #     Parsing of each article page.
    #     :param response:
    #     :return:
    #     """
    #     a = response.body
    #     self.logger.info('Crawling url {0}'.format(response.url))

        # content
        # /html/body/div[3]/table/tbody/tr/td/table/tbody/tr/td/span
        # .. /div


