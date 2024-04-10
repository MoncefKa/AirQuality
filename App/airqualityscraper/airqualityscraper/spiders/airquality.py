from airqualityscraper.items import AirqualityscraperItem as AQI
import scrapy
from scrapy.http import Request
from scrapy_playwright.page import PageMethod

class AirqualitySpider(scrapy.Spider):
    
    name = "airquality"
    allowed_domains = ["www.iqair.com"]
    start_urls = ["https://www.iqair.com/world-most-polluted-countries"]
    
    
    def start_requests(self):
        meta=dict(
            playwright=True,
            playwright_include_page=True,
            playwright_page_methods=[PageMethod("wait_for_selector","div.ranking-column")]
        )
        
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse_titles,meta=meta,dont_filter=True)
            yield Request(url=url,callback=self.parse_table,meta=meta,dont_filter=True)


    def parse_titles(self,response):
        item = AQI()
        table_header = response.xpath(".//table[contains(@class,'mat-table')]")
        for header in table_header:
            head=header.xpath(".//thead/tr/th//text()").extract()
            item["Title"]=head
        yield item
         

    def parse_table(self, response):
        item = AQI()
        year_data=list()
        if response.status == 200:
        
            table_row = response.xpath(".//table[contains(@class,'mat-table')]/tbody/tr")
            for row in table_row:
                col_rank = row.xpath(".//td[contains(@class,'cdk-column-rank')]//text()").get()
                col_country = row.xpath(".//td[contains(@class,'cdk-column-country')]//text()").get()
                
                year_data=[]
                
                for i in range(2018, 2024):
                    col_year_data = row.xpath(f".//td[contains(@class,'cdk-column-avg{i}')]//text()").get()
                    year_data.append(col_year_data)
                    
                item["CountryName"]=col_country
                item["CountryRank"]=col_rank
                item["CountryAirQuality"]=col_year_data
                yield item