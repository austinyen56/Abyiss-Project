from Abyiss import Abyiss

apiKey = "!gme)0y90Q8cM62fDA9605p09--^605^)NL" 
client = Abyiss.Client(apiKey)

timeframe = input("Enter timeframe(1m/5m/15m/1h/6h/1d): ")
ts = input("Show full or summarized data?(f/s): ")

# Obtain aggregates from the coinbasepro exchange, shiba-usd market
aggregates = client.aggregates("coinbasepro", "SHIB-USDT", timeframe)
print("Exchange: ",aggregates.get("exchange"))
print("Market: ",aggregates.get("market"))
if ts == 'f':
    for i in range(len(aggregates.get("aggregates"))):
        
        print("Open Price: {:.15f} {:>15} {:.15f}".format(float(aggregates.get("aggregates")[i].get("o")), "Close Price:", aggregates.get("aggregates")[i].get("c")), end="")
        if i == 0:
            print("     Closing Price % Change From Previous Aggregate: ", 0,"%")
        else:
            print("     Closing Price % Change From Previous Aggregate: {:.3f}%".format(float(aggregates.get("aggregates")[i].get("c"))/float(aggregates.get("aggregates")[i-1].get("c"))*100-100))
            

else:
    print("First Aggregate:")
    print("Open Price: ", aggregates.get("aggregates")[0].get("o"), "Close Price: ", aggregates.get("aggregates")[0].get("c"), "Time: ", aggregates.get("aggregates")[0].get("t"))
    print("")
    print("Last Aggregate:")
    print("Open Price: ", aggregates.get("aggregates")[-1].get("o"), "Close Price: ", aggregates.get("aggregates")[-1].get("c"), "Time: ", aggregates.get("aggregates")[-1].get("t"))
    print("")
    print("Closing Price % Change From Previous Aggregate: {:.3f}%".format(float(aggregates.get("aggregates")[-1].get("c"))/float(aggregates.get("aggregates")[0].get("c"))*100-100))
    print("")
    
print("Total Aggregates: ", len(aggregates.get("aggregates")), "in the timeframe ", timeframe)