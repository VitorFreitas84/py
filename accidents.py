import csv

YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    try:
        filename = input("Name of file that contains NHTSA data: ")
        with open(filename, "rt") as text_file:

            perc_reduc = get_float("Percent reduction of texting while driving [0, 100]: ", 0, 100)

            print()
            print(f"With a {perc_reduc}% reduction in using a cell",
                "phone while driving, approximately the",
                "following number of injuries and deaths",
                "would have been prevented in the USA.", sep="\n")
            print()
            print("Year, Injuries, Deaths")

            reader = csv.reader(text_file)
            next(reader)

            for row in reader:
                year = row[YEAR_COLUMN]

                try:
                    injur, fatal = estimate_reduction(row, PHONE_COLUMN, perc_reduc)
                    print(year, injur, fatal, sep=", ")

                except ZeroDivisionError as zero_div_err:
                    print(f"Error: {zero_div_err} in line {reader.line_num} of {filename}")

    except FileNotFoundError as not_found_err:
        print(f"{not_found_err}\nPlease choose a different file.")

    except ValueError as val_err:
        print(f"Error: {val_err}")

        if "float()" in str(val_err) and "not in range" in str(val_err):
            print("Error: Please enter a percentage between 0 and 100.")

    except (csv.Error, KeyError) as error:
        print(f"Error: {error} in line {reader.line_num} of {filename}")

    # Handle generic exceptions
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def estimate_reduction(row, behavior_key, perc_reduc):
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])

    if fatal_crashes == 0:
        raise ZeroDivisionError("Fatal Crashes column contains zero (0).")
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


def get_float(prompt, lower_bound, upper_bound):
    number = None
    while number is None:
        try:
            number = float(input(prompt))
            if number < lower_bound or number > upper_bound:
                print(f"Error: {number} is out of range. Please enter a number between {lower_bound} and {upper_bound}.")
                number = None
        except ValueError as val_err:
            print(f"Error: {val_err}")
    print()
    return number


if __name__ == "__main__":
    main()
