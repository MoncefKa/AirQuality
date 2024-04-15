

from scrapy import Field,Item


class AirqualityscraperItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    Title = Field()
    CountryName = Field()
    CountryRank = Field()
    CountryAirQuality = Field()

class CityAirQuality(Item):
    
    CityAir=Field()