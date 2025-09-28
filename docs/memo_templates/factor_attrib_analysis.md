Source: [Portfolio Factor Attribution Analysis](https://github.com/katcohen/fixed-income-risk-portfolio/blob/main/python/src/factor_attrib_cfa.py)

# IG Credit Portfolio Factor Attribution — Analyst Memo  

**Date:** August 25, 2025
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
