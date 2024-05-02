from write import InvoiceWriter
from read import LandReader
import datetime

class LandOperation:
    def __init__(self):
        self.land_reader = LandReader()  # Instantiate LandReader
        self.land_data = self.land_reader.load_land_data()  # Call load_land_data() on the instance

    def pad_to_length(self, text, length):
        padding = length - len(text)
        if padding % 2 == 0:
            left_padding = right_padding = padding // 2
        else:
            left_padding = padding // 2
            right_padding = left_padding + 1
        return " " * left_padding + text + " " * right_padding

    def display_land(self):
        border_top = "╔" + "═" * 15 + "╦" + "═" * 20 + "╦" + "═" * 15 + "╦" + "═" * 10 + "╦" + "═" * 10 + "╦" + "═" * 10 + "╦" + "═" * 10 + "╗"
        border_bottom = "═" + "═" * 15 + "╦" + "═" * 20 + "╦" + "═" * 15 + "╦" + "═" * 10 + "╦" + "═" * 10 + "╦" + "═" * 10 + "╦" + "═" * 10 + "═"
        border_middle = "╠" + "═" * 15 + "╬" + "═" * 20 + "╬" + "═" * 15 + "╬" + "═" * 10 + "╬" + "═" * 10 + "╬" + "═" * 10 + "╬" + "═" * 10 + "╣"
        header = "║" + self.pad_to_length("Kitta", 15) + "║" + self.pad_to_length("City/District", 20) + "║" + self.pad_to_length("Direction", 15) + "║" + self.pad_to_length("Area", 10) + "║" + self.pad_to_length("Price", 10) + "║" + self.pad_to_length("Status", 10) + "║"
        print(border_top)
        print(header)
        print(border_middle)

        for kitta, details in self.land_data.items():
            row = "║" + self.pad_to_length(str(kitta), 15) + "║" + self.pad_to_length(str(details['city']), 20) + "║" + self.pad_to_length(str(details['direction']), 15) + "║" + self.pad_to_length(str(details['area']), 10) + "║" + self.pad_to_length(str(details['price']), 10) + "║" + self.pad_to_length(str(details['status']), 10) + "║"
            print(row)

        print(border_bottom)



    def rent_land(self):
        while True:
            customer = input("Enter your name: ").replace(" ", "")  # Get user input and remove leading/trailing whitespace
            if customer:  # Check if the input is not empty
                break  # If input is valid, exit the loop
            else:
                print("Name cannot be empty. Please enter your name.")
    
        while True:
            try:
                lands_to_rent = int(input("How many lands do you want to rent? "))
                if lands_to_rent > 0:
                    break
                else:
                    print("Please enter a valid number of lands to rent (greater than 0).")
            except ValueError:
                print("Please enter a valid number.")
    
        rented_lands_info = []  # To store information about rented lands
    
        for _ in range(lands_to_rent):
            kitta = int(input("Enter the kitta number of land you want to rent: "))
            if kitta in self.land_data and self.land_data[kitta]["status"].lower() == "available":
                while True:
                    duration = int(input("Enter the duration of rent (in months) for land with kitta " + str(kitta) + ":"))
                    if duration > 0:
                        break
                    else:
                        print("Duration should be greater than 0. Please enter a valid duration.")
                rented_lands_info.append({
                    "kitta": kitta,
                    "city": self.land_data[kitta]["city"],
                    "direction": self.land_data[kitta]["direction"],
                    "area": self.land_data[kitta]["area"],
                    "price": self.land_data[kitta]["price"],
                    "duration": duration
                })
                # Update availability of the rented land to "Not Available"
                self.land_data[kitta]["status"] = "Not Available"
                print("Land rented successfully.")
            else:
                print("Land is not available for rent.")
    
        if rented_lands_info:
            # Generate a bill number
            bill_number = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            # Prepare transaction details for generating invoice
            transaction_details = {
                "bill_number": bill_number,
                "customer": customer,
                "lands": rented_lands_info,
                "total_amount": sum(land['price'] * land['duration'] for land in rented_lands_info)
            }
            # Generate invoice
            invoice_writer = InvoiceWriter()  # Instantiate InvoiceWriter
            invoice_writer.generate_invoice(transaction_details)
            invoice_writer.print_invoice_details(transaction_details)
        else:
            print("No land rented, so no invoice generated.")
        
    

    def return_lands(self, lands_to_return):
        invoice_writer = InvoiceWriter()  # Instantiate InvoiceWriter
        while True:
            customer = input("Enter your name: ").replace(" ", "")  # Get user input and remove leading/trailing whitespace
            if customer:  # Check if the input is not empty
                break  # If input is valid, exit the loop
            else:
                print("Name cannot be empty. Please enter your name.")

        total_amount_fine = 0
        lands = []
        for a in range(lands_to_return):
            kitta = int(input("Enter the kitta number of the land to return: "))
            land = self.land_data[kitta]
            if kitta in self.land_data and self.land_data[kitta]["status"].lower() == "not available":
                months_late = int(input("Enter the number of months land with kitta "+str(kitta)+ " is late: "))
                if months_late > 0:
                    late_fee = land["price"] * 1.5 * months_late  # Late fee is 150% of monthly rent per month late
                    print("Late fee for "+str(months_late)+" month(s) is "+ str(late_fee))
                else:
                    late_fee = 0
                total_amount_fine += late_fee  # Add late fee to total amount
                lands.append({
                    "kitta": kitta,
                    "city": land["city"],  # Get city from land data
                    "area": land["area"],  # Get area from land data
                    "price": land["price"],  # Get price from land data
                    "late_months": months_late,  # Include late months in the returned lands information
                    "fine": late_fee  # Include late fee as fine in the returned lands information
                })
            else:
                print("Land with kitta "+str(kitta)+" is not rented or does not exist.")

        if lands:  # Generate return invoice only if there are lands to return
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            bill_number = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            transaction_details = {
                "customer": customer,
                "lands": lands,
                "total_amount": total_amount_fine  # Total amount now includes late fees
            }
            invoice_writer.generate_invoice_return(transaction_details, current_date, customer, bill_number)
            invoice_writer.print_return_invoice_details(transaction_details, current_date, customer, bill_number)
