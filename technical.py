from Abyiss import Abyiss

apiKey = "!gme)0y90Q8cM62fDA9605p09--^605^)NL" 
client = Abyiss.Client(apiKey)

#exchanges = client.getExchanges()
#exchangeDetails = client.getExchangeDetails("coinbasepro")
#exchangeStatus = client.getExchangeStatus("coinbasepro")
#exchangeMarkets = client.getExchangeMarkets("coinbasepro")
#exchangeMarketDetails = client.getMarketDetails("coinbasepro", "BTC-USDT")
##aggregates = client.aggregates("coinbasepro", "BTC-USDT", "1h", '300')
#aggregates = client.aggregates("coinbasepro", "BTC-USD", "1m", "250")
#trades = client.trades("coinbasepro", "BTC-USDT", '300')
#quotes = client.quotes("coinbasepro", "BTC-USDT")
#orderbook = client.orderBook("coinbasepro", "BTC-USDT")

timeframe = input("Enter timeframe(1m/5m/15m/1h/6h/1d): ")
ts = input("Show all timestamps?(y/n): ")

# Obtain aggregates from the coinbasepro exchange, shiba-usd market
aggregates = client.aggregates("coinbasepro", "SHIB-USDT", timeframe)
if ts == 'y':
    for i in range(len(aggregates.get("aggregates"))):
        print("Open Price: ", aggregates.get("aggregates")[i].get("o"), "Close Price: ", aggregates.get("aggregates")[i].get("c"))
else:
    print("Open Price: ", aggregates.get("aggregates")[0].get("o"), "Close Price: ", aggregates.get("aggregates")[-1].get("c"))
    print(float(((aggregates.get("aggregates")[0].get("c") - aggregates.get("aggregates")[0].get("o")) * 100) / aggregates.get("aggregates")[0].get("o"))*100)

