Source: [Stress Testing Engine](https://github.com/katcohen/fixed-income-risk-portfolio/blob/main/python/src/stress_engine.py)

# Fixed Income Scenario & Stress — Analyst Memo  

**Date:** August 25, 2025  
**Analyst:** Katherine Cohen  

## Executive Summary  
We evaluated portfolio sensitivity to rate and spread shocks using scenario analysis and stress testing.  
- **Scenarios tested:** Parallel +100 bps, Recession (+150 bps spreads / -50 bps rates), Higher-for-Longer (+50/+50), Risk-off (-75 bps rates / +200 bps spreads).  
- Results show **spread shocks** are the dominant risk driver.  
- Portfolio is particularly vulnerable under **Recession** and **Risk-off** cases.  

## Methodology  
- Portfolio: IG (LQD), HY (HYG), Treasuries (IEF), MBS (MBB).  
- Risk measures: Effective duration & spread duration.  
- Stress scenarios applied using:  
  \[
  \Delta P/P \approx -(D \cdot \Delta y + SD \cdot \Delta s)
  \]  
- Historical risk metrics: VaR (95%) and Expected Shortfall (95%) applied to return history.  

## Results  
| Scenario | ΔP/P (%) | Commentary |  
|----------|----------|------------|  
| Parallel +100 bps | {{X%}} | Moderate loss from rates. |  
| Recession | {{X%}} | Spreads widen sharply; HY underperforms. |  
| Higher-for-Longer | {{X%}} | Balanced hit from both rates & spreads. |  
| Risk-off | {{X%}} | Worst case: HY drag, IG spread widening. |  

Historical Risk:  
- **VaR (95%):** {{X%}}  
- **Expected Shortfall (95%):** {{X%}}  

## Interpretation  
- Spread shocks dominate losses, especially HY allocation.  
- Recession & Risk-off cases show asymmetric downside risk.  
- Rate-only scenarios are less impactful due to diversification.  

## Implications & Actions  
- Add credit hedges (CDX HY/IG).  
- Reduce HY exposure or shift to shorter-duration IG.  
- Rebalance toward Treasuries/MBS for downside protection.  
