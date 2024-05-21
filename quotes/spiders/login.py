from typing import Iterable, Any

import scrapy
from scrapy import Request, FormRequest
from scrapy.http import Response


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse_login(self, response):
        ret = FormRequest.from_response(
            response=response,
            formdata={
                'username': 'rivka',
                'password': '1111'
            }
        )
        self.log('Sent: ' + str(ret))
        return ret

    def start_requests(self) -> Iterable[Request]:
        return [
            Request(
                'https://quotes.toscrape.com/login',
                callback=self.parse_login
            )
        ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        pass
