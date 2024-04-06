from scrapy import Spider
from scrapy.http import Request,Response
from scrapy_playwright.page import PageMethod

class CityAirSpider(Spider):
    
    name="cityspider"
    start_urls=["https://www.iqair.com/world-most-polluted-cities/"]
    
    def start_requests(self):
        meta=dict(
            playwright=True,
            playwright_include_page=True,
            playwright_page_methods=[PageMethod("wait_for_selector","div.table-body")]
        )
        yield Request(url=self.start_urls[0],callback=self.parse_city,meta=meta)
        
    def parse_city(self,response:Response):
        
        val_city={}
        arr=[]
        if response.status == 200 :
            
            city_table=response.xpath(".//table[contains(@class,'mat-table')]/tbody")
            for city in city_table:
                city_rank=city.xpath(".//tr/td[contains(@class,'mat-column-ranking')]//text()").extract()
            
            for row in city_table:
                for index,value in enumerate(city_rank):
                    val_city[value]=row.xpath(f".//tr[{index+1}]//text()").getall()
                arr.append(val_city)
            
            yield {"d":arr}