Fixed-Income Model Portfolio — Analyst Memo

Analyst: Katherine Cohen
Period: 2015-present (daily)
Implementation: ETF sleeves per advisor-style allocation

Objective:
Evaluate a diversified, advisor-style fixed-income model portfolio built from liquid ETFs and identify risk drivers and actionable improvements under current macro conditions (sticky inflation, “higher-for-longer” policy risk, tariff-related cost pressures, and late-cycle growth uncertainty).

Portfolio & Method
Sleeves / tickers (weights):
- Core Intermediate (AGG, 27%), Multisector (BOND, 23%), Short-Term (SHY, 13%), IG Corporate (LQD, 7%), World Hedged (BNDX, 6%), Nontraditional/Unconstrained (TOTL, 7%), High Yield (HYG, 5%), Bank Loans (BKLN, 5%), Ultrashort (ICSH, 4%), Muni Intermediate (MUB, 3%).
- Prices from Yahoo Finance; daily total-return proxies via adjusted close.
- Portfolio return = ∑(sleeve return × weight), rebalanced implicitly by weights.
- Summary metrics: annualized return/volatility, Sharpe (rf=0 as implemented), and max drawdown.

Results (2015-present):
Annualized return: 2.08%
Annualized volatility: 4.06%
Sharpe ratio (rf=0): 0.51
Max drawdown: -15.11%

Note: Sharpe here uses rf=0 (per code). Using a positive realized cash yield would reduce the Sharpe; interpret the 0.51 as an ex-cash risk-adjusted indicator.

Interpretation
Return profile: 2.1% annualized is consistent with a high-quality, duration-bearing bond mix over a period that included a severe rate selloff (2022) and a sharp rise in front-end yields.
Risk profile: 4.1% vol is moderate for fixed income. The -15% max drawdown indicates meaningful rate beta—expected given the 27% AGG + 23% multisector sleeves, plus IG corporates and global hedged bonds. The drawdown is consistent with 2022’s parallel-ish bear-steepener and spread widening.
Credit vs. rates: Credit sleeves (HYG 5%, BKLN 5%, LQD 7%, part of BOND/TOTL) add income but introduce cyclical downside if growth softens; rate duration dominates tail risk when yields gap higher.
Liquidity & implementation: ETF set is liquid, diversified, and operationally simple—appropriate for an online portfolio showcase.

Macro context & what it implies
Tariffs / cost-push: Risk of stickier inflation and a “higher-for-longer” rates path increases the chance of further curve repricing; duration should be budgeted carefully.
Late-cycle dynamics: Growth wobble + tighter financial conditions argues for credit discipline (HY/BKLN exposure sized to income benefit vs. drawdown risk).
Global diversification: BNDX hedged helps, but global duration still adds to rate beta; hedged exposure limits FX noise.

Actionable recommendations

A. Duration management (primary lever)
If “higher-for-longer” is base case:
Trim 3-5% from longer-duration sleeves (AGG/LQD/BNDX) to Short-Term (SHY/ICSH) or Unconstrained (TOTL) to reduce portfolio DV01 and drawdown sensitivity.
Consider barbelled duration: keep ultrashort + a measured 10-30y Treasury sleeve for convexity if a growth shock hits.
If recession risk rises (leading data roll-over):
Rotate +5% into duration via Treasuries/TIPS and reduce HY/BKLN 3-5%—benefits from flight-to-quality and curve bull-steepening.

B. Inflation hedging
Add 2–4% to TIPS (either by allocating within TOTL/BOND if they hold TIPS, or a dedicated TIP sleeve) as insurance against tariff-driven breakeven firming.

C. Credit discipline
Keep HY + Loans at ~10% cap unless spreads compensate for default cycle risk. Use HY primarily for carry; avoid it as a beta substitute.
If spreads tighten below long-run medians while growth softens, rebalance to IG/Treasuries.

D. Process upgrades for the portfolio site
Add a scenario panel (±100 bps parallel, bear/bull steepener, +150 bps HY spreads) and show ΔP/P using sleeve durations and spread durations.
Track rolling 12-month vol, max DD, and yield-to-worst of sleeves to explain the carry/risk trade-off.
Show a credit vs. rates contribution chart (e.g., factor model using rate level/slope + HY–IG factor).

Risk guardrails (proposed):
Volatility budget: 3.5–4.5% (realized, 1-yr).
Max DD budget: <10% through cycle (use short-term/unconstrained sleeves and TIPS to pull this down).
Credit risk cap: HY + Loans ≤ 12%; BBB share within IG monitored if you later add more granular sleeves.
Rebalance rule: Semi-annual or 2% band per sleeve, whichever first.

What to watch:
Breakevens & wage prints: persistent >2.5% y/y breakevens → keep TIPS tilt and shorter duration.

Labor & ISM: deterioration + easing inflation → lengthen duration, cut HY/BKLN.

Term premium / 10-2 slope: steepening with weak growth = own duration; bear steepening with sticky inflation = reduce DV01.
