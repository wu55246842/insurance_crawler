import pandas as pd
from typing import List, Dict

class DataHandler:
    def __init__(self, data: List[Dict[str, str]], output_format: str = 'csv'):
        self.data = pd.DataFrame(data)
        self.output_format = output_format

    def save_data(self, filename: str = 'output'):
        if self.output_format == 'csv':
            self.data.to_csv(f'{filename}.csv', index=False)
        elif self.output_format == 'excel':
            self.data.to_excel(f'{filename}.xlsx', index=False)
        elif self.output_format == 'json':
            self.data.to_json(f'{filename}.json')
        else:
            raise ValueError('Invalid output format. Please choose from "csv", "excel", or "json".')
