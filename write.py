# write.py
from read import LandReader
import datetime

class InvoiceWriter:
    def generate_invoice(self, transaction_details):
        try:
            bill_number = transaction_details["bill_number"]  # Retrieve bill_number from transaction_details
            customer = transaction_details["customer"]  # Retrieve customer name from transaction_details
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')

            invoice_name = str(customer)+"_rent_"+str(bill_number)+".txt"
            print("Invoice file name:", invoice_name)  # Print file path for debugging
            with open(invoice_name, "w") as file:
                border_top_bottom = "=" * 118
                border_middle = "-" * 118

                file.write(border_top_bottom + "\n")
                file.write(" " * 40 + "Land Rental Management System\n")
                file.write(" " * 47 + "Invoice\n")
                file.write(border_top_bottom + "\n")
                file.write("Date: " + str(current_date) + "\n")
                file.write("Customer: " + str(customer) + "\n")
                file.write("Bill Number: " + str(bill_number) + "\n")
                file.write(border_middle + "\n")
                file.write("      Kitta     City/District    tArea         Price per Ana      Duration        Total Price  ")
                file.write(border_middle + "\n")
                for land in transaction_details['lands']:
                    file.write("   \t" + str(land['kitta']) + "      \t" + str(land['city'])+ "       \t" + str(land['area']) + "         \t" + str(land['price']) + "       \t" + str(land['duration']) + "      \t" + str(land['price'] * land['duration']) + "\n")
                file.write(border_top_bottom + "\n")
                file.write("Grand Total: " + str(transaction_details['total_amount']) + "\n")
                file.write(border_top_bottom + "\n")

            print("Invoice generated successfully.")

            # Call the update_land_availability method
            self.update_rented_lands_status(transaction_details['lands'])

        except Exception as e:
            print("Error generating invoice: "+str(e))

    def print_invoice_details(self, transaction_details):
        border_top_bottom = "=" * 118
        border_middle = "-" * 118

        print(border_top_bottom)
        print(" " * 40 + "Land Rental Management System")
        print(" " * 47 + "Invoice")
        print(border_top_bottom)
        print("Date: " + str(datetime.datetime.now().strftime('%Y-%m-%d')))
        print("Customer: " + str(transaction_details["customer"]))
        print("Bill Number: " + str(transaction_details["bill_number"]))
        print(border_middle)
        print("      Kitta     City/District    tArea         Price per Ana      Duration        Total Price  ")
        print(border_middle)
        for land in transaction_details['lands']:
            print("   \t" + str(land['kitta']) + "      \t" + str(land['city']) + "     \t" + str(land['area']) + "         \t" + str(land['price']) + "       \t" + str(land['duration']) + "      \t" + str(land['price'] * land['duration']))
        print(border_top_bottom)
        print("Grand Total: " + str(transaction_details['total_amount']))
        print(border_top_bottom)


    def update_rented_lands_status(self, rented_lands):
        try:
            updated_lines = []  # List to store updated lines  
            # Read the land data file and update status of rented lands  
            with open("land_detail.txt", "r") as file:
                lines = file.readlines()

            # Update status of rented lands in the land data
            for line in lines:
                land_info = line.replace(" ", "").split(", ")
                kitta = int(land_info[0])
                for land in rented_lands:
                    if land["kitta"] == kitta:
                        land_info[-1] = "Not Available"  # Change status to "Not Available" for rented lands
                        break  # Once status is updated, no need to check further
                updated_line = land_info[0]
                for item in land_info[1:]:
                    updated_line += ', ' + item
                updated_line += '\n'
                updated_lines.append(updated_line)

                
            # Write the updated land data back to the file
            with open("land_detail.txt", "w") as file:
                for updated_line in updated_lines:
                    file.write(updated_line)

            print("Land availability updated successfully.")

        except Exception as e:
            print(f"Error updating land availability: {e}")



    def update_land_availability(self, returned_lands):
        try:
            updated_lines = []  # List to store updated lines  
            # Read the land data file and update status of returned lands  
            with open("land_detail.txt", "r") as file:
                lines = file.readlines()

            # Update status of returned lands in the land data
            for line in lines:
                land_info = line.replace(" ", "").split(", ")  # Remove leading/trailing whitespace before splitting
                kitta = int(land_info[0])
                for land in returned_lands:
                    if land["kitta"] == kitta:
                        land_info[-1] = "Available"  # Change status to "Available"
                        break  # Once status is updated, no need to check further
                updated_line = ", ".join(land_info) + '\n'
                updated_lines.append(updated_line)

            # Write the updated land data back to the file
            with open("land_detail.txt", "w") as file:
                for updated_line in updated_lines:
                    file.write(updated_line)

            print("Land availability updated successfully.")

        except Exception as e:
            print(f"Error updating land availability: {e}")





    def generate_invoice_return(self, transaction_details, current_date, customer, bill_number):
        try:
            invoice_name = customer + "_return_" + str(bill_number) + ".txt"  # Adjust invoice name for return
            print("Invoice file path:" + invoice_name)  # Print file path for debugging
            with open(invoice_name, "w") as file:
                border_top_bottom = "=" * 118
                border_middle = "-" * 118

                file.write(border_top_bottom + "\n")
                file.write(" " * 40 + "Land Rental Management System\n")
                file.write(" " * 47 + "Return Invoice\n")  # Update invoice title
                file.write(border_top_bottom + "\n")
                file.write("Date: " + str(current_date) + "\n")
                file.write("Customer: " + customer + "\n")
                file.write("Bill Number: " + str(bill_number) + "\n")
                file.write(border_middle + "\n")
                file.write("    \tKitta   \tCity/District  \tArea       \tPrice per Ana      Late Month      \tFine\n")
                file.write(border_middle + "\n")
                total_price = 0  # Initialize total price
                for land in transaction_details['lands']:
                    late_months = land["late_months"]
                    fine = land["fine"]
                    total_price += fine  # Update total price
                    file.write("   \t" + str(land['kitta']) + "      \t" + str(land['city']) + "      \t" + str(land['area']) + "         \t" + str(land['price']) + "       \t" + str(late_months) + "      \t" + str(fine) + "\n")
                    file.write("Late Months: " + str(late_months) + "\n")  # Add late months information
                    file.write("Fine: " + str(fine) + "\n")  # Add fine information
                file.write(border_top_bottom + "\n")
                file.write("Grand Total: " + str(total_price) + "\n")
                file.write(border_top_bottom + "\n")
            print("Return invoice generated successfully.")
            self.update_land_availability(transaction_details['lands'])
        except Exception as e:
            print("Error generating return invoice: " + str(e))



    def print_return_invoice_details(self, transaction_details, current_date, customer, bill_number):
        border_top_bottom = "=" * 118
        border_middle = "-" * 118

        print(border_top_bottom)
        print(" " * 40 + "Land Rental Management System")
        print(" " * 47 + "Return Invoice")
        print(border_top_bottom)
        print("Date: " + str(current_date))
        print("Customer: " + customer)
        print("Bill Number: " + str(bill_number))
        print(border_middle)
        print("    \tKitta   \tCity/District  \tArea       \tPrice per Ana      Late Month      \tFine")
        print(border_middle)
        total_price = 0  # Initialize total price
        for land in transaction_details['lands']:
            late_months = land["late_months"]
            fine = land["fine"]
            total_price += fine  # Update total price
            print("   \t" + str(land['kitta']) + "      \t" + str(land['city']) + "      \t" + str(land['area']) + "         \t" + str(land['price']) + "       \t" + str(late_months) + "      \t" + str(fine))
            print("Late Months: " + str(late_months))  # Add late months information
            print("Fine: " + str(fine))  # Add fine information
        print(border_top_bottom)
        print("Grand Total: " + str(total_price))
        print(border_top_bottom)

