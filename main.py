
class Transportation:
    def __init__(self, fuel_type, distance, vehicle_type, transport_type):
        self.fuel_type = fuel_type
        self.distance = distance
        self.vehicle_type = vehicle_type
        self.transport_type = transport_type

    def calculate_emissions(self):
        emissions = 0
        if self.transport_type == 'car':
            if self.fuel_type == 'gasoline':
                if self.vehicle_type == 'sedan':
                    emissions = self.distance * 0.2  # 0.2 kg CO2 per km for a gasoline sedan
                elif self.vehicle_type == 'suv':
                    emissions = self.distance * 0.3  # 0.3 kg CO2 per km for a gasoline SUV
            elif self.fuel_type == 'diesel':
                if self.vehicle_type == 'sedan':
                    emissions = self.distance * 0.15  # 0.15 kg CO2 per km for a diesel sedan
                elif self.vehicle_type == 'suv':
                    emissions = self.distance * 0.25  # 0.25 kg CO2 per km for a diesel SUV
        elif self.transport_type == 'train':
            if self.fuel_type == 'electricity':
                emissions = self.distance * 0.05  # 0.05 kg CO2 per km for an electric train
            elif self.fuel_type == 'diesel':
                emissions = self.distance * 0.1  # 0.1 kg CO2 per km for a diesel train
        elif self.transport_type == 'bus':
            if self.fuel_type == 'gasoline':
                emissions = self.distance * 0.2  # 0.2 kg CO2 per km for a gasoline bus
            elif self.fuel_type == 'diesel':
                emissions = self.distance * 0.15  # 0.15 kg CO2 per km for a diesel bus
        elif self.transport_type == 'motorcycle':
            if self.fuel_type == 'gasoline':
                emissions = self.distance * 0.15  # 0.15 kg CO2 per km for a gasoline motorcycle
            elif self.fuel_type == 'electricity':
                emissions = self.distance * 0.05  # 0.05 kg CO2 per km for an electric motorcycle
        elif self.transport_type == 'tricycle':
            if self.fuel_type == 'gasoline':
                emissions = self.distance * 0.1  # 0.1 kg CO2 per km for a gasoline tricycle
            elif self.fuel_type == 'electricity':
                emissions = self.distance * 0.03  # 0.03 kg CO2 per km for an electric tricycle
        elif self.transport_type == 'walking' or 'cycling':
            emissions = self.distance * 0.00
        return emissions

class House:
    def __init__(self, square_footage, num_residents, energy_source, num_vehicles, location):
        self.square_footage = square_footage  # in square feet
        self.num_residents = num_residents
        self.energy_source = energy_source  # "electricity", "natural_gas", or "oil"
        self.num_vehicles = num_vehicles
        self.location = location  # "urban", "suburban", or "rural"

    def calculate_emissions(self):
        electricity_emissions = self.square_footage * 0.15  # 0.15 lbs CO2 per sq ft per month
        natural_gas_emissions = self.square_footage * 0.12  # 0.12 lbs CO2 per sq ft per month
        oil_emissions = self.square_footage * 0.18  # 0.18 lbs CO2 per sq ft per month

        if self.energy_source == "electricity":
            total_emissions = electricity_emissions
        elif self.energy_source == "natural_gas":
            total_emissions = natural_gas_emissions
        elif self.energy_source == "oil":
            total_emissions = oil_emissions
        else:
            raise ValueError("Invalid energy source")

        total_emissions += self.num_residents * 44  # 44 lbs CO2 per person per month

        if self.location == "urban":
            total_emissions += self.num_vehicles * 24  # 24 lbs CO2 per vehicle per month
        elif self.location == "suburban":
            total_emissions += self.num_vehicles * 15  # 15 lbs CO2 per vehicle per month
        elif self.location == "rural":
            total_emissions += self.num_vehicles * 10  # 10 lbs CO2 per vehicle per month
        else:
            raise ValueError("Invalid location")

        return total_emissions


class Diet:
    def __init__(self, meat_consumption, dairy_consumption, grain_consumption, fruit_veg_consumption,
                 seafood_consumption, meat_source, dairy_source, grain_source, fruit_veg_source, seafood_source):
        self.meat_consumption = meat_consumption
        self.dairy_consumption = dairy_consumption
        self.grain_consumption = grain_consumption
        self.fruit_veg_consumption = fruit_veg_consumption
        self.seafood_consumption = seafood_consumption
        self.meat_source = meat_source
        self.dairy_source = dairy_source
        self.grain_source = grain_source
        self.fruit_veg_source = fruit_veg_source
        self.seafood_source = seafood_source

    def calculate_carbon_footprint(self):
        meat_emissions = self.meat_consumption * 6.61  # in kg CO2e per kg of meat
        dairy_emissions = self.dairy_consumption * 2.44  # in kg CO2e per kg of dairy
        grain_emissions = self.grain_consumption * 0.65  # in kg CO2e per kg of grains
        fruit_veg_emissions = self.fruit_veg_consumption * 0.29  # in kg CO2e per kg of fruits and vegetables
        seafood_emissions = self.seafood_consumption * 3.0  # in kg CO2e per kg of seafood

        # emissions from food source
        meat_source_emissions = 0
        dairy_source_emissions = 0
        grain_source_emissions = 0
        fruit_veg_source_emissions = 0
        seafood_source_emissions = 0

        if self.meat_source == "beef":
            meat_source_emissions = self.meat_consumption * 60  # in kg CO2e per kg of beef
        elif self.meat_source == "pork":
            meat_source_emissions = self.meat_consumption * 7.7  # in kg CO2e per kg of pork
        elif self.meat_source == "chicken":
            meat_source_emissions = self.meat_consumption * 6.1  # in kg CO2e per kg of chicken

        if self.dairy_source == "cow":
            dairy_source_emissions = self.dairy_consumption * 2.44  # in kg CO2e per kg of dairy from cows
        elif self.dairy_source == "goat":
            dairy_source_emissions = self.dairy_consumption * 0.92  # in kg CO2e per kg of dairy from goats

        if self.grain_source == "imported":
            grain_source_emissions = self.grain_consumption * 1.1  # in kg CO2e per kg of imported grains
        elif self.grain_source == "local":
            grain_source_emissions = self.grain_consumption * 0.3  # in kg CO2e per kg of local grains

        if self.fruit_veg_source == "imported":
            fruit_veg_source_emissions = self.fruit_veg_consumption * 1.1  # in kg CO2e per kg of imported fruits and vegetables
        elif self.fruit_veg_source == "local":
            fruit_veg_source_emissions = self.fruit_veg_consumption * 0.3  # in kg CO2e per kg of local fruits and vegetables

        if self.seafood_source == "wild":
            seafood_source_emissions = self.seafood_consumption * 3.0  # in kg CO2e per kg of wild-caught seafood
        elif self.seafood_source == "farmed":
            seafood_source_emissions = self.seafood_consumption * 1.5  # in kg CO2e per kg of farmed seafood

        total_emissions = meat_emissions + dairy_emissions + grain_emissions + fruit_veg_emissions + seafood_emissions + \
                      meat_source_emissions + dairy_source_emissions + grain_source_emissions + \
                      fruit_veg_source_emissions + seafood_source_emissions

        return total_emissions


