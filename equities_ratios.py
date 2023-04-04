# Calculate price to equity ratio
def calc_stock_pe_ratio(stock_price, eps):
    pe_ratio = stock_price / eps
    return pe_ratio

# Calculate price to book ratio
def calc_stock_pb_ratio(stock_price, companies_total_equity, companies_shares_outstanding):
    book_value_per_share = companies_total_equity / companies_shares_outstanding
    pb_ratio = stock_price / book_value_per_share
    return pb_ratio