from crawler import start_crawler
from parser import Parser
from data_handler import DataHandler

class Main:
    def __init__(self, url: str):
        self.url = url
        self.crawler = start_crawler
        self.parser = Parser
        self.data_handler = DataHandler

    def start_crawling(self):
        # Start the crawler and get the HTML
        html = self.crawler(self.url)

        # Parse the HTML and get the data
        data = self.parser(html).parse()

        # Save the data
        self.data_handler(data).save_data()

if __name__ == "__main__":
    main = Main("http://www.example.com")
    main.start_crawling()
