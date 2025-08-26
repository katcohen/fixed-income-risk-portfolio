import pandas as pd, numpy as np, yfinance as yf, statsmodels.api as sm
from pandas_datareader import data as pdr
from datetime import date

def fetch_portfolio_returns(start="2015-01-01", end=None):
    tickers = ["IEF","LQD","HYG","EMB","TIP"]
    weights = pd.Series({"IEF":0.30,"LQD":0.30,"HYG":0.20,"EMB":0.10,"TIP":0.10})
    end = end or date.today().isoformat()
    px = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)["Close"]
    rets = px.pct_change().dropna()
    port = (rets * weights).sum(axis=1)
    return port, rets

def prepare_factors(start="2015-01-01", end=None):
    fred = pdr.DataReader(["GS2","GS10","T10YIE"], "fred", start).ffill()
    port, rets = fetch_portfolio_returns(start, end)
    factors = pd.DataFrame(index=port.index)
    factors["level"] = fred["GS10"].diff()
    factors["slope"] = (fred["GS10"] - fred["GS2"]).diff()
    factors["credit"] = rets["HYG"] - rets["LQD"]
    factors["inflation"] = fred["T10YIE"].diff()
    df = pd.concat([port.rename("port_ret"), factors], axis=1).dropna()
    return df

def run_factor_model(df):
    y = df["port_ret"]
    X = sm.add_constant(df[["level","slope","credit","inflation"]])
    model = sm.OLS(y, X).fit(cov_type="HC3")
    betas = model.params.drop("const")
    fac_var = df[["level","slope","credit","inflation"]].var()
    var_contrib = (betas**2 * fac_var) / (betas**2 * fac_var).sum()
    return model, betas, var_contrib

if __name__ == "__main__":
    df = prepare_factors()
    model, betas, var_contrib = run_factor_model(df)
    print(model.summary())
    print("\nBetas:\n", betas)
    print("\nVariance Contribution:\n", var_contrib)

import matplotlib.pyplot as plt
(fig := plt.figure(figsize=(6,4)))
plt.bar(var_contrib.index, var_contrib.values*100)
plt.ylabel("Variance Share (%)"); plt.title("Factor Variance Contribution")
plt.grid(True, axis="y")
fig.tight_layout()
fig.savefig("outputs/factor_variance_share.png", dpi=150)
