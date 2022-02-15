# Abyiss Closing Price Percent Change
[![Python 3.7.9](https://img.shields.io/badge/python-3.7.9-blue.svg)](https://www.python.org/downloads/release/python-374/)


Shows the open price, close price, and price change over a specified timeframe specifically for the exchange coinbasepro and the market SHIB/USDT. The user has the option to view the full data or summarized data. You can also view current stats and compare it witha previous timeframe (in unixtimeframe).

## How to run this program
* Run the python file ```python3 technical.py```
* Follow the given input statements to obtain the data.
* A csv file will be generated based on the data provided.


## Bugs?
* The reason why it always display 0% change when comparing a previous aggregate price is because when calling client.lastAggregate, the time parameter doesn't seem to change the result. I am able to find time using exchange and market given 1m to 1d timeframe but not the other way around. There may be another function in the API that can obtain data from time but I'm not sure which function can perform that.
