print("How many calories do you consume in a day?")
breakfast_calories = int(input("Breakfast calories?: "))
lunch_calories = int(input("Lunch calories?: "))
snack_calories = int(input("Snack calories?: "))
dinner_calories = int(input("Dinner calories: "))
total_calories = breakfast_calories + lunch_calories + snack_calories + dinner_calories
print("Your total calories for today: ", total_calories)

