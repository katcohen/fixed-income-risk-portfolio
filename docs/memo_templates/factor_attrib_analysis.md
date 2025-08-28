
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
  # IG Credit Portfolio Factor Attribution — Analyst Memo  

**Date:** {{insert date of analysis}}  
**Analyst:** Katherine Cohen  

## Executive Summary  
We ran a multi-factor regression of a diversified fixed-income portfolio (30% Treasuries, 30% IG Credit, 20% High Yield, 10% EM Debt, 10% TIPS) against systematic risk factors:  

- **Level:** Changes in 10Y U.S. Treasury yields (GS10).  
- **Slope:** Changes in curve slope (10Y–2Y).  
- **Credit:** HY – IG daily return spread differential.  
- **Inflation:** Changes in 10Y breakeven inflation (T10YIE).  

Results show the portfolio’s performance is overwhelmingly explained by credit spreads, with modest sensitivity to the curve slope, and minimal contribution from rate levels or breakeven inflation.  

## Methodology  
- OLS Regression with HC3 robust standard errors (daily data, 2015–present).  
- Dependent variable: Portfolio daily returns (ETF-weighted).  
- Independent variables: Level, slope, credit, inflation.  
- Variance attribution: Approximate share of explained variance = β² × Var(factor) / Σ(β² × Var).  

## Results  
**Regression Betas (robust):**  
- Level: -0.0033 (not statistically significant)  
- Slope: -0.0092 (significant, p < 0.05)  
- Credit: -0.2434 (highly significant, p < 0.001)  
- Inflation: +0.0038 (not significant)  

**Variance Contribution:**  
- Credit: ~96%  
- Slope: ~2%  
- Level: <1%  
- Inflation: <1%  

## Interpretation  
- Credit spread risk dominates portfolio returns (≈96% of variance explained). This reflects the large allocation to IG and HY credit sleeves.  
- Curve slope sensitivity is notable, suggesting positioning reacts to steepening/flattening moves — potentially via IG corporates and EM debt.  
- Rate level exposure is minimal, consistent with partial diversification via Treasuries and TIPS.  
- Inflation beta is weak, indicating TIPS allocation is too small to materially impact portfolio variance.  

## Implications & Actions  
- **Risk Oversight:** Portfolio is highly exposed to credit spread widening, which could severely impact returns in a risk-off environment.  
- **Portfolio Construction:** Consider reducing credit overweight or adding explicit hedges (CDX IG, HY protection).  
- **Strategic View:** Slope sensitivity suggests curve trades matter; monitor Fed policy outlook for steepening/flattening triggers.  
- **Next Steps:** Extend analysis with rolling betas to assess regime dependence (e.g., pre/post-COVID, high inflation era). 
