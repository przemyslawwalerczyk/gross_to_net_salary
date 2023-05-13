def calculate_social_contribution(amount):
  if amount < 200:
    return 0
  elif amount >= 200 and amount < 1000:
    return 100
  else:
    return 200

def calculate_tax(amount):
  if amount <= 3000:
    return (amount - calculate_social_contribution(amount)) * 0.1
  else:
    return 300 + (amount - calculate_social_contribution(amount) - 3000) * 0.2

def convert_gross_to_net(salary):
  return salary - calculate_social_contribution(salary) - calculate_tax(salary)

  
salary = float(input("What is your gross salary?: "))
after_social = salary - calculate_social_contribution(salary)
after_tax = after_social - calculate_tax(salary)

print("Your salary gross:", salary)  
print("Salary after social contribution:", after_social)
print("Net salary after tax: ", after_tax)
  
  
  
  
  
  
