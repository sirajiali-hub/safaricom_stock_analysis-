# Safaricom (SCOM) Equity Analysis: Risk, Return & Portfolio Analytics

A quantitative equity analysis of Safaricom PLC — the most liquid stock on the Nairobi Securities Exchange — from the perspective of an investment analyst assessing portfolio inclusion.

---

## Business Context

Safaricom PLC dominates the NSE by market capitalization and daily trading volume. Any Kenya-focused equity portfolio must have a view on SCOM. This analysis provides the quantitative foundation for that view, covering return profiling, downside risk measurement, volatility regimes, and technical price structure.

## Key Findings

| Metric | Value |
|--------|-------|
| Period | March 2024 – March 2026 |
| Total Return | 6.3% (annualized ~3.0%) |
| Annualized Volatility | 21.7% |
| Sharpe Ratio | -0.32 (underperforms risk-free T-bills at ~10%) |
| Maximum Drawdown | -22.7% |
| 1-Day VaR (95%, Historical) | -2.05% (KES 205K per KES 10M position) |

**Bottom line:** SCOM has not compensated investors for the equity risk taken. An investor holding 91-day T-bills would have earned more with zero downside. However, SCOM remains a core portfolio holding due to liquidity, market weight, and M-Pesa/fintech exposure.

## Analysis Sections

The notebook covers six areas an investment analyst would evaluate:

1. **Return Analysis** — total, annualized, and risk-adjusted returns with Sharpe ratio calculation against Kenya's risk-free rate (91-day T-bill)
2. **Return Distribution** — normality testing (Jarque-Bera) to validate VaR model assumptions; fat tails mean parametric VaR underestimates risk
3. **Volatility Analysis** — rolling 20-day and 60-day annualized volatility with regime identification showing volatility clustering
4. **Value at Risk (VaR)** — Historical VaR, Parametric VaR, and Conditional VaR (Expected Shortfall) at 95% and 99% confidence levels, with KES impact for a KES 10M position
5. **Technical Analysis** — SMA (20/50/200), Bollinger Bands, RSI with current positioning assessment
6. **Drawdown Analysis** — peak-to-trough measurement and recovery analysis

## Project Structure

```
safaricom-equity-analysis/
│
├── safaricom_equity_analysis.ipynb     # Main analysis notebook
├── safaricom_stock_data.csv            # Daily OHLCV data (523 trading days)
├── README.md
├── requirements.txt
├── .gitignore
│
└── outputs/                            # Generated charts
    ├── 01_price_and_returns.png
    ├── 02_return_distribution.png
    ├── 03_quarterly_returns.png
    ├── 04_volatility_analysis.png
    ├── 05_var_analysis.png
    ├── 06_technical_analysis.png
    ├── 07_drawdown_analysis.png
    └── 08_volume_analysis.png
```

## Dataset

523 trading days of Safaricom PLC (SCOM) daily data from the Nairobi Securities Exchange.

| Field | Description |
|-------|-------------|
| Date | Trading date |
| Open, High, Low, Close | Daily OHLC prices (KES) |
| Volume | Shares traded |

Price range: KES 23.34 – KES 36.24. Average daily volume: ~9.1M shares.

## How to Run

```bash
git clone https://github.com/sirajiali-hub/safaricom_stock_analysis-.git
cd safaricom-stock-analysis

pip install -r requirements.txt

jupyter notebook safaricom_equity_analysis.ipynb
```

## Limitations

- No benchmark comparison against NSE 20/NSE 25 index to separate alpha from market beta
- Purely quantitative — no fundamental analysis (P/E, dividend yield, DCF)
- Single-asset analysis without portfolio correlation context
- Timestamp format suggests simulated data; production analysis would use verified NSE data feeds

## Future Enhancements

- GARCH(1,1) volatility modeling for dynamic VaR
- Multi-asset portfolio optimization with other NSE blue chips
- Event study around earnings announcements and M-Pesa policy changes
- Monte Carlo simulation for scenario-based portfolio planning

## Tools

Python, pandas, NumPy, SciPy, matplotlib, seaborn

---


