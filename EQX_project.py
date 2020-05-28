#Practice grabbing info from yahoo finance using Equinox Gold as an example

import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
from datetime import date
from datetime import datetime
import yfinance as yf
yf.pdr_override()
import pandas as pd
import csv

def get_from_yahoo_finance(tick):
	#call yahoo finance to retrieve info on EQX stock and store this in a csv

	gold_data = pdr.get_data_yahoo(tick, start='2018-01-01', end=date.today())
	stock_name = 'EQX'+'_'+str(date.today())
	#store the info in a csv
	#.to_csv will create the file if it isn't there, but cannot move through directory paths that don't exist
	gold_data.to_csv(stock_name+'.csv')
	print(f"Created a folder: {stock_name}.")

def compile_EQX_data():
	#compile data from EQX csv into lists

	get_from_yahoo_finance('EQX')
	file = 'EQX_'+str(date.today())+'.csv'
	with open(file) as f:
		read_file = csv.reader(f)
		header_row = next(read_file)

		#store all data from EQX file in appropriate list
		dates = []
		opens = []
		highs = []
		lows = []
		closes = []
		adj_closes = []
		volumes = []

		for row in read_file:
			format_date = datetime.strptime(row[0], '%Y-%m-%d')
			dates.append(format_date)
			opens.append(row[1])
			highs.append(row[2])
			lows.append(row[3])
			closes.append(row[4])
			adj_closes.append(row[5])
			volumes.append(row[6])

	return dates, opens, highs, lows, closes, adj_closes, volumes

def graph_EQX():
	#Graph EQX stock data using matplotlib

	dates, opens, highs, lows, closes, adj_closes, volumes = compile_EQX_data()

	short_dates = []
	short_closes = []
	for i in range(75):
		short_dates.append(dates[i])
		close_float = float(closes[i])
		short_closes.append(round(close_float, 3))

	#plot the price data, overlay the exact points onto the trend line
	plt.plot(short_dates, short_closes)
	plt.scatter(short_dates, short_closes)
	plt.xlabel('Date')
	plt.ylabel('Close Price')
	plt.title('EQX Gold: Close Prices for Brief Slice of Time')
	plt.show()


graph_EQX()