import pandas as pd


def random_date():
    df = pd.read_csv(f"TECL.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df2 = df[df.index > '2020-01-01']
    return pd.to_datetime(df2.sample().index[0])


def stock_prices():
    initial_date = random_date()
    results = []
    for stock in ['SPY', 'TECL']:
        df = pd.read_csv(f"{stock}.csv")
        df = df[['Date', 'Close/Last']]
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        result_df = df.loc[initial_date:].resample('MS').first()
        results.append(result_df.tail(12))

    merged = pd.concat(results, axis=1)
    merged.columns = ['SPY', 'TECL']
    return merged
