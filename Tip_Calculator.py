#  DAY 2 








# DAYS LEFT 


# age = input()
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# years = 90

# years_left = years - int(age) c

# # one year has 52 weeks 
# weeks_in_a_year = 52
# week_left = years_left*weeks_in_a_year
# print(f"You have {week_left} weeks left.")




print("------------------------------------------------------------------------------")
print("Welcome to the tip calculator!   ")
bill = float(input("What was the total bill? £"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print("------------------------------------------------------------------------------")
print(f"Each person should pay £{final_amount}")
print("------------------------------------------------------------------------------")
