import requests
from bs4 import BeautifulSoup
import tkinter as tk

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url)
        self.soup = BeautifulSoup(self.data.content, 'html.parser')
        self.rate = self.get_rate()

    def get_rate(self):
        rate = self.soup.find('div', attrs={'class': 'col-md-4'}).find_all('div', attrs={'class': 'value'})[1].text
        return float(rate.replace(',', '.'))

    def convert(self, amount):
        return round(amount / self.rate, 2)

class App:
    def __init__(self):
        self.converter = CurrencyConverter('https://bank.gov.ua/ua/markets/exchangerates')
        self.root = tk.Tk()
        self.root.title('Currency Converter')
        self.root.geometry('300x150')

        self.label = tk.Label(self.root, text='Enter amount in UAH:')
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.button = tk.Button(self.root, text='Convert', command=self.convert)
        self.button.pack(pady=5)

        self.result = tk.Label(self.root, text='')
        self.result.pack(pady=10)

    def convert(self):
        amount = float(self.entry.get())
        result = self.converter.convert(amount)
        self.result.config(text=f'{amount} UAH = {result} USD')

app = App()
app.root.mainloop()
