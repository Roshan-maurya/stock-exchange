import requests
import pandas as pd
def get_data(symbol,time, API_KEY):
    r = requests.get('https://www.alphavantage.co/query?function='+time+'&symbol='+symbol+'&apikey='+API_KEY+'')

    dataIntraday = r.json()
    if(time == 'TIME_SERIES_DAILY'):
        return dataIntraday['Time Series (Daily)']
    elif(time == 'TIME_SERIES_WEEKLY'):
        return dataIntraday['Weekly Time Series']
    elif(time == 'TIME_SERIES_MONTHLY'):
        return dataIntraday['Monthly Time Series']        

def convert_to_df(data):
    """Convert the result JSON in pandas dataframe"""
    
    df = pd.DataFrame.from_dict(data, orient='index')
    
    df = df.reset_index()

    #we rename columns

    df = df.rename(index=str, columns={"index": "date", "1. open": "open",
    "2. high": "high", "3. low": "low", "4. close": "close"})
    
    #change to datetime

    df['date'] = pd.to_datetime(df['date'])

    #sort data according to date

    df = df.sort_values(by=['date'])

    #change the datatype

    df.open = df.open.astype(float)
    df.close = df.close.astype(float)
    df.high = df.high.astype(float)
    df.low = df.low.astype(float)
    
    #Checks
    df.head()
    df.info()

    return df