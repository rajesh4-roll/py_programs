"""
    File: leap_year.py
    --------------------------
    This tells the user about leap year or not
"""

def leap_year(x):
    if x%4 != 0:
        if x%100 != 0:
            if x%400 != 0:
                print("That's not a leap year.")
            else:
                print("That's a leap year.")
        else:
            print("That's a leap year.")
    else:
        print("That's a leap year.")

def main():
    leap_year(2021)
    leap_year(2024)
    leap_year(2028)
    leap_year(2032)

if __name__ == "__main__":
    main()