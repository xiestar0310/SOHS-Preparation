# use scrapy and beautifulsoup to get climate data
from bs4 import BeautifulSoup
import json
import sys
import requests
import scrapy

# Beautifulsoup web scraping

# whenever there's a list of fun facts in google results,
# each list item has the class "v9i61e"

FACT = "v9i61e"   

with open("assets/cache.json") as f:
    cache = json.loads(f.read())

class Info:
    def __init__(self, thing):
        self.thing = thing
        cached = cache.get(self.thing)
        if cached:
            self.getFacts = lambda: cached
        else:
            self.soup = BeautifulSoup(self.google(), 'html.parser')

    def google(self) -> str:
        request = requests.get(f"https://google.com/search?q=weather+in+{self.thing}")
        return request.text

    def getFacts(self):
        facts = self.soup.find_all("li", class_  =FACT)
        facts_better = [
            fact.get_text()
            for fact in facts]
        cache[self.thing] = facts_better
        with open("cache.json", "w") as f:
            f.write(json.dumps(cache))
        return facts_better

# scrapy as an alternative to beautifulsoup

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://google.com/search?q=weather+in+London']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)