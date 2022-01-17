import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath('//table[@class="jsx-3979628367 table table-striped tp-table-body"]/tbody/tr')

        for row in rows:
            country = row.xpath('.//td[1]/a/text()').get()
            gdp_debt = row.xpath('.//td[2]/text()').get()
            population = row.xpath('.//td[3]/text()').get()

            yield {
                'country': country,
                'gdp_debt': gdp_debt,
                'population': population
            }
