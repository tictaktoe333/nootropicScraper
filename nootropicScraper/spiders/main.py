import scrapy
#scrapy shell
#fetch('URL')

#Run spider
#scrapy crawl nootropics -O output.json

class nootropicSpider(scrapy.Spider):
    name = 'nootropics'
    start_urls = ['https://nootropics-database.com']

    def parse(self, response):
        for row in response.css('tbody.MuiTableBody-root'):
            yield {
                'Name': row.css('td:nth-child(2) > a::text').getall(),
                'OA': row.css('td:nth-child(3)::text').getall(),
                'Sleep': row.css('td:nth-child(4)::text').getall(),
                'Mood': row.css('td:nth-child(5)::text').getall(),
                'Memory': row.css('td:nth-child(6)::text').getall(),
                'Focus': row.css('td:nth-child(7)::text').getall(),
                'Creativity': row.css('td:nth-child(8)::text').getall(),
                'Confidence': row.css('td:nth-child(9)::text').getall(),
                'Social': row.css('td:nth-child(10)::text').getall(),
                'Learning': row.css('td:nth-child(11)::text').getall(),
                'Motivation': row.css('td:nth-child(12)::text').getall(),
                'Energy': row.css('td:nth-child(13)::text').getall(),
                'Anti-stress': row.css('td:nth-child(14)::text').getall(),
                'Alertness': row.css('td:nth-child(16)::text').getall()
            }
            