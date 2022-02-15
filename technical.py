from Abyiss import Abyiss
from datetime import datetime
import csv


apiKey = "!gme)0y90Q8cM62fDA9605p09--^605^)NL" 
client = Abyiss.Client(apiKey)


timeframe = input("Enter timeframe(1m/5m/15m/1h/6h/1d): ")
ts = input("Show full or summarized data?(f/s): ")

def unixTotime(t):
    return datetime.fromtimestamp(t/1000).strftime('%Y-%m-%d %H:%M:%S')     # Current time, change to datetime.utcfromtimestamp if you want UTC time

# Obtain aggregates from the coinbasepro exchange, shiba-usd market
aggregates = client.aggregates("coinbasepro", "SHIB-USDT", timeframe)

print("------------------------------------------------------")
print("\nExchange: ",aggregates.get("exchange"))
print("Market: ",aggregates.get("market"))
if ts == 'f':
    for i in range(len(aggregates.get("aggregates"))):
        
        print("Open Price: {:.15f} {:>15} {:.15f}".format(float(aggregates.get("aggregates")[i].get("o")), "Close Price:", aggregates.get("aggregates")[i].get("c")), end="")
        if i == 0:
            print("     Closing Price % Change From Previous Aggregate:1 ", "0%", "      Time:", unixTotime(aggregates.get("aggregates")[i].get("t")))
        else:  
            print("     Closing Price % Change From Previous Aggregate: {:.3f}%     Time: {}".format(float(aggregates.get("aggregates")[i].get("c")) / float(aggregates.get("aggregates")[i-1].get("c")) * 100-100, unixTotime(aggregates.get("aggregates")[i].get("t"))))
            

if ts == 's':
    print("First Aggregate:")
    print("Open Price: ", aggregates.get("aggregates")[0].get("o"), "Close Price: ", aggregates.get("aggregates")[0].get("c"), "Time: ", unixTotime(aggregates.get("aggregates")[0].get("t")))
    print("")
    print("Last Aggregate:")
    print("Open Price: ", aggregates.get("aggregates")[-1].get("o"), "Close Price: ", aggregates.get("aggregates")[-1].get("c"), "Time: ", unixTotime(aggregates.get("aggregates")[-1].get("t")))
    print("")
    print("Closing Price % Change From Previous Aggregate: {:.3f}%".format(float(aggregates.get("aggregates")[-1].get("c"))/float(aggregates.get("aggregates")[0].get("c"))*100-100))
    print("")

print("Total Aggregates: ", len(aggregates.get("aggregates")), "in the timeframe ", timeframe)

# Writing to csv file
with open('SHIB-USDT_percentchange.csv', 'w', newline='') as csvfile:
    fieldnames = ['Open Price', 'Close Price', 'Time']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(aggregates.get("aggregates"))):
        writer.writerow({'Open Price': aggregates.get("aggregates")[i].get("o"), 'Close Price': aggregates.get("aggregates")[i].get("c"), 'Time': unixTotime(aggregates.get("aggregates")[i].get("t"))})
print("\nCSV file created\n")

print("------------------------------------------------------")

print("Current Stats:")
current = ("coinbasepro", "SHIB-USDT",str(datetime.now().timestamp()))

print("Open Price: {:.20f}".format(client.lastAggregate(current[0], current[1], current[2]).get("o")))
print("Close Price: {:.20f}".format(client.lastAggregate(current[0], current[1], current[2]).get("c")))

print("Time: ", unixTotime(client.lastAggregate(current[0], current[1], current[2]).get("t")))

comp = (input("Do you want to compare from a previous time (type unix timestamp or 0 for no)?"))
if comp != '0':
    print("Closing Price % Change From Previous Aggregate: {:.3f}%".format(float(client.lastAggregate(current[0], current[1], current[2]).get("c")) / float(client.lastAggregate(current[0], current[1], comp).get("c")) * 100 - 100))

# The reason why it always display 0% change is because when calling client.lastAggregate, the time parameter doesn't seem to change the result. See the last 2 print statements
# I am able to find time using exchange and market given 1m to 1d timeframe but not the other way around.
print(client.lastAggregate(current[0], current[1], current[2]))
print(client.lastAggregate("coinbasepro", "SHIB-USDT", '1543000000'))