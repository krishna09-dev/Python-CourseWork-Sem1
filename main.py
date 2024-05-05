from operation import LandOperation

# Function to get current date and time
def get_current_date_time():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to display the rental system menu
def display_menu():
    border_top = "╔" + "═" * 88 + "╗"
    border_middle = "║" + " " * 88 + "║"
    # Printing the top border
    print(border_top)
    # Printing the middle border
    print(border_middle)
    # Printing the centered title lines
    title1 = "Land Rental System"
    title2 = "TechnoPropertyNepal Rental"
    print("║" + " " * ((88 - len(title1)) // 2) + title1 + " " * ((88 - len(title1)) // 2) + "║")
    print("║" + " " * ((88 - len(title2)) // 2) + title2 + " " * ((88 - len(title2)) // 2) + "║")
    # Printing the middle border
    print(border_middle)
    # Printing the centered location and date/time lines
    location = "Kathmandu, Nepal"
    date = "Date: " + get_current_date_time().split()[0]
    time = "Time: " + get_current_date_time().split()[1]
    print("║" + " " * ((88 - len(location)) // 2) + location + " " * ((88 - len(location)) // 2) + "║")
    print("║" + " " * ((88 - len(date)) // 2) + date + " " * ((88 - len(date)) // 2) + "║")
    print("║" + " " * ((88 - len(time)) // 2) + time + " " * ((88 - len(time)) // 2) + "║")
    print(border_middle)
    # Printing the middle border
    print("╚" + "═" * 88 + "╝")
    
    # Printing the menu borders
    print(border_top)
    print(border_middle)
    print("║" + " " * ((88 - len("RENTAL SYSTEM MENU")) // 2) + "RENTAL SYSTEM MENU" + " " * ((88 - len("RENTAL SYSTEM MENU")) // 2) + "║")
    print(border_middle)
    print("╠" + "═" * 88 + "╣")
    print(border_middle)
    print("║" + " " * ((88 - len("1. Display Land")) // 2) + "1. Display Land" + " " * ((90 - len("1. Display Land")) // 2) + "║")
    print("║" + " " * ((88 - len("2. Rent Land")) // 2) + "2. Rent Land" + " " * ((88 - len("2. Rent Land")) // 2) + "║")
    print("║" + " " * ((88 - len("3. Return Land")) // 2) + "3. Return Land" + " " * ((88 - len("3. Return Land")) // 2) + "║")
    print("║" + " " * ((88 - len("4. Exit")) // 2) + "4. Exit" + " " * ((90 - len("4. Exit")) // 2) + "║")
    print(border_middle)
    print("╚" + "═" * 88 + "╝")


def main():
    display_menu()
    land_operation = LandOperation()
    while True:
        
        choice = input("\nEnter your choice: ")
        if choice == "1":
            land_operation.display_land()
        elif choice == "2":
            land_operation.rent_land()
        elif choice == "3":
            lands_to_return = int(input("Enter the number of lands to return: "))
            land_operation.return_lands(lands_to_return)
        elif choice == "4":
            print("\nThank you for using the Land Rental System.")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")

# Call the main function
main()
