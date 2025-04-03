import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import getpass
from datetime import date, datetime
import os

log_path = 'log.csv'


def log(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        
        user_name = getpass.getuser()
        func_name = func.__name__
        formatted_date = date.today().strftime("%d-%m-%Y")
        formatted_time = datetime.now().time()

        if os.path.isfile("logs.csv"):
            print("Файл существует")
            file_df = pd.read_csv("logs.csv")
            df = pd.DataFrame([len(file_df),user_name, func_name,formatted_date, formatted_time],
            columns=['id','user_name', 'func_name', 'formatted_date', 'data_time'])
            df.to_csv('logs.csv', mode='a', index=False)

        else:
            print("Файл не существует")
            df = pd.DataFrame([0 ,user_name, func_name,formatted_date, formatted_time],
            columns=['id','user_name', 'func_name', 'formatted_date', 'data_time'])
            df.to_csv('logs.csv')


        return original_result
    return wrapper

class Cost():
    def __init__(self, log_path):
        self.log_path = log_path

    def processing(self):
        data = pd.read_csv('log.csv')
        clean_data: pd.DataFrame = data.drop(columns=['Adj Close','Volume'])
        sns.barplot(data=clean_data)
        plt.xlabel('Фиксированная дата')
        plt.ylabel('Изменения')

        sns.set_style("bluegrid")
        sns.boxplot(x='Фиксированная дата', y='Изменения', data=sns.load_dataset('iris'))
        plt.title('Стоимость акций APPLE')
        plt.show()


apple_cost = Cost(log_path)
apple_cost.processing()
    
