class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.parked_cars = {}

    def park_car(self, car_number):
        if self.available_spots > 0:
            if car_number not in self.parked_cars:
                self.parked_cars[car_number] = True
                self.available_spots -= 1
                return f"Car {car_number} parked successfully"
            return f"Car {car_number} is already parked"
        return "Sorry, parking is full"

    def remove_car(self, car_number):
        if car_number in self.parked_cars:
            del self.parked_cars[car_number]
            self.available_spots += 1
            return f"Car {car_number} removed successfully"
        return f"Car {car_number} not found in parking"

    def get_status(self):
        return f"Available spots: {self.available_spots}/{self.total_spots}"

def main():
    # Create parking lot with 5 spots
    parking = ParkingLot(5)
    
    while True:
        print("\n1. Park Car")
        print("2. Remove Car")
        print("3. Check Status")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            car_num = input("Enter car number: ")
            print(parking.park_car(car_num))
            
        elif choice == '2':
            car_num = input("Enter car number: ")
            print(parking.remove_car(car_num))
            
        elif choice == '3':
            print(parking.get_status())
            
        elif choice == '4':
            print("Thank you for using the parking system!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()