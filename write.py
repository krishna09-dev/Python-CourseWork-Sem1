import os
import datetime

class InvoiceWriter:
    @staticmethod
    def generate_invoice(transaction_details, current_date, customer, bill_number):
        try:
            os.makedirs("transactions", exist_ok=True)  # Ensure "transactions" directory exists
            print("Directory 'transactions' created successfully.")
            invoice_name = f"transactions/{customer}_rent_{bill_number}.txt"
            print("Invoice file path:", invoice_name)  # Print file path for debugging
            with open(invoice_name, "w") as file:
                border_top_bottom = "=" * 118
                border_middle = "-" * 118

                file.write(border_top_bottom + "\n")
                file.write(" " * 40 + "Land Rental Management System\n")
                file.write(" " * 47 + "Invoice\n")
                file.write(border_top_bottom + "\n")
                file.write(f"Date: {current_date}\n")
                file.write(f"Customer: {customer}\n")
                file.write(f"Bill Number: {bill_number}\n")
                file.write(border_middle + "\n")
                file.write("    \tKitta   \tCity/District  \tArea       \tPrice per Ana      Duration      \tTotal Price\n")
                file.write(border_middle + "\n")
                for land in transaction_details['lands']:
                    file.write(f"   \t{land['kitta']:4}      \t{land['city']:<15}  \t{land['area']:5}         \t{land['price']:10}       \t{transaction_details['duration']:8}      \t{land['price'] * transaction_details['duration']}\n")
                file.write(border_top_bottom + "\n")
                file.write(f"Grand Total: {transaction_details['total_amount']}\n")
                file.write(border_top_bottom + "\n")
            print("Invoice generated successfully.")
            
            # Call method to update land availability
            InvoiceWriter.update_land_availability(transaction_details['lands'])
            
        except Exception as e:
            print(f"Error generating invoice: {e}")


    @staticmethod
    def update_land_availability(rented_lands):
        try:
            # Read the land data file and update status of rented lands
            with open("land_detail.txt", "r") as file:
                lines = file.readlines()
    
            # Update status of rented lands in the land data
            for i, line in enumerate(lines):
                kitta, city, direction, area, price, status = line.strip().split(", ")
                kitta = int(kitta)
                if kitta in [land['kitta'] for land in rented_lands]:
                    status = "Not Available"
                    lines[i] = f"{kitta}, {city}, {direction}, {area}, {price}, {status}\n"
    
            # Write the updated land data back to the file
            with open("land_detail.txt", "w") as file:
                file.writelines(lines)
    
            print("Land availability updated successfully.")
    
        except Exception as e:
            print(f"Error updating land availability: {e}")
