import random

class Service:
    def __init__(self, year):
        self.current_year = year
        self.game_lost = False
        self.game_won = False


    def get_year(self):
        return self.current_year.year

    def buy_acres(self, acres_to_buy):
        """
        Function to buy or sell acres. If acres_to_buy is positive, it buys acres. If acres_to_buy is negative, it sells acres.
        :param acres_to_buy: The amount of acres we want to buy or sell
        :return: --
        """
        if acres_to_buy > 0:           #buy acres
            if acres_to_buy * self.current_year.land_price > self.current_year.stock:
                raise Error("You don't have enough grain to buy that many acres.")
            else:
                self.current_year.acres = self.current_year.acres + acres_to_buy
                self.current_year.stock = self.current_year.stock - (acres_to_buy * self.current_year.land_price)


        if acres_to_buy < 0:              #sell acres
            acres_to_sell = acres_to_buy * -1
            if acres_to_sell > self.current_year.acres:
                raise Error("You don't have that many acres to sell.")
            else:
                self.current_year.stock = self.current_year.stock + (acres_to_sell * self.current_year.land_price)
                self.current_year.acres = self.current_year.acres - acres_to_sell


    def feed_people(self, feed_amount):
        """
        Function to feed people. It takes the amount of people to feed and divides it by 20 to get the amount of acres to feed.
        :param feed_amount: The amount of units to feed
        :return:  --
        """
        if feed_amount < 0:
            raise Error("You can't feed negative people.")
        if feed_amount // 20 > self.current_year.population:
            raise Error("You don't have that many people to feed.")
        if feed_amount > self.current_year.stock:
            raise Error("You don't have enough grain to feed that many people.")
        self.current_year.stock = self.current_year.stock - feed_amount
        self.current_year.starved = self.current_year.population - (feed_amount // 20)


    def plant_acres(self, acres_to_plant):
        """
        Function to plant acres. It takes the amount of acres to plant and subtracts it from the current amount of acres.
        :param acres_to_plant: The amount of acres we want to plant
        :return: --
        """
        if acres_to_plant < 0:
            raise Error("You can't plant negative acres.")
        if acres_to_plant > self.current_year.stock:
            raise Error("You don't have enough grain to plant that many acres.")
        if acres_to_plant > self.current_year.acres:
            raise Error("You don't have that many acres to plant.")
        self.current_year.planted_acres = acres_to_plant
        self.current_year.stock = self.current_year.stock - acres_to_plant


    def next_year(self):
        """
        Function to go to the next year. It calculates the amount of rats, the amount of harvest, the amount of new people,
        the amount of stock and the amount of population.
        :return: --
        """
        self.current_year.year = self.current_year.year + 1
        self.current_year.harvest = random.randint(1,6)
        self.current_year.land_price = random.randint(15, 25)
        self.current_year.stock = self.current_year.stock + (self.current_year.harvest * self.current_year.planted_acres)

        if self.current_year.starved ==0:
            people_came = random.randint(0, 10)
            self.current_year.new_people = people_came
            self.current_year.population = self.current_year.population + people_came
        else:
            previous_population = self.current_year.population
            self.current_year.population = self.current_year.population - self.current_year.starved
            if self.current_year.population < previous_population // 2:
                self.game_lost = True
            self.current_year.new_people = 0
        rats_chance = random.randint(1, 100)
        if rats_chance <= 200:
            self.current_year.rats = random.randint(1, 10) * self.current_year.stock // 100
            self.current_year.stock = self.current_year.stock - self.current_year.rats
        else:
            self.current_year.rats = 0

class Error(Exception):
    pass