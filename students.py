import csv

def read_dictionary(filename, key_column_index=None):
    """Read the contents of a CSV file into a dictionary or compound dictionary.

    Parameters:
        filename (str): The name of the CSV file to read.
        key_column_index (int): The index of the column to use as the keys in the dictionary.
                               If None, the I-Number will be used as the key.

    Returns:
        dict: A dictionary that contains the contents of the CSV file.
              If key_column_index is provided, it returns a compound dictionary.
    """
    student_dict = {}

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip the first line of text containing headings

            for row in reader:
                key = row[key_column_index] if key_column_index is not None else row[0]
                value = row[1] if key_column_index is not None else row[1:]

                student_dict[key] = value

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} was not found.")

    return student_dict

def main():
    # Assuming the students.csv file is in the same directory as this Python script
    filename = 'students.csv'
    
    # Reading the CSV file into a dictionary
    student_dict = read_dictionary(filename)

    # Get an I-Number from the user
    user_input = input("Enter an I-Number: ")
    
    # Remove dashes from the user input
    user_input = user_input.replace("-", "")

    # Validate the I-Number
    if not user_input.isdigit():
        print("Invalid I-Number: contains non-digit characters")
        return

    # Check for too few or too many digits
    if len(user_input) < 9:
        print("Invalid I-Number: too few digits")
    elif len(user_input) > 9:
        print("Invalid I-Number: too many digits")
    else:
        # Search for the I-Number in the dictionary
        if user_input in student_dict:
            print(f"Student Name: {student_dict[user_input]}")
        else:
            print("No such student")

if __name__ == "__main__":
    main()
