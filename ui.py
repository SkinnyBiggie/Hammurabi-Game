from service import *

class UI:
    def __init__(self, service):
        self.service = service

    def view_buy_acres(self):
        try:
            acres_to_buy = int(input("Acres to buy/sell(+/-)-> "))
            self.service.buy_acres(acres_to_buy)
        except ValueError as e:
            print(e)
            self.view_buy_acres()
        except Exception as e:
            print(e)
            self.view_buy_acres()

    def view_feed_people(self):
        try:
            units_to_feed = int(input("Units to feed the population-> "))
            self.service.feed_people(units_to_feed)
        except ValueError as e:
            print(e)
            self.view_feed_people()
        except Exception as e:
            print(e)
            self.view_feed_people()

    def view_plant_acres(self):
        try:
            acres_to_plant = int(input("Acres to plant-> "))
            self.service.plant_acres(acres_to_plant)
        except ValueError as e:
            print(e)
            self.view_plant_acres()
        except Exception as e:
            print(e)
            self.view_plant_acres()

    def start(self):
        print(str(self.service.current_year))
        for i in range(4):
            self.view_buy_acres()
            self.view_feed_people()
            self.view_plant_acres()
            self.service.next_year()
            print(str(self.service.current_year))
            if self.service.game_lost:
                print("GAME OVER. You were a bad ruler.")
                return
        if self.service.current_year.acres >= 1000 and self.service.current_year.population >= 100:
            print("GAME OVER. You were a good ruler.")
            return
        else:
            print("GAME OVER. You were a bad ruler.")
            return
