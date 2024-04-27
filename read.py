class LandReader:
    def load_land_data(self):
        land_data = {}
        with open("land_detail.txt", "r") as file:
            for line in file:
                if line.strip():  # Check if line is not empty
                    kitta, city, direction, area, price, status = line.strip().split(", ")
                    land_data[int(kitta)] = {
                        "city": city,
                        "direction": direction,
                        "area": int(area),
                        "price": int(price),
                        "status": status
                    }
        return land_data
