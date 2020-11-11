def meal_vouchers(food_cost, voucher_value):
    if voucher_value > food_cost:
        print("Pay in cash. No return on vouchers.")
    else:
        num_vouchers = food_cost//voucher_value
        pay_up = food_cost % voucher_value

    text_out = f"You'll need {num_vouchers} food vouchers and you will also need {pay_up} in cash."
    print(text_out) #Is there a better way of using f string? Or do I really need to pass it as a variable?
meal_vouchers(500, 74)
