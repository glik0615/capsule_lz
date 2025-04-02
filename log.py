import pandas as pd
import matplotlib.pyplot as plt

log_path = 'log.py'

class Cost():
    def __init__(self, log_path):
        self.log_path = log_path

    def processing(self):
        data: pd.DataFrame = pd.read_csv('log.csv')
        clean_data: pd.DataFrame = data.dropna(subset=['column_name'])


        
    def graph(self,clean_data):
        plt.hist(clean_data['column_name'], bins=10, color='blue')
        plt.title('Стоимость акций Apple')
        plt.xlabel('Дата')
        plt.ylabel('Значение изменений')
        plt.show()
