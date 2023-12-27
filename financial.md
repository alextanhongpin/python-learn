Useful metrics for financial analysis

- Profitability metrics: Return on equity (ROE), return on assets (ROA), gross profit margin, operating profit margin, net profit margin, EBITDA margin
- Liquidity metrics: Current ratio, quick ratio, inventory turnover ratio, days sales outstanding (DSO), accounts payable turnover ratio, cash conversion cycle (CCC)
- Solvency metrics: Debt-to-equity ratio, debt-to-asset ratio, times interest earned ratio (TIE), interest coverage ratio
- Valuation metrics: Market-to-book ratio (M/B), price-to-earnings ratio (P/E), price-to-book ratio (P/B), price-to-sales ratio (P/S), dividend yield, payout ratio
- Cash flow metrics: Free cash flow to equity (FCFE), free cash flow to firm (FCFF), enterprise value (EV), debt-to-enterprise value ratio (D/EV), EBITDA multiple

These metrics can be used to assess a company's financial performance, identify potential risks and opportunities, and make informed investment decisions.

```python
# filename: financial_metrics.py
import pandas as pd

# Define the function to calculate the return on equity (ROE)
def calculate_roe(net_income, shareholders_equity):
    return net_income / shareholders_equity

# Define the function to calculate the return on assets (ROA)
def calculate_roa(net_income, total_assets):
    return net_income / total_assets

# Define the function to calculate the debt-to-equity ratio
def calculate_debt_to_equity(total_debt, shareholders_equity):
    return total_debt / shareholders_equity

# Define the function to calculate the current ratio
def calculate_current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities

# Define the function to calculate the quick ratio
def calculate_quick_ratio(quick_assets, current_liabilities):
    return quick_assets / current_liabilities

# Define the function to calculate the inventory turnover ratio
def calculate_inventory_turnover(cost_of_goods_sold, average_inventory):
    return cost_of_goods_sold / average_inventory

# Define the function to calculate the days sales outstanding (DSO)
def calculate_dso(average_accounts_receivable, revenue):
    return average_accounts_receivable / revenue * 365

# Define the function to calculate the accounts payable turnover ratio
def calculate_apt(cost_of_goods_sold, average_accounts_payable):
    return cost_of_goods_sold / average_accounts_payable

# Define the function to calculate the cash conversion cycle (CCC)
def calculate_ccc(inventory_turnover, dso, apt):
    return (1 / inventory_turnover) + (1 / dso) + (1 / apt)

# Define the function to calculate the gross profit margin
def calculate_gross_profit_margin(gross_profit, revenue):
    return gross_profit / revenue

# Define the function to calculate the operating profit margin
def calculate_operating_profit_margin(operating_income, revenue):
    return operating_income / revenue

# Define the function to calculate the net profit margin
def calculate_net_profit_margin(net_income, revenue):
    return net_income / revenue

# Define the function to calculate the EBITDA margin
def calculate_ebitda_margin(ebitda, revenue):
    return ebitda / revenue

# Define the function to calculate the interest coverage ratio
def calculate_interest_coverage_ratio(ebitda, interest_expense):
    return ebitda / interest_expense

# Define the function to calculate the debt-to-asset ratio
def calculate_debt_to_asset_ratio(total_debt, total_assets):
    return total_debt / total_assets

# Define the function to calculate the times interest earned ratio (TIE)
def calculate_tie(ebitda, interest_expense):
    return ebitda / interest_expense

# Define the function to calculate the return on invested capital (ROIC)
def calculate_roic(ebitda, taxes, depreciation_and_amortization, net_working_capital, gross_capital_expenditures):
    return (ebitda - taxes - depreciation_and_amortization) / (net_working_capital + gross_capital_expenditures)

# Define the function to calculate the economic value added (EVA)
def calculate_eva(net_operating_profit_after_tax, cost_of_capital, invested_capital):
    return net_operating_profit_after_tax - (cost_of_capital * invested_capital)

# Define the function to calculate the shareholder value added (SVA)
def calculate_sva(net_income, cost_of_equity, shareholders_equity):
    return net_income - (cost_of_equity * shareholders_equity)

# Define the function to calculate the market-to-book ratio (M/B)
def calculate_mb(market_capitalization, book_value_of_equity):
    return market_capitalization / book_value_of_equity

# Define the function to calculate the price-to-earnings ratio (P/E)
def calculate_pe(stock_price, earnings_per_share):
    return stock_price / earnings_per_share

# Define the function to calculate the price-to-book ratio (P/B)
def calculate_pb(stock_price, book_value_per_share):
    return stock_price / book_value_per_share

# Define the function to calculate the price-to-sales ratio (P/S)
def calculate_ps(stock_price, revenue_per_share):
    return stock_price / revenue_per_share

# Define the function to calculate the dividend yield
def calculate_dividend_yield(dividend_per_share, stock_price):
    return dividend_per_share / stock_price

# Define the function to calculate the payout ratio
def calculate_payout_ratio(dividends, net_income):
    return dividends / net_income

# Define the function to calculate the free cash flow to equity (FCFE)
def calculate_fcfe(net_income, depreciation_and_amortization, capital_expenditures, changes_in_working_capital):
    return net_income + depreciation_and_amortization - capital_expenditures - changes_in_working_capital

# Define the function to calculate the free cash flow to firm (FCFF)
def calculate_fcff(net_income, depreciation_and_amortization, capital_expenditures, changes_in_working_capital, interest_expense):
    return net_income + depreciation_and_amortization - capital_expenditures - changes_in_working_capital + interest_expense

# Define the function to calculate the enterprise value (EV)
def calculate_ev(market_capitalization, net_debt):
    return market_capitalization + net_debt

# Define the function to calculate the debt-to-enterprise value ratio (D/EV)
def calculate_d_to_ev(total_debt, enterprise_value):
    return total_debt / enterprise_value

# Define the function to calculate the EBITDA multiple
def calculate_ebitda_multiple(enterprise_value, ebitda):
    return enterprise_value / ebitda

# Define the function to calculate the price-to-sales ratio (P/S)
def calculate_ps(market_capitalization, revenue):
    return market_capitalization / revenue
```
