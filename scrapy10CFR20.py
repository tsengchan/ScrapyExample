@@ -0,0 +1,43 @@
import scrapy

#scrapy example scrape radiation regulations
class QuotesSpider(scrapy.Spider):
    name = "class1"

    def start_requests(self):
        urls = [
            'https://www.nrc.gov/reading-rm/doc-collections/cfr/part020/',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) #Request generates Response passes to parse()

    def parse(self, response):


        yield{
            'text': response.xpath('//div[@id="mainSubFull"]/p/a/text()').extract(),

            }


        next_page =  response.xpath('//div[@id="mainSubFull"]/p/a/@href').extract()

        if next_page is not None:
            for part in next_page: #loop through sub urls

                next_page = response.urljoin(part)
                #this opens sub url
                yield scrapy.Request(next_page, callback=self.parse_page)


    def parse_page(self, response):
        maintext = response.meta.get('maintext')



        yield{

            'subSection': response.xpath('//div[@id="mainSubFull"]/p/text()').extract(),

             }
