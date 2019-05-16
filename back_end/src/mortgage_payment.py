

def calculate_mortgage(result, rents):
    interest_rate = 3.9
    months = 240
    loan_rate = 1.75

    if "beds" in result:
        beds = result["beds"]
        rent_income = int(rents[int(beds)])
        sale_price = int(result["sale_price"])
        loan = loan_rate * sale_price

        monthly_rate = interest_rate / 100 / 12
        mortgage_payment = (monthly_rate/(1-(1 + monthly_rate)**(-months))) * loan
        result = {"mortgage_payment": mortgage_payment, "rent_income": rent_income}
        return result


if __name__ == "__main__":
    rents = {2:"1100"}
    p = {"beds":"2", "sale_price":"130000"}
    a = calculate_mortgage(p, rents)
    print(a)
