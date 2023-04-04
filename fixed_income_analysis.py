# Calculate bond yield
def calc_bond_yield(face_value, coupon_rate, current_price, years_to_maturity):
    bond_yield = (coupon_rate + ((face_value - current_price) / years_to_maturity)) / ((face_value + current_price) / 2)
    return bond_yield

# Calculate modified duration
def calc_modified_duration(face_value, coupon_rate, current_price, years_to_maturity, yield_change):
    modified_duration = (-1 * (years_to_maturity * (face_value * coupon_rate / ((1 + (yield_change / 2)) ** 2) + (face_value / (1 + (yield_change / 2)) ** years_to_maturity))) / current_price) / (yield_change / 200)
    return modified_duration

# Calculate bond price
def calc_bond_price(face_value, coupon_rate, years_to_maturity, required_rate_of_return):
    bond_price = (coupon_rate * face_value / required_rate_of_return * (1 - (1 + required_rate_of_return) ** -years_to_maturity)) + (face_value / (1 + required_rate_of_return) ** years_to_maturity)
    return bond_price

# Calculate yield to maturity
def calc_yield_to_maturity(face_value, coupon_rate, current_price, years_to_maturity):
    # Using the secant method to solve for YTM
    def secant_method(f, x0, x1, tol):
        while abs(x1 - x0) > tol:
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
            x0 = x1
            x1 = x2
        return x1
    # Function to calculate the present value of bond cash flows
    def present_value(c, r, n, fv):
        pv = 0
        n = int(n)  # Convert years_to_maturity to an integer
        for i in range(1, n + 1):
            pv += c / ((1 + r) ** i)
        pv += fv / ((1 + r) ** n)
        return pv
    # Define the function to be solved
    def ytm_func(y):
        return present_value(coupon_rate * face_value, y, years_to_maturity, face_value) - current_price
    ytm = secant_method(ytm_func, 0.05, 0.1, 0.0001)
    return ytm