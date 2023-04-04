import tkinter as tk
import customtkinter as ctk
from tkinter import Toplevel, Entry, Label, Button
from tkinter import simpledialog

from equities_ratios import calc_stock_pe_ratio, calc_stock_pb_ratio
from equities_discounts import calc_stock_dcf, calc_stock_ddm, calc_stock_discount_rate
from equities_valuations import calc_stock_capm, calc_stock_ev_ebitda

from fixed_income_analysis import calc_bond_price, calc_bond_yield, calc_modified_duration, calc_yield_to_maturity

class FinanceApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Securities Analysis Tool")
        self.geometry("400x400")

        self.main_menu()

    def main_menu(self):
        self.clear_frame()

        security_label = tk.Label(self, text="What type of security do you want to evaluate?")
        security_label.pack(pady=10)

        equities_button = ctk.CTkButton(self, text="Equities", command=self.equities_menu)
        equities_button.pack(pady=5)

        fixed_income_button = ctk.CTkButton(self, text="Fixed Income", command=self.fixed_income_menu)
        fixed_income_button.pack(pady=5)

        quit_button = ctk.CTkButton(self, text="Quit", command=self.destroy)  # Change this line
        quit_button.pack(pady=5)

    def equities_menu(self):
        self.clear_frame()

        equities_label = tk.Label(self, text="Choose a valuation metric to calculate:")
        equities_label.pack(pady=10)

        pe_button = ctk.CTkButton(self, text="P/E ratio", command=lambda: self.show_result("P/E ratio", self.calc_stock_pe_ratio_gui()))
        pe_button.pack(pady=5)

        pb_button = ctk.CTkButton(self, text="P/B ratio", command=lambda: self.show_result("P/B ratio", self.calc_stock_pb_ratio_gui()))
        pb_button.pack(pady=5)

        dcf_button = ctk.CTkButton(self, text="Discounted cash flow", command=lambda: self.show_result("DCF", self.calc_stock_dcf_gui()))
        dcf_button.pack(pady=5)

        ddm_button = ctk.CTkButton(self, text="Dividend discount model", command=lambda: self.show_result("DDM", self.calc_stock_ddm_gui()))
        ddm_button.pack(pady=5)

        capm_button = ctk.CTkButton(self, text="Capital asset pricing model", command=lambda: self.show_result("CAPM", self.calc_stock_capm_gui()))
        capm_button.pack(pady=5)

        ev_ebitda_button = ctk.CTkButton(self, text="EV/EBITDA ratio", command=lambda: self.show_result("EV/EBITDA ratio", self.calc_stock_ev_ebitda_gui()))
        ev_ebitda_button.pack(pady=5)

        back_button = ctk.CTkButton(self, text="Back", command=self.main_menu)
        back_button.pack(pady=5)

    def fixed_income_menu(self):
        self.clear_frame()

        fixed_income_label = tk.Label(self, text="Choose a valuation metric to calculate:")
        fixed_income_label.pack(pady=10)

        bond_yield_button = ctk.CTkButton(self, text="Bond yield", command=lambda: self.show_result("Bond Yield", self.calc_bond_yield_gui()))
        bond_yield_button.pack(pady=5)

        modified_duration_button = ctk.CTkButton(self, text="Modified duration", command=lambda: self.show_result("Modified Duration", self.calc_modified_duration_gui()))
        modified_duration_button.pack(pady=5)

        bond_price_button = ctk.CTkButton(self, text="Bond price", command=lambda: self.show_result("Bond Price", self.calc_bond_price_gui()))
        bond_price_button.pack(pady=5)

        yield_to_maturity_button = ctk.CTkButton(self, text="Yield to maturity", command=lambda: self.show_result("Yield to Maturity", self.calc_yield_to_maturity_gui()))
        yield_to_maturity_button.pack(pady=5)

        back_button = ctk.CTkButton(self, text="Back", command=self.main_menu)
        back_button.pack(pady=5)
    
    def show_result(self, label, result):
        self.clear_frame()

        result_label = tk.Label(self, text=f"{label}: {result}")
        result_label.pack(pady=10)

        back_button = ctk.CTkButton(self, text="Back", command=self.main_menu)
        back_button.pack(pady=5)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def get_float_input(self, title, prompt):
        input_dialog = Toplevel(self)
        input_dialog.title(title)

        label = Label(input_dialog, text=prompt)
        label.pack()

        entry_var = tk.StringVar()
        entry = Entry(input_dialog, textvariable=entry_var)
        entry.pack()

        submit_button = Button(input_dialog, text="Submit", command=input_dialog.destroy)
        submit_button.pack()

        input_dialog.grab_set()
        input_dialog.wait_window()

        entered_value = float(entry_var.get())

        return entered_value

    def calc_stock_pe_ratio_gui(self):
        stock_price = self.get_float_input("Stock Price", "Enter the stock price: ")
        eps = self.get_float_input("Earnings per Share", "Enter the earnings per share: ")
        return calc_stock_pe_ratio(stock_price, eps)

    def calc_stock_pb_ratio_gui(self):
        stock_price = self.get_float_input("Stock Price", "Enter the stock price: ")
        companies_total_equity = self.get_float_input("Total Equity", "Enter the companies total equity: ")
        companies_shares_outstanding = self.get_float_input("Shares Outstanding", "Enter the companies shares outstanding: ")
        return calc_stock_pb_ratio(stock_price, companies_total_equity, companies_shares_outstanding)
    
    def calc_stock_discount_rate_gui(self):
        risk_free_rate = self.get_float_input("Risk-Free Rate", "Enter the risk-free rate: ")
        beta = self.get_float_input("Beta", "Enter the beta: ")
        expected_market_return = self.get_float_input("Expected Market Return", "Enter the expected market return: ")
        face_value = self.get_float_input("Face Value", "Enter the face value of the bond: ")
        coupon_rate = self.get_float_input("Coupon Rate", "Enter the coupon rate: ")
        market_price = self.get_float_input("Market Price", "Enter the market price of the bond: ")
        years_to_maturity = self.get_float_input("Years to Maturity", "Enter the years to maturity of the bond: ")
        tax_rate = self.get_float_input("Tax Rate", "Enter the tax rate: ")
        market_value_of_debt = self.get_float_input("Market Value of Debt", "Enter the market value of debt: ")
        market_value_of_equity = self.get_float_input("Market Value of Equity", "Enter the market value of equity: ")
        return calc_stock_discount_rate(risk_free_rate, beta, expected_market_return, face_value, coupon_rate, market_price, years_to_maturity, tax_rate, market_value_of_debt, market_value_of_equity)

    def calc_stock_dcf_gui(self):
        cash_flows = simpledialog.askstring("Expected Cash Flows", "Enter the expected cash flows (separated by commas): ")
        expected_cash_flows = [float(x.strip()) for x in cash_flows.split(',')]
        discount_rate = self.calc_stock_discount_rate_gui()
        return calc_stock_dcf(expected_cash_flows, discount_rate)
    
    def calc_stock_ddm_gui(self):
        dividend_per_share = self.get_float_input("Dividend per Share", "Enter the dividend per share: ")
        required_rate_of_return = self.get_float_input("Required Rate of Return", "Enter the required rate of return: ")
        dividend_growth_rate = self.get_float_input("Dividend Growth Rate", "Enter the dividend growth rate: ")
        return calc_stock_ddm(dividend_per_share, required_rate_of_return, dividend_growth_rate)
    
    def calc_stock_capm_gui(self):
        risk_free_rate = self.get_float_input("Risk-free Rate", "Enter the risk-free rate: ")
        expected_market_return = self.get_float_input("Expected Market Return", "Enter the expected market return: ")
        beta = self.get_float_input("Stock's Beta", "Enter the stock's beta: ")
        return calc_stock_capm(risk_free_rate, expected_market_return, beta)

    def calc_stock_ev_ebitda_gui(self):
        total_cash = self.get_float_input("Total Cash", "Total cash: ")
        total_debt = self.get_float_input("Total Debt", "Total debt: ")
        marketcap = self.get_float_input("Company Market Cap", "Company market cap: ")
        ebitda = self.get_float_input("EBITDA", "Enter the EBITDA: ")
        return calc_stock_ev_ebitda(total_cash, total_debt, marketcap, ebitda)
    
    def calc_bond_yield_gui(self):
        face_value = self.get_float_input("Face Value", "Enter the face value of the bond: ")
        coupon_rate = self.get_float_input("Coupon Rate", "Enter the coupon rate: ")
        current_price = self.get_float_input("Current Price", "Enter the current price of the bond: ")
        years_to_maturity = self.get_float_input("Years to Maturity", "Enter the years to maturity of the bond: ")
        return calc_bond_yield(face_value, coupon_rate, current_price, years_to_maturity)

    def calc_modified_duration_gui(self):
        face_value = self.get_float_input("Face Value", "Enter the face value of the bond: ")
        coupon_rate = self.get_float_input("Coupon Rate", "Enter the coupon rate: ")
        current_price = self.get_float_input("Current Price", "Enter the current price of the bond: ")
        years_to_maturity = self.get_float_input("Years to Maturity", "Enter the years to maturity of the bond: ")
        yield_change = self.get_float_input("Yield Change", "Enter the change in yield: ")
        return calc_modified_duration(face_value, coupon_rate, current_price, years_to_maturity, yield_change)

    def calc_bond_price_gui(self):
        face_value = self.get_float_input("Face Value", "Enter the face value of the bond: ")
        coupon_rate = self.get_float_input("Coupon Rate", "Enter the coupon rate: ")
        years_to_maturity = self.get_float_input("Years to Maturity", "Enter the years to maturity of the bond: ")
        required_rate_of_return = self.get_float_input("Required Rate of Return", "Enter the required rate of return: ")
        return calc_bond_price(face_value, coupon_rate, years_to_maturity, required_rate_of_return)
    
    def calc_yield_to_maturity_gui(self):
        face_value = self.get_float_input("Face Value", "Enter the face value of the bond: ")
        coupon_rate = self.get_float_input("Coupon Rate", "Enter the coupon rate: ")
        current_price = self.get_float_input("Current Price", "Enter the current price of the bond: ")
        years_to_maturity = self.get_float_input("Years to Maturity", "Enter the years to maturity of the bond: ")
        return calc_yield_to_maturity(face_value, coupon_rate, current_price, years_to_maturity)

if __name__ == "__main__":
    app = FinanceApp()
    app.mainloop()