def set_diet(self, meat_consumption, dairy_consumption, grain_consumption, fruit_veg_consumption, seafood_consumption,
             meat_source, dairy_source, grain_source, fruit_veg_source, seafood_source):
    self.meat_consumption = meat_consumption
    self.dairy_consumption = dairy_consumption
    self.grain_consumption = grain_consumption
    self.fruit_veg_consumption = fruit_veg_consumption
    self.seafood_consumption = seafood_consumption
    self.meat_source = meat_source
    self.dairy_source = dairy_source
    self.grain_source = grain_source
    self.fruit_veg_source = fruit_veg_source
    self.seafood_source = seafood_source


def get_diet(self):
    return self.meat_consumption, self.dairy_consumption, self.grain_consumption, self.fruit_veg_consumption, \
        self.seafood_consumption, self.meat_source, self.dairy_source, self.grain_source, \
        self.fruit_veg_source, self.seafood_source

def main():
    # Collecting user input for transportation
    transport_type = input("What mode of transportation did you use? (car, train, bus, motorcycle, tricycle, walking, cycling): ")
    transportation_emissions = 0
    if transport_type == "walking" or transport_type == "cycling":
        pass
    else:
        fuel_type = input("What fuel type did you use? (gasoline, diesel, electricity): ")
        distance = float(input("How many kilometers did you travel? "))
        vehicle_type = ""
        if transport_type == "car" or transport_type == "motorcycle" or transport_type == "tricycle":
            vehicle_type = input("What type of vehicle did you use? (sedan, suv): ")
        # Creating a Transportation object
        transportation = Transportation(fuel_type, distance, vehicle_type, transport_type)
        transportation_emissions = transportation.calculate_emissions()


    # Collecting user input for diet
    
    meat_consumption = float(input("How many grams of meat did you consume? "))
    dairy_consumption = float(input("How many grams of dairy did you consume? "))
    grain_consumption = float(input("How many grams of grain did you consume? "))
    fruit_veg_consumption = float(input("How many grams of fruits and vegetables did you consume? "))
    seafood_consumption = float(input("How many grams of seafood did you consume? "))

    if meat_consumption == 0:
        meat_source = 0
    else:
        meat_source = input("What was the source of your meat? (beef, pork, poultry, fish, none): ")

    if dairy_consumption == 0:
        dairy_source = 0
    else:
        dairy_source = input("What was the source of your dairy? (cow, goat, sheep, none): ")
    if grain_consumption == 0:
        grain_source = 0
    else:
        grain_source = input("What was the source of your grain? (rice, wheat, corn, none): ")
    if fruit_veg_consumption == 0:
        fruit_veg_source = 0
    else:
        fruit_veg_source = input("What was the source of your fruits and vegetables? (local, imported, none): ")
    if seafood_consumption == 0:
        seafood_source = 0
    else:
        seafood_source = input("What was the source of your seafood? (local, imported, none): ")

    # Creating a Diet object
    diet = Diet(meat_consumption, dairy_consumption, grain_consumption, fruit_veg_consumption, seafood_consumption,
                meat_source, dairy_source, grain_source, fruit_veg_source, seafood_source)
    diet_emissions = diet.calculate_carbon_footprint()

    # Collecting user input for housing
    square_footage = float(input("What is the square footage of your house? "))
    num_residents = int(input("How many people live in your house? "))
    energy_source = input("What is the source of energy for your house? (electricity, natural_gas, oil): ")
    num_vehicles = int(input("How many vehicles do you own? "))
    location = input("What is the location of your house? (urban, suburban, rural): ")

    # Creating a House object
    house = House(square_footage, num_residents, energy_source, num_vehicles, location)
    house_emissions = house.calculate_emissions()

    # Calculating total carbon footprint
    total_emissions = (transportation_emissions + diet_emissions + house_emissions)/1000
    print("Your total carbon footprint is:", round(total_emissions, 2), "kg CO2 eq.")

if __name__ == '__main__':
    main()
