import requests
import json
import time
import datetime


def get_tick_data():
    r = requests.get('https://api.luno.com/api/1/tickers?pair=XBTZAR')
    json_resp = json.loads(r.text)
    tick_data_obj = json_resp['tickers'][0]
    timestamp = int(tick_data_obj['timestamp'])
    timestamp = datetime.datetime.fromtimestamp(timestamp/1000)
    timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    bid = float(tick_data_obj['bid'])
    ask = float(tick_data_obj['ask'])
    avg = (bid + ask) / 2
    print("Timestamp: ", timestamp, " Bid: ", bid, " Ask: ", ask, " Avg: ", avg)
    time.sleep(10)

while(True):
    get_tick_data()
