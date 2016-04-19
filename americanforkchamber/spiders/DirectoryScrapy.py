# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.utils.response import open_in_browser

from .. import items


class DirectorySpider(Spider):
    name = "directory"
    allowed_domains = ["americanforkchamber.org"]
    start_urls = (
        'http://americanfork.chamberofcommerce.me/members/directory/search_1_column.php?org_id=AFCC&view_all_flag=X',
    )

    def parse(self, response):
        """
        Parsing of each page.
        :param response:
        :return:
        """

        try:
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
                        record[
                            'address_book_link'] = 'http://americanfork.chamberofcommerce.me/members/directory/{0}'.format(
                            link.strip())
                        continue
                    if 'http' in link:
                        record['link'] = link.strip()
                        continue

                address = item.xpath('.//text()').extract()
                address = address[2:len(address) - 4]
                if len(address) > 4:
                    record['author_job'] = address[0].strip()
                    address = address[1:]

                record['phone'] = address[-1:].pop().strip()
                record['address'] = ' '.join(address[1:-2]).replace('  ', ' ')

                yield record

        except IndexError as e_index:
            print(e_index)
