'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

amount = int(input("what is the amount to invest? "))

interest = int(input("What is the interest rate (in percent)? "))

years = int(input("how many years will you invest? "))

future_value = (amount * interest/100 * years) + amount

print(f'In {years} years, your initial principal of ${amount} will be worth ${future_value}')
