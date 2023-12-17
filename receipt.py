import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        # Skip the header row
        next(csv_reader, None)
        for row in csv_reader:
            # Ensure the row has the expected number of elements
            if len(row) == 3:
                key = row[key_column_index]
                # Use the product number as the key, and the row as the associated list.
                compound_dict[key] = [key] + row[1:]  # Include the product number in the value list
    return compound_dict

def main():
    # Call the read_dictionary function and store the compound dictionary in a variable named products_dict.
    products_dict = read_dictionary('products.csv', 0)

    # Print the products_dict.
    print("All Products")
    print(products_dict)

    # Open the request.csv file for reading.
    with open('request.csv', 'r') as request_file:
        # Skip the first line of the requestx.csv file because it contains column headings.
        next(request_file)

        # Use a loop that reads and processes each row from the request.csv file.
        print("\nRequested Items")
        csv_reader = csv.reader(request_file)
        for row in csv_reader:
            # Use the requested product number to find the corresponding item in the products_dict.
            product_number = row[0]
            product_details = products_dict.get(product_number)

            if product_details:
                # Print the product name, requested quantity, and product price.
                product_name = product_details[1]
                quantity = int(row[1])
                price = float(product_details[2])
                total_price = quantity * price
                print(f"{product_name}: {quantity} @ {price:.2f} (Total: {total_price:.2f})")

if __name__ == "__main__":
    # Add a call to the main function.
    main()
