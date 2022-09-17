# program to calculate and display approximate number of minutes since the user's birthday
# assumes midnight for both dates, so is not current to the exact minute

from datetime import date       # for date operations
import re                       # for regular expressions
import sys                      # for sys.exit
import inflect                  # for converting numbers to words

def main():
    current_date = date.today()
    birth_date = input("Date of Birth: ")
    validate(birth_date)                      # ensure that date is in the right format
    convert(birth_date, current_date)         # call conversion function which also prints result


# validate that date is in YYYY-MM-DD format (exits otherwise); convert to ISO format

def validate(s):
    if match := re.search(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", s):
        return True
    else:
        sys.exit("Invalid format")

# converts user-entered time to ISO format; calculates amount of time between the two dates

def convert(s, t):
    converted_date = date.fromisoformat(s)          # puts birth_date (above) into ISO format so we can perform operations on it
    time_difference = t - converted_date
    time_difference_in_minutes = int(time_difference.total_seconds() / 60)
    p = inflect.engine()                            # required per inflect documentation
    output = p.number_to_words(time_difference_in_minutes, andword="")  # inflect method to convert numbers to words
    print(output.capitalize() + " minutes")


if __name__ == "__main__":
    main()
