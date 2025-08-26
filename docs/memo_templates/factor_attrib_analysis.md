# Fixed-Income Factor Attribution — Results Summary
_Date: 2025-08-26_

## Executive Summary
Regression of a diversified FI portfolio (30% IEF, 30% LQD, 20% HYG, 10% EMB, 10% TIP) on level, slope, credit, and inflation factors shows:

- **Credit factor dominates** (≈ 96% variance share).
- **Slope** is modest but statistically significant (beta ≈ -0.009).
- **Level** and **Inflation** factors explain very little variance.

## Key Findings
- Portfolio is most sensitive to **credit spread risk**.
- Slope exposure indicates vulnerability to **curve flatteners**.
- Rate level (10Y) and breakeven inflation add minimal explanatory power.

## Implications
- Portfolio is essentially a **credit beta trade**.
- Oversight recommendation: introduce **rate hedges** (Treasuries) or reduce HY/IG tilt to balance risk.
- Next step: monitor rolling betas to capture regime shifts.
# IG Credit Factor Attribution — Research Note
Date: 2025-08-26

## Executive Summary
- Portfolio attribution based on CFA-style fixed-income factor framework.
- OLS regression with HC3 robust errors applied to IG credit portfolio returns (2015–2025).
- Main finding: **Credit spread factor** explains ~96% of systematic variance.
- Other factors (level, slope, inflation) play minor roles.

## Method
- Portfolio: 30% Treasuries (IEF), 30% IG (LQD), 20% HY (HYG), 10% EM (EMB), 10% TIPS (TIP).
- Factors:
  - **Level**: Δ10Y UST yield (GS10)
  - **Slope**: Δ(10Y – 2Y)
  - **Credit**: HY – IG returns (HYG – LQD)
  - **Inflation**: Δ10Y breakeven inflation (T10YIE)
- Regression: OLS with HC3 robust SE.

## Results
- Credit beta: -0.243 (highly significant).
- Variance contribution: ~96% credit, ~2% slope, <2% others.
- R²: ~0.11, consistent with daily noise but significant credit exposure.

## Implications & Actions
- Portfolio risk overwhelmingly driven by credit spreads.
- Recommend monitoring credit spread volatility and stress-testing for widening scenarios.
- Consider hedges (CDX IG/HY index overlays) to manage tail risk.
