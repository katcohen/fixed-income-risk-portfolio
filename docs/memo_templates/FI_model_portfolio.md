Fixed-Income Model Portfolio — Analyst Memo

Analyst: Katherine Cohen

Objective:
Evaluate a diversified, advisor-style fixed-income model portfolio built from liquid ETFs and identify risk drivers and actionable improvements under current macro conditions (sticky inflation, “higher-for-longer” policy risk, tariff-related cost pressures, and late-cycle growth uncertainty).

Portfolio & Method — allocations / tickers (weights)

Core Intermediate (AGG, 27%), Multisector (BOND, 23%), Short-Term (SHY, 13%), IG Corporate (LQD, 7%), World Hedged (BNDX, 6%), Nontraditional/Unconstrained (TOTL, 7%), High Yield (HYG, 5%), Bank Loans (BKLN, 5%), Ultrashort (ICSH, 4%), Muni Intermediate (MUB, 3%).

Data/returns: Prices from Yahoo Finance; daily total-return proxies via adjusted close.
Portfolio return: ∑(allocation return × weight), with weights implying the rebalancing.
Summary metrics: annualized return/volatility, Sharpe (rf=0 as implemented), and max drawdown.

Results (2015–present):
Annualized return: 2.08% · Annualized volatility: 4.06% · Sharpe (rf=0): 0.51 · Max drawdown: –15.11%
Note: Sharpe uses rf=0. Using a positive realized cash yield would reduce the Sharpe; read 0.51 as an ex-cash indicator.

Interpretation

Return profile: ~2.1% is consistent with a high-quality, duration-bearing bond mix over a period that included the 2022 rate shock and a sharp rise in front-end yields.
Risk profile: 4.1% vol is moderate for fixed income. The –15% max drawdown reflects meaningful rate risk given AGG 27% + BOND 23%, plus IG corporates and global hedged bonds—consistent with 2022’s parallel-ish bear-steepener and spread widening.
Credit vs. rates: Credit allocations (HYG 5%, BKLN 5%, LQD 7%, and credit portions of BOND/TOTL) add income but bring cyclical downside if growth softens. Rate duration dominates tail risk when yields gap higher.
Liquidity & implementation: ETF set is liquid, diversified, and operationally appropriate for an online portfolio showcase.

Macro context & implications

Tariffs / cost-push: Sticky inflation risk → “higher-for-longer” path; budget duration carefully.

Late-cycle dynamics: Growth slowdown + tighter financial conditions → credit discipline (size HY/BKLN to income benefit vs. drawdown risk).

Global diversification: BNDX (hedged) reduces FX noise; global duration still adds rate beta.

Actionable recommendations

A. Duration management (primary lever)

Base case higher-for-longer: Trim 3–5% from longer-duration allocations (AGG/LQD/BNDX) to SHY/ICSH or TOTL to lower DV01 and drawdown sensitivity. Keep ultrashort plus a measured 10–30y Treasury allocation for convexity if a growth shock hits.

If recession risk rises: Add ~+5% duration via Treasuries/TIPS; cut HY/BKLN 3–5%—benefits from flight-to-quality and curve bull-steepening.

B. Inflation hedging
Add 2–4% TIPS (via TOTL/BOND if they hold TIPS, or a dedicated TIP allocation) as insurance against tariff-driven breakeven firming.

C. Credit discipline
Keep HY + Loans ≈ 10% cap unless spreads pay for default-cycle risk. Use HY for carry, not beta. If spreads richen below long-run medians while growth softens, rebalance to IG/Treasuries.

D. Portfolio-site process upgrades
Add a scenario panel (±100 bps parallel, bear/bull steepener, +150 bps HY spreads) and show ΔP/P using allocation durations and spread durations. Track rolling 12-mo vol, max DD, and yield-to-worst by allocation. Include a rates vs. credit contribution chart (e.g., factor model with rate level/slope + HY–IG).

Risk guardrails (proposed)

Volatility budget: 3.5–4.5% (realized, 1-yr).

Max DD budget: <10% through-cycle (use short-term/unconstrained allocations and TIPS to pull this down).

Credit cap: HY + Loans ≤ 12%; monitor BBB share within IG if you later add more granularity.

Rebalance rule: Semi-annual or 2% band per allocation, whichever comes first.

What to watch

Breakevens & wages: Persistent breakevens >2.5% y/y → keep TIPS tilt, stay shorter duration.

Labor & ISM: Deterioration + easing inflation → lengthen duration, cut HY/BKLN.

Term premium / 10–2 slope:

Steepening with weak growth → own duration.

Bear steepening with sticky inflation → reduce DV01.
