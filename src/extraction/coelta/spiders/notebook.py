import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebook#D[A:notebook]"]
    count_page = 1
    max_page = 5

    def parse(self, response):

        products = response.css('div.ui-search-result__wrapper')
    
        for product in products:
            preco = product.css('span.andes-money-amount__fraction::text').getall()
            yield {
                'Marca': product.css('span.poly-component__brand::text').get(),
                'Nome': product.css('a.poly-component__title::text').get(),
                'Vendedor': product.css('span.poly-component__seller::text').get(),
                'Número de classificação da revisão': product.css('span.poly-reviews__rating::text').get(),
                'Quantidade de avaliações': product.css('span.poly-reviews__total::text').get(),
                'Preço': preco[1] if len(preco) > 0 else None
            }
        if self.count_page < self.max_page:
            
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.count_page += 1
                yield scrapy.Request(url=next_page, callback=self.parse)

        #pass
#scrapy crawl notebook -o data.json
