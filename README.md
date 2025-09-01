# 📊 Fixed-Income Risk Portfolio

A collection of projects demonstrating knowledge and skills in fixed income, credit risk, and portfolio analysis.  


---

## 🚀 Projects

### 1. Factor Model & Risk Attribution (IG Credit) 
Developed a multi-factor risk model for U.S. investment-grade (IG) corporate bond portfolios:
- Ran OLS regressions with robust (HC3) standard errors of IG excess returns on key market factors (equity index, HY        credit beta, oil prices, and Treasury rate shifts).
- Conducted variance decomposition to identify the primary drivers of portfolio risk, quantifying factor contributions      vs. idiosyncratic risk.
- Produced attribution charts to highlight which macro/market exposures explain IG credit risk in different market          regimes.
  
### 2. Scenario & Stress Testing
Built a scenario and stress testing framework for a diversified fixed-income portfolio:
- Modeled parallel rate shifts, recession scenarios, higher-for-longer, and risk-off environments to test portfolio         resilience.
- Measured duration and spread duration impacts under shocks to interest rates and credit spreads.
- Extended analysis with historical Value-at-Risk (VaR) and Expected Shortfall to capture tail risk exposures.
- Produced stress dashboards to visualize potential mark-to-market losses across scenarios.
  
### 3. Performance Attribution (High Yield)
Performed performance attribution analysis on high-yield credit strategies:
- Applied Brinson-style allocation and selection decomposition to compare active positioning vs. benchmark.
- Quantified alpha sources by separating sector allocation effects from security selection skill.
- Generated attribution reports showing how much outperformance derived from top-down vs. bottom-up drivers.

### 4. Fixed-Income (FI) Model Portfolio 
- Prices from Yahoo Finance; daily total-return proxies via adjusted close.
- Portfolio return = ∑(sleeve return × weight), rebalanced implicitly by weights.
- Summary metrics: annualized return/volatility, Sharpe (rf=0 as implemented), and max drawdown.
---

## 🛠️ Tech Stack
- **Python:** pandas, statsmodels, numpy, matplotlib  
- **R:** quantmod, PerformanceAnalytics, tidyverse  
- **Data:** Yahoo Finance (ETF proxies), FRED  

---

## 📂 Structure
fixed-income-risk-portfolio/
├─ python/ # Jupyter notebooks + source code
├─ r/ # R scripts + renv
├─ docs/ # memo templates for credit/risk writeups
├─ data/ # placeholder for downloaded data

## ✍️ Author
Katherine Cohen  
🎓 FRM Candidate | 📈 Fixed Income & Risk Management





