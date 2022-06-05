from datetime import time
# Convert this to Windows Forms
class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{name} menu is available from {start_time} to {end_time}".format(name = self.name, start_time = self.start_time, end_time = self.end_time)

  def calculate_bill(self, purchased_items):
      amount = 0
      for item in purchased_items:
          for key,value in self.items.items():
              if item == key:
                  amount += value
      return amount

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                for item,price in menu.items.items():
                    print('%-50s' % item + '$' + str(price))

class Business:
    def __init__(self, name, franchises):
        pass

brunch = Menu("Brunch", { 'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50 }, time.isoformat(time(11,00),timespec = 'minutes'), time.isoformat(time(16,00),timespec = 'minutes'))
early_bird = Menu("Early Bird", { 'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00 }, time.isoformat(time(15,00),timespec = 'minutes'), time.isoformat(time(18,00),timespec = 'minutes'))
dinner = Menu("Dinner", { 'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00 }, time.isoformat(time(17,00),timespec = 'minutes'), time.isoformat(time(23,00),timespec = 'minutes'))
kids = Menu("Kids", { 'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00 }, time.isoformat(time(11,00),timespec = 'minutes'), time.isoformat(time(21,00),timespec = 'minutes'))
arepas_menu = Menu("Take a' Arepa", { 'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50 }, time.isoformat(time(10,00),timespec = 'minutes'), time.isoformat(time(20,00),timespec = 'minutes'))

print(kids)

bru = brunch.calculate_bill({'pancakes', 'home fries', 'coffee'})
ear = early_bird.calculate_bill({'salumeria plate', 'mushroom ravioli (vegan)'})
print(ear)

flagship_store = Franchise("1232 West End Road", {brunch, early_bird, dinner, kids})
new_installment = Franchise("12 East Mulberry Street", {brunch, early_bird, dinner, kids})
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
print(flagship_store)
flagship_store.available_menus("17:00")
print(brunch)
print(early_bird)
print(dinner)
print(kids)

business1 = Business("Basts Fazoolin' with my Heart", {flagship_store, new_installment})
business2 = Business("Take a' Arepa", arepas_place)
