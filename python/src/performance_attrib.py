import pandas as pd
from pathlib import Path

def brinson_allocation_selection(port_ret, bench_ret, w_p, w_b):
    """
    One-period Brinson attribution.
    port_ret, bench_ret, w_p, w_b: pandas Series indexed by the same asset names.
    Returns a Series with Allocation, Selection, Interaction, Active Return.
    """
    port_ret  = pd.Series(port_ret, dtype=float)
    bench_ret = pd.Series(bench_ret, dtype=float)
    w_p       = pd.Series(w_p, dtype=float)
    w_b       = pd.Series(w_b, dtype=float)

    # align on common assets
    port_ret, bench_ret = port_ret.align(bench_ret, join="inner")
    w_p = w_p.reindex(port_ret.index)
    w_b = w_b.reindex(port_ret.index)

    # normalize weights
    w_p = w_p / w_p.sum()
    w_b = w_b / w_b.sum()

    # Brinson-Linke one-period decomposition
    A = ((w_p - w_b) * bench_ret).sum()                # allocation
    S = (w_b * (port_ret - bench_ret)).sum()           # selection
    I = ((w_p - w_b) * (port_ret - bench_ret)).sum()   # interaction
    total = (w_p*port_ret).sum() - (w_b*bench_ret).sum()

    return pd.Series({
        "Allocation": A,
        "Selection": S,
        "Interaction": I,
        "Active Return": total
    })

def _example_and_save():
    # Example placeholders — replace with real monthly sleeve series later
    assets    = ["HY_Core","HY_Short","EM_Bonds"]
    port_ret  = pd.Series([0.012, 0.006, 0.008], index=assets)
    bench_ret = pd.Series([0.010, 0.007, 0.007], index=assets)
    w_p       = pd.Series([0.60, 0.25, 0.15], index=assets)
    w_b       = pd.Series([0.70, 0.20, 0.10], index=assets)

    out = brinson_allocation_selection(port_ret, bench_ret, w_p, w_b)
    print(out)

    # Save CSV to python/outputs/
    out_df = out.to_frame("Value")
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "hy_perf_attrib_example.csv"
    out_df.to_csv(csv_path, float_format="%.6f")
    print(f"\n✔ Saved {csv_path}")

if __name__ == "__main__":
    _example_and_save()
