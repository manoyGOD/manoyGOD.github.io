def load_currency_rates(filename):
    currency_rates = {}
    with open(filename, mode="r") as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip header
            code, name, rate = line.strip().split(',')
            currency_rates[code] = float(rate)
    return currency_rates

def convert_currency(amount, currency, rates):
    if currency in rates:
        return amount * rates[currency]
    else:
        return None

# Load exchange rates
rates = load_currency_rates('D:/Github/manoyGOD.github.io/ACT4B/currency.csv')

# Get user input
dollar_amount = float(input("How much dollar do you have? "))
currency_choice = input("What currency you want to have? ").upper()

# Convert currency
converted_amount = convert_currency(dollar_amount, currency_choice, rates)

# Display result
print(f"\nDollar: {dollar_amount} USD")
if converted_amount:
    print(f"{currency_choice}: {converted_amount}")
else:
    print("Currency not found.")
