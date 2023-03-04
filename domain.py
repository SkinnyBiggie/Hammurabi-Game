class Year:
    def __init__(self):
         self.year = 1
         self.new_people = 0
         self.starved = 0
         self.population = 100
         self.acres = 1000
         self.harvest = 3
         self.rats = 200
         self.land_price = 20
         self.stock = 2800
         self.planted_acres = 0

    def __str__(self):
        string_format  = "In year " + str(self.year) + ", " + str(self.starved) + " poeple starved.\n"
        string_format += str(self.new_people) + " people came to the city.\n"
        string_format += "City population is " + str(self.population) + ".\n"
        string_format += "City owns " + str(self.acres) + " acres of land.\n"
        string_format += "Harvest was " + str(self.harvest) + " units per acre.\n"
        string_format += "Rats ate " + str(self.rats) + " units of food.\n"
        string_format += "Land price is " + str(self.land_price) + " units per acre.\n"
        string_format += "Grain stocks are " + str(self.stock) + "units.\n"
        return string_format

