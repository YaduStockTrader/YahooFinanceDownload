# This file will download data from YahooFinance Using yfinance
import sys
from datetime import date

import yfinance as yf

filepath = sys.argv[1]
input_symbol = sys.argv[2]
input_from_date = sys.argv[3]


def download_data(file_location, input_sym, from_date):
    symbol_list = input_sym.split("|")
    end_date = date.today()
    start_date = from_date
    print("From Date - : " + start_date)
    print(end_date)
    for forex_symbol in symbol_list:
        print(forex_symbol)
        data = yf.download(forex_symbol, start=start_date, end=end_date)
        data.to_csv(file_location + "\\" + forex_symbol + ".csv")


download_data(filepath,input_symbol, input_from_date)
print("************ File Download Completed Successfully ************")
