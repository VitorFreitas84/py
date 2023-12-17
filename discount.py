"""
Author: Vitor Hugo Santos de Freitas

02 Team Activity: Calling Functions
"""

# Import the datetime class from the datetime module
from datetime import datetime

# Get the current date and time
current_date_and_time = datetime.now()

# Get the day of the week as an integer (0 for Monday, 1 for Tuesday, etc.)
day_of_week = current_date_and_time.weekday()

subtotal = float(input("Please enter the subtotal: "))

# Check if today is Tuesday or Wednesday and subtotal is $50 or greater
if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
    discount = 0.1 * subtotal  # Calculate the discount amount
else:
    discount = 0

# Calculate the sales tax amount (6% of the subtotal)
sales_tax = 0.06 * subtotal

# Calculate the total amount due
total_due = subtotal - discount + sales_tax

# Display the results
if discount > 0:
    print(f"Discount amount: {discount:.2f}")
print(f"Sales tax amount: {sales_tax:.2f}")
print(f"Total: {total_due:.2f}")

