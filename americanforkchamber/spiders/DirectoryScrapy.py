# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector
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
    #     return Request(ajax_template, callback=self.parse, method='POST')

    def parse(self, response):
        """
        Parsing of each page.
        :param response:
        :return:
        """

        # soup = BeautifulSoup(response.body, 'html.parser')
        # content = soup.find('span', attrs={'style': 'font-family:Verdana;font-size:11;'})
        # for i in content.find_all('div', attrs={'style': 'border:1px solid #00a800; padding:10px;'}):
        #     d = 'sadsad'
        #     pass

        blocks = Selector(response=response).xpath('//span/div[@style="border:1px solid #00a800; padding:10px;"]')
        for block in blocks:
            record = items.DirectoryItem()

            item = block.xpath('.//tr/td')
            header = item.xpath('.//div/span//text()').extract()

            record['title'] = header[0]
            record['author'] = header[1]

            links = item.xpath('.//a//@href').extract()
            for link in links:
                if 'mailto' in link:
                    record['email'] = link
                    continue
                if 'vcard.php?' in link:
                    record['address_book_link'] = link.strip()
                    continue
                if 'http' in link:
                    record['link'] = link.strip()
                    continue

            address = item.xpath('.//text()').extract()
            address = address[2:len(address)-4]
            if len(address) > 4:
                record['author_job'] = address[0].strip()
                address = address[1:]

            record['phone'] = address[-1:].pop().strip()
            record['address'] = ' '.join(address[1:-2]).replace('  ', ' ')

            yield record

        # content
        # /html/body/div[3]/table/tbody/tr/td/table/tbody/tr/td/span
        # .. /div
