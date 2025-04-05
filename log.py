import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

import getpass
from datetime import date, datetime
import pandas as pd
import os


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

class Cost:

    def __init__(self):
        pass
    
    @log
    def processing(self):
        # Чтение данных из CSV файла
        data = pd.read_csv('log.csv')
        print("Прочитанные данные:")
        print(data.head())

        # Построение гистограммы
        x = data['Date'].tolist()
        y = data['Open'].tolist()
        y1 = data['High'].tolist()
        y2 = data['Close'].tolist()
        y3 = data['Low'].tolist()
        plt.scatter(x,y1, color = 'green')
        plt.bar(x,y)
        plt.bar(x,y2)
        plt.scatter(x,y3, color = 'red')
        plt.xlabel('Дата')
        plt.ylabel('Изменения')
        plt.title('Гистограмма стоимости акций Apple')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

apple_cost = Cost()
apple_cost.processing()


