import numpy as np, pandas as pd

BOOK = pd.DataFrame({
    "asset": ["IG (LQD)","HY (HYG)","Treasuries (IEF)","MBS (MBB)"],
    "w":     [0.40,      0.25,       0.25,               0.10],
    "dur":   [8.8,       4.0,        7.5,                6.0],
    "s_dur": [7.5,       3.5,        0.0,                0.8]
})

def pnl_rate_spread(book, d_rate_bps=0.0, d_spread_bps=0.0):
    dy = d_rate_bps/10000.0; ds = d_spread_bps/10000.0
    rr = -(book["dur"]*dy + book["s_dur"]*ds)
    port = (book["w"]*rr).sum()
    return rr, port

SCENARIOS = {
    "Parallel +100bps": {"d_rate_bps":100, "d_spread_bps":0},
    "Recession: +150bps spreads, -50bps rates": {"d_rate_bps":-50, "d_spread_bps":150},
    "Higher-for-longer: +50bps rates, +50bps spreads": {"d_rate_bps":50, "d_spread_bps":50},
    "Risk-off: -75bps rates, +200bps spreads": {"d_rate_bps":-75, "d_spread_bps":200}
}

def run_scenarios():
    rows=[]
    for name, s in SCENARIOS.items():
        rr, port = pnl_rate_spread(BOOK, **s)
        rows.append([name, port*100])
    out = pd.DataFrame(rows, columns=["Scenario","Port ΔP/P (%)"]).round(2)
    return out

# Historical VaR/ES (if you have a pd.Series of returns)
def var_es_hist(returns: pd.Series, alpha=0.95):
    r = returns.dropna().sort_values()
    idx = int((1-alpha)*len(r))
    var = float(r.iloc[idx])

    out = run_scenarios()
    print(out.to_string(index=False))

import os
if __name__ == "__main__":
    out = run_scenarios()
    print(out.to_string(index=False))

    import os
    os.makedirs("outputs", exist_ok=True)
    out.to_csv("outputs/stress_results.csv", index=False)

if __name__ == "__main__":
    out = run_scenarios()
    print(out.to_string(index=False))

out = run_scenarios()
import os; os.makedirs("outputs", exist_ok=True)
out.to_csv("outputs/stress_results.csv", index=False)
