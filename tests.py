import unittest
from src.domain import *
from src.service import *


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.year = Year()
        self.service = Service(self.year)
        self.old_acres = self.service.current_year.acres
        self.old_stock = self.service.current_year.stock

    def tearDown(self) -> None:
        pass


    def test_ServiceBuyGrains(self):
        self.service.buy_acres(1)
        self.assertEqual(self.service.current_year.acres, self.old_acres + 1)
        self.assertEqual(self.service.current_year.stock, self.old_stock - self.service.current_year.land_price)

    def test_ServiceSellGrains(self):
        self.service.buy_acres(-1)
        self.assertEqual(self.service.current_year.acres, self.old_acres - 1)
        self.assertEqual(self.service.current_year.stock, self.old_stock + self.service.current_year.land_price)

    def test_ServiceFeedPeople(self):
        self.service.feed_people(2000)
        self.assertEqual(self.service.current_year.starved, 0)
        self.assertEqual(self.service.current_year.stock, self.old_stock - self.service.current_year.population * 20)

    def test_ServicePlantAcres(self):
        self.service.plant_acres(100)
        self.assertEqual(self.service.current_year.stock, self.old_stock - 100)

if __name__ == '__main__':
    unittest.main()