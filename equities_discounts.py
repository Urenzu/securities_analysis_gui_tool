# Calculate stock discount rate
def calc_stock_discount_rate(risk_free_rate, beta, expected_market_return, face_value, coupon_rate, market_price, years_to_maturity, tax_rate, market_value_of_debt, market_value_of_equity):
    cost_of_equity = risk_free_rate + beta * (expected_market_return - risk_free_rate)
    interest_payment = face_value * coupon_rate
    ytm = (interest_payment + (face_value - market_price) / years_to_maturity) / ((face_value + market_price) / 2)
    cost_of_debt = ytm * (1 - tax_rate)
    total_value = market_value_of_debt + market_value_of_equity
    weight_of_debt = market_value_of_debt / total_value
    weight_of_equity = market_value_of_equity / total_value
    discount_rate = cost_of_equity * weight_of_equity + cost_of_debt * weight_of_debt
    return discount_rate

# Calculate stock discounted cash flow
def calc_stock_dcf(expected_cash_flows, discount_rate):
    present_values = []
    for i, cash_flow in enumerate(expected_cash_flows):
        present_value = cash_flow / (1 + discount_rate) ** (i+1)
        present_values.append(present_value)
    dcf = sum(present_values)
    return dcf

# Calculate stock dividend discount model
def calc_stock_ddm(dividend_per_share, required_rate_of_return, dividend_growth_rate):
    if required_rate_of_return == dividend_growth_rate:
        return "Error: Required rate of return cannot be equal to the dividend growth rate."
    else:
        ddm = dividend_per_share / (required_rate_of_return - dividend_growth_rate)
        return ddm