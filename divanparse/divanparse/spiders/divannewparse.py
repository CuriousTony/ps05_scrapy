import scrapy


class DivannewparseSpider(scrapy.Spider):
    name = "divannewparse"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/sankt-peterburg/category/torshery"]

    def parse(self, response):
        lighting = response.css('div.WdR1o')
        for light in lighting:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('span.ui-LD-ZU.KIkOH::text').get(),
                'link': f"https://www.divan.ru{light.css('a').attrib['href']}"
            }
