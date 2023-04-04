# Calculate capital asset pricing model
def calc_stock_capm(risk_free_rate, expected_market_return, beta):
    capm = risk_free_rate + beta * (expected_market_return - risk_free_rate)
    return capm

# Calculate stock ev to ebitda
def calc_stock_ev_ebitda(total_cash, total_debt, marketcap, ebitda):
    net_cash = total_cash - total_debt
    enterprise_value = marketcap + net_cash
    ev_ebitda = enterprise_value / ebitda
    return ev_ebitda