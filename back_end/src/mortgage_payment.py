

def calculate_mortgage_return(sale_price, rent):
    """
    Calculate the mortgage return for a property

    :param sale_price: the sale price of a property
    :param rent: The total rent gained from letting all out all of the rooms in the property
    :return: A dict conaining the mortgage repayment and total rent
    """
    interest_rate = 3.9
    months = 240
    loan_rate = 0.75

    sale_price = int(sale_price)
    rent = int(rent)

    loan = loan_rate * sale_price

    monthly_rate = interest_rate / 100 / 12
    mortgage_payment = (monthly_rate / (1 - (1 + monthly_rate) ** (-months))) * loan
    result = {"mortgage_payment": mortgage_payment, "rent": rent}
    return result


