actual_cost = float(input("Enter the the Actual Product/Item price:"))
sale_amount = float(input("Enter the Sale Amount:"))

if (sale_amount < actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit gained!!!!")