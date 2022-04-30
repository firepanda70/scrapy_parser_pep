import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep in response.css('section[id="numerical-index"] tbody tr'):
            link = pep.css('a::attr(href)').get()
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('h1.page-title::text').get().split('–')
        number = int(number.replace('PEP', '').strip())
        name = name.strip()
        data = {
            'number': number,
            'name': name,
            'status': response.css('dt:contains("Status") + dd::text').get()
        }

        yield PepParseItem(data)
