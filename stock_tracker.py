# Stock Portfolio Tracker

# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 200,
    "MSFT": 420
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock_name = input(
        "\nEnter stock name (AAPL/TSLA/GOOGL/AMZN/MSFT): "
    ).strip().upper()

    if stock_name not in stock_prices:
        print("Invalid stock name! Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

    except ValueError:
        print("Please enter a valid whole number!")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    print("\nStock Name:", stock_name)
    print("Stock Price: $", price)
    print("Quantity:", quantity)
    print("Investment Value: $", investment)

    choice = input(
        "\nDo you want to add another stock? (yes/no): "
    ).strip().lower()

    if choice != "yes":
        break

print("\n===== Portfolio Summary =====")
print("Total Investment Value: $", total_investment)

# Save results to a text file
try:
    with open("portfolio.txt", "w", encoding="utf-8") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("-----------------------\n")
        file.write(f"Total Investment Value: ${total_investment}\n")

    print("Portfolio saved successfully to portfolio.txt")

except OSError as error:
    print("Error saving portfolio:", error)
