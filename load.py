import pandas as pd 
cols = ["ts", "from_bank", "from_acct", "to_bank", "to_acct", "amt_recieved", "curr_recieved", "amt_paid", "curr_paid", "fmt", "is_laundering"]

def load_slice(path, skip=0, nrows=1_000_000):
    df = pd.read_csv(path, header=0, names=cols, skiprows=range(1, skip+1) if skip else None, nrows=nrows)
    df["ts"] = pd.to_datetime(df["ts"], format="%Y/%m/%d %H:%M")
    df["day"] = df["ts"].dt.floor("D")
    df["tx_id"] = range(skip, skip+len(df))
    return df