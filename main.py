from operation import LandOperation

# Function to get current date and time
def get_current_date_time():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to display the rental system menu
def display_menu():
    border_top_bottom = "+" + "-" * 88 + "+"
    border_middle = "|" + " " * 88 + "|"
    print("\033[1;36m" + border_top_bottom)
    print("║{: ^88}║".format("Land Rental System"))
    print(border_middle)
    print("║{: ^88}║".format("Kathmandu, Nepal"))
    print("║{: ^88}║".format("Date: " + get_current_date_time().split()[0]))
    print("║{: ^88}║".format("Time: " + get_current_date_time().split()[1]))
    print(border_top_bottom + "\033[0m")
    print("\033[1;34m" + "+" + "-" * 88 + "+")
    print("║{: ^88}║".format("RENTAL SYSTEM MENU"))
    print("+" + "-" * 88 + "+")
    print("║{: ^88}║".format("1. Display Land"))
    print("║{: ^88}║".format("2. Rent Land"))
    print("║{: ^88}║".format("3. Return Land"))
    print("║{: ^88}║".format("4. Exit"))
    print("+" + "-" * 88 + "+" + "\033[0m")

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
            land_operation.return_land()
        elif choice == "4":
            print("\nThank you for using the Land Rental System.")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
