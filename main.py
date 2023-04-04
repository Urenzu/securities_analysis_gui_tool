from equities_ratios import calc_stock_pe_ratio, calc_stock_pb_ratio
from equities_discounts import calc_stock_dcf, calc_stock_ddm, calc_stock_discount_rate
from equities_valuations import calc_stock_capm, calc_stock_ev_ebitda

from fixed_income_analysis import calc_bond_price,  calc_bond_yield, calc_modified_duration, calc_yield_to_maturity

# Main function to run the program
def main():
    while True:
        print("What type of security do you want to evaluate?")
        print("1. Equities")
        print("2. Fixed Income")
        print("3. Quit")
        security_choice = input("Enter your choice (1-3): ")

        if security_choice == '1':
            # Equities valuation formula calculations
            while True:
                print("Choose a valuation metric to calculate:")
                print("1. P/E ratio")
                print("2. P/B ratio")
                print("3. Dividend discount model")
                print("4. Discounted cash flow")
                print("5. Capital asset pricing model")
                print("6. EV/EBITDA ratio")
                print("7. Quit")
                choice = input("Enter your choice (1-7): ")

                if choice == '1':
                    pe_ratio = calc_stock_pe_ratio()
                    print(f"P/E ratio: {pe_ratio}")
                elif choice == '2':
                    pb_ratio = calc_stock_pb_ratio()
                    print(f"P/B ratio: {pb_ratio}")
                elif choice == '3':
                    ddm = calc_stock_ddm()
                    print(f"DDM: {ddm}")
                elif choice == '4':
                    dcf = calc_stock_dcf()
                    print(f"DCF: {dcf}")
                elif choice == '5':
                    capm = calc_stock_capm()
                    print(f"CAPM: {capm}")
                elif choice == '6':
                    ev_ebitda = calc_stock_ev_ebitda()
                    print(f"EV/EBITDA ratio: {ev_ebitda}")
                elif choice == '7':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
        
        elif security_choice == '2':
            # Fixed Income valuation formula calculations
            while True:
                print("Choose a valuation metric to calculate:")
                print("1. Bond yield")
                print("2. Modified duration")
                print("3. Bond price")
                print("4. Yield to maturity")
                print("5. Quit")
                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    bond_yield = calc_bond_yield()
                    print(f"Bond yield: {bond_yield}")
                elif choice == '2':
                    mod_duration = calc_modified_duration()
                    print(f"Modified duration: {mod_duration}")
                elif choice == '3':
                    bond_price = calc_bond_price()
                    print(f"Bond price: {bond_price}")
                elif choice == '4':
                    ytm = calc_yield_to_maturity()
                    print(f"Yield to maturity: {ytm}")
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

        elif security_choice == '3':
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()