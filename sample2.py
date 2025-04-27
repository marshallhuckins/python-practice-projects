def calculate_future_value(monthly_investment, yearly_interest, years):
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        monthly_investment = float(input("Enter monthly investment:\t"))
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        years = int(input("Enter number of years:\t\t"))

        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
