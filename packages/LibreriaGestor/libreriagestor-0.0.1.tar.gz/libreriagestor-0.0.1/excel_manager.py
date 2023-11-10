import pandas as pd

class ExcelManager:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        try:
            data = pd.read_excel(self.filename, dtype={'completed': bool})
            return data
        except FileNotFoundError:
            return pd.DataFrame()

    def save_data(self, data):
        data.to_excel(self.filename, index=False)

    def update_data(self, updated_data):
        current_data = self.load_data()
        updated_data = pd.concat([current_data, updated_data], ignore_index=True)
        updated_data.drop_duplicates(subset=['description'], keep='last', inplace=True)
        self.save_data(updated_data)
