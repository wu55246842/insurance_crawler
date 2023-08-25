from bs4 import BeautifulSoup
from typing import Dict, List

class Parser:
    def __init__(self, html: str):
        self.html = html

    def parse(self) -> List[Dict[str, str]]:
        soup = BeautifulSoup(self.html, 'html.parser')
        products = soup.find_all('div', class_='product')

        data = []
        for product in products:
            name = product.find('h2').text
            plan = product.find('div', class_='plan').text
            coverage = product.find('div', class_='coverage').text
            benefits = product.find('div', class_='benefits').text
            clauses = product.find('div', class_='clauses').text

            data.append({
                'name': name,
                'plan': plan,
                'coverage': coverage,
                'benefits': benefits,
                'clauses': clauses,
            })

        return data
