def Calculate_Profit_or_Loss(cost_price, selling_price):
    gain_or_loss = selling_price - cost_price

    if gain_or_loss > 0:
        result_type = "Profit"
    elif gain_or_loss < 0:
        result_type = "Loss"

    else:
        result_type = "No Profit No Loss"

    gain_percentage = (gain_or_loss / cost_price) * 100
    loss_percentage = (abs(gain_or_loss)) / cost_price * 100

    return{

        "Result Type" : result_type,
        "Gain or Loss" : gain_or_loss,
        "Gain Percentage" : gain_percentage,
        "Loss Percentage" : loss_percentage
    }

cost_price = float(input("Enter the cost Price :"))
selling_price = float(input("Enter the selling Price: "))

result = Calculate_Profit_or_Loss(cost_price, selling_price)

print("\n Result:")
print(f"{result['Result Type']}: {result['Gain or Loss']}")
print(f"Gain Percentage: {result['Gain Percentage']}%")
print(f"Loss Percentage: {result['Loss Percentage']}%")