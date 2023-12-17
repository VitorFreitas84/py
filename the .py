import csv
from datetime import datetime

def read_csv(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [row for row in reader]
        return header, data
    except FileNotFoundError:
        print(f"Error: missing file\n[Errno 2] No such file or directory: '{file_name}'")
        exit()

def generate_receipt(products, requests):
    try:
        product_dict = {row[0]: row[1:] for row in products}
        total_items = 0
        subtotal = 0

        print("Inkom Emporium\n")

        for request in requests:
            prod_num, quantity = request
            prod_info = product_dict[prod_num]
            prod_name, price = prod_info[0], float(prod_info[1])
            
            print(f"{prod_name}: {quantity} @ {price:.2f}")
            total_items += int(quantity)
            subtotal += float(quantity) * price

        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total_due = subtotal + sales_tax

        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_due:.2f}\n")
        print("Thank you for shopping at the Inkom Emporium.")

        current_date_and_time = datetime.now()
        print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))

    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file\n'{e}'")


if __name__ == "__main__":
    products_header, products_data = read_csv("products.csv")
    requests_header, requests_data = read_csv("request.csv")

    generate_receipt(products_data, requests_data)
