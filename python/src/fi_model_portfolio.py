import os, pandas as pd, numpy as np, yfinance as yf
from datetime import date

TICKERS = {
    "Core_Intermediate": "AGG",
    "Multisector": "BOND",          # or DBND
    "Short_Term": "SHY",            # or SPSB / IGSB
    "IG_Corporate": "LQD",
    "World_Hedged": "BNDX",
    "Nontraditional": "TOTL",
    "High_Yield": "HYG",
    "Bank_Loans": "BKLN",
    "Ultrashort": "ICSH",           # or SHV
    "Muni_Intermediate": "MUB",
}

WEIGHTS = pd.Series({
    "Core_Intermediate": 0.27,
    "Multisector": 0.23,
    "Short_Term": 0.13,
    "IG_Corporate": 0.07,
    "World_Hedged": 0.06,
    "Nontraditional": 0.07,
    "High_Yield": 0.05,
    "Bank_Loans": 0.05,
    "Ultrashort": 0.04,
    "Muni_Intermediate": 0.03,
}, name="weight")

assert abs(WEIGHTS.sum()-1.0) < 1e-9, "Weights must sum to 1."

def fetch_prices(start="2015-01-01", end=None):
    end = end or date.today().isoformat()
    tickers = list(TICKERS.values())
    px = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)["Close"]
    px.columns = [c if isinstance(c,str) else c[1] for c in px.columns]  # flatten if needed
    return px

def summarize_portfolio(rets, rf=0.0):
    ann_ret = (1+rets).prod()**(252/len(rets)) - 1
    ann_vol = rets.std()*np.sqrt(252)
    sharpe = (ann_ret - rf)/ann_vol if ann_vol>0 else np.nan
    cum = (1+rets).cumprod()
    roll_max = cum.cummax()
    mdd = (cum/roll_max - 1).min()
    return pd.Series({
        "ann_return": ann_ret, "ann_vol": ann_vol, "sharpe": sharpe, "max_drawdown": mdd
    })

if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)

    px = fetch_prices(start="2015-01-01")
    rets = px.pct_change().dropna()

    # Map weights to tickers
    w_tickers = WEIGHTS.rename(index=TICKERS)  # index becomes tickers
    w_tickers = w_tickers.groupby(w_tickers.index).sum()  # if you swap proxies

    # Portfolio daily returns
    port_ret = (rets[w_tickers.index] * w_tickers).sum(axis=1)

    # Save outputs
    WEIGHTS.to_csv("outputs/fi_model_portfolio_weights.csv")
    port_ret.to_frame("portfolio_ret").to_csv("outputs/fi_model_portfolio_returns.csv")
    summary = summarize_portfolio(port_ret)
    summary.to_frame("value").to_csv("outputs/fi_model_portfolio_summary.csv")
    print(summary.round(4))
