import scrapy
from scrapy_selenium import SeleniumRequest
from daraz.items import DarazItem

class ClothSpider(scrapy.Spider):
    name = 'cloth'

    def start_requests(self):
        for page in range(1,103):
            url = f'https://www.daraz.com.bd/womens-traditional-clothing/?page={page}'
            yield SeleniumRequest(
                url=url,
                callback = self.parse_page
            )

    def parse_page(self, response):
        product_links = response.css('div.gridItem--Yd0sa div.title--wFj93 a::attr(href)').getall()
        for link in product_links:
            yield SeleniumRequest(
                url = "https://" + link,
                callback = self.parse_product,
            )

    def parse_product(self, response):
        scrape_item = DarazItem()
        scrape_item['title'] = response.css('span.pdp-mod-product-badge-title::text').get()
        scrape_item['disc_price'] = response.css('span.pdp-price_type_normal::text').get()
        scrape_item['discount'] = response.css('span.pdp-product-price__discount::text').get()
        scrape_item['original_price'] = response.css('span.pdp-price_type_deleted::text').get()
        scrape_item['rating'] = response.xpath('//div[@class="pdp-review-summary"]//a[contains(text(),"Rating")]/text()').get()
        scrape_item['review'] = response.xpath('//div[@class="pdp-review-summary"]//a[contains(text(),"Question")]/text()').get()
        scrape_item['brand'] = response.css('a.pdp-product-brand__brand-link::text').get()
        scrape_item['std_deliver_fee'] = response.xpath('(//div[@class="delivery-option-item__shipping-fee"])[1]/text()').get()
        scrape_item['return_policy'] = response.xpath('//div[contains(text(), "Return")]/text()').getall()
       
        yield scrape_item