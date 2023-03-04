from ui import *
from service import *
from domain import Year

year_one = Year()
service = Service(year_one)
ui = UI(service)
ui.start()
