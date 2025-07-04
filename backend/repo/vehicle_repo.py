class VehicleRepo:
    def __init__(self):
        self.vehicle_map = {}

    def find_vehicle_by_number(self, vehicle_number):
        if vehicle_number in self.vehicle_map:
            return self.vehicle_map[vehicle_number]
        return None
    
    def save_vehicle(self, vehicle):
        self.vehicle_map[vehicle.number] = vehicle
        return vehicle
