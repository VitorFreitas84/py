"""
Author: Vitor Hugo Santos de Freitas

02 Checkpoint: Calling Functions
"""
# Import the math module so that we can call the math.ceil function.
import math

# Get user input for the number of items and items per box
num_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# Calculate the number of boxes needed
num_boxes = math.ceil(num_items / items_per_box)

# Print the result
print(f"For {num_items} items, packing {items_per_box} items in each box, you will need {num_boxes} boxes.")
