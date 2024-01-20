# class ParkingLot:
#     def __init__(self):
#         self.levels = {'A': {}, 'B': {}}
#         self.space = set()

#         # Initialize parking spot
#         for level in ['A', 'B']:
#             for spot in range(1, 21):
#                 self.space.add((level, spot))

#     def assign_parking_spot(self, vehicle_number):
#         if not self.space:
#             return "Parking lot is full."

#         level, spot = self.space.pop()
#         self.levels[level][vehicle_number] = spot
#         return {"level": level, "spot": spot}

#     def retrieve_parking_spot(self, vehicle_number):
#         for level, spot in self.levels.items():
#             if vehicle_number in spot:
#                 return {"level": level, "spot": spot[vehicle_number]}

#         return "Vehicle not found in the parking lot."

#     def unpark_vehicle(self, vehicle_number):
#         for level, spot in self.levels.items():
#             if vehicle_number in spot:
#                 self.space.append((level, spot[vehicle_number]))
#                 del spot[vehicle_number]
#                 return f"Vehicle {vehicle_number} has been unparked."

#         return "Vehicle not found in the parking lot."

#     def retrieve_nearest_parking_location(self):
#         if not self.space:
#             return "Parking lot is full."

#         level, spot = self.space.pop()
#         self.space.add((level, spot))  # Add it back as it's not actually assigned
#         return {"level": level, "spot": spot}


# # Example Usage
# parking_lot = ParkingLot()

# # Assign a parking spot
# result = parking_lot.assign_parking_spot("ABC123")
# print(result)  # Output: {"level": "A", "spot": 1}

# # Retrieve parking spot for a vehicle
# result = parking_lot.retrieve_parking_spot("ABC123")
# print(result)  # Output: {"level": "A", "spot": 1}

# # Unpark a vehicle
# result = parking_lot.unpark_vehicle("ABC123")
# print(result)  # Output: "Vehicle ABC123 has been unparked."

# # Retrieve the nearest parking location
# result = parking_lot.retrieve_nearest_parking_location()
# print(result)  # Output: {"level": "A", "spot": 1}




class ParkingLot:
    slots = {"A": dict.fromkeys(range(1, 3)), "B": dict.fromkeys(range(3, 5))}

    def _find(self, num=None):
        spot = None
        if not num:
            operator = lambda: is_empty is None
        else:
            operator = lambda: is_empty == num
        for floor, floor_slots in self.slots.items():
            for slot, is_empty in floor_slots.items():

                if operator():
                    spot = floor, slot
                    return spot
        if not spot:
            return 

    def park(self, number):
        spot = self._find()
        
        self.slots[spot[0]][spot[1]] = number
       
    def find_park(self, number=None):
        return self._find(number)

    def unpark(self, number):
        spot = self.find_park(number)

        self.slots[spot[0]][spot[1]] = None
        print(spot)


if __name__ == "__main__":
    parking_lot = ParkingLot()
    def find_parking():
        num = input("""
1. For Parked vehicle
2. Nearest empty Parking"""
            )
        text = ""
        vehicle_num = None
        if num == "1":
            text = "Vehicle is parked at"
            vehicle_num = input(" enter vehicle number")
        elif num == "2":
            text = "Nearest empty spot at "
        else:
            text = "Invalid choice"
        spot = parking_lot.find_park(vehicle_num) if text else ""
        if not spot:
            text = "vehicle not found"
            spot = ''
        print(text, spot)

    x = True
    while x:
        choice = input(
            """
        1. To Park
        2. Find Parking
        3. Unpark
        0. To Exit the program
    """
        )
        c = choice
        if c == "0":
            x = False
        elif c == "1":
            if parking_lot.find_park() is None:
                print("No Spot Is Available")
            else:
                import pdb;pdb.set_trace()
                print("nearest parking at", parking_lot.find_park())
                num = input("vehicle numer")
                parking_lot.park(num)
        elif c == "2":
            find_parking()
        elif c == "3":
            num = input("vehicle numer")
            parking_lot.unpark(num)
        else:
            print("Invalid input try again")
print("Exiting")


