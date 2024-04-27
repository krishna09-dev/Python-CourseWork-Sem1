from write import InvoiceWriter
from read import LandReader
import datetime

class LandOperation:
    def __init__(self):
        self.land_reader = LandReader()  # Instantiate LandReader
        self.land_data = self.land_reader.load_land_data()  # Call load_land_data() on the instance

    def display_land(self):
        border_top_bottom = "\033[1;36m╔" + "═" * 15 + "╦" + "═" * 20 + "╦" + "═" * 15 + "╦" + "═" * 10 + "╦" + "═" * 10 + "╦" + "═" * 10 + "╗\033[0m"
        border_middle = "\033[1;36m╠" + "═" * 15 + "╬" + "═" * 20 + "╬" + "═" * 15 + "╬" + "═" * 10 + "╬" + "═" * 10 + "╬" + "═" * 10 + "╣\033[0m"
        header = "\033[1;36m║ {:^15} ║ {:^20} ║ {:^15} ║ {:^10} ║ {:^10} ║ {:^10} ║\033[0m".format("Kitta", "City/District", "Direction", "Area", "Price", "Status")
        print(border_top_bottom)
        print(header)
        print(border_middle)

        for kitta, details in self.land_data.items():
            row = "\033[1;36m║ {:^15} ║ {:^20} ║ {:^15} ║ {:^10} ║ {:^10} ║ {:^10} ║\033[0m".format(kitta, details['city'], details['direction'], details['area'], details['price'], details['status'])
            print(row)

        print(border_top_bottom)



    def rent_land(self):
        customer = input("Enter your name: ")
        duration = int(input("Enter the duration of rent (in months): "))
        total_amount = 0
        lands = []
        while True:
            kitta = int(input("Enter the kitta number of land you want to rent: "))
            if self.land_data.get(kitta, {}).get("status", "").lower() == "available":
                total_amount += self.land_data[kitta]["price"] * duration
                lands.append({
                    "kitta": kitta,
                    "city": self.land_data[kitta]["city"],
                    "direction": self.land_data[kitta]["direction"],
                    "area": self.land_data[kitta]["area"],
                    "price": self.land_data[kitta]["price"]
                })
                self.land_data[kitta]["status"] = "Not Available"
                print("Land rented successfully.")
            else:
                print("Land is not available for rent.")
            more = input("Do you want to rent more land? (yes/no): ")
            if more.lower() != "yes":
                break

        # Generate transaction details and call method to generate invoice only if lands are rented
        if lands:
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            bill_number = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            transaction_details = {
                "customer": customer,
                "duration": duration,
                "lands": lands,
                "total_amount": total_amount
            }
            InvoiceWriter.generate_invoice(transaction_details, current_date, customer, bill_number)
        else:
            print("No land rented, so no invoice generated.")

    def return_land(self):
        while True:
            kitta = int(input("Enter the kitta number of land you want to return (enter 0 to stop): "))
            if kitta == 0:
                break
            if self.land_data.get(kitta, {}).get("status", "").lower() == "not available":
                months_late = int(input("Enter the number of months the land is late: "))
                if months_late > 0:
                    late_fee = self.land_data[kitta]["price"] * 1.5 * months_late  # Late fee is 150% of monthly rent per month late
                    print(f"Late fee for {months_late} month(s) is {late_fee}.")
                else:
                    late_fee = 0
                self.land_data[kitta]["status"] = "Available"
                print("Land returned successfully.")
            else:
                print("Land is not rented or does not exist.")