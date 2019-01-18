import sys
import sqlite3

nice_list = '/Users/braddavis/workspace/python/exercises/bagOfLoot/testing/data/santa.db'

# Checks if child exists and if not, adds to the database
def checkChild(name):
  with sqlite3.connect(nice_list) as taco:
      cursor = taco.cursor()
      try:
        cursor.execute(f'''SELECT *
                         FROM Children c
                         Where c.Name = '{name}'
                         ''')
        child_check = cursor.fetchone()
        if child_check == None:
          cursor.execute(
            '''
            Insert Into Children
              Values(?, ?, ?)
            ''', (None, name, "NICE")
          )
          cursor.execute(f'''SELECT *
                         FROM Children c
                         Where c.Name = '{name}'
                         ''')
          child_check = cursor.fetchone()
          return child_check
      except sqlite3.OperationalError as err:
        print("error", err)
        print()


# Checks if a child exists in db by name
def checkName(name):
  with sqlite3.connect(nice_list) as taco:
      cursor = taco.cursor()
      try:
        cursor.execute(f'''SELECT *
                         FROM Children c
                         Where c.Name = '{name}'
                         ''')
        name_check = cursor.fetchone()
        return name_check
      except sqlite3.OperationalError as err:
        print("error", err)
        print()

# Checks if existing child has a gift with given name
def checkGift(name, childId):
  with sqlite3.connect(nice_list) as taco:
      cursor = taco.cursor()
      try:
        cursor.execute(f'''SELECT *
                          FROM Gifts g
                          Join Children c
                          On c.ChildId = g.ChildId
                          Where g.Name = "{name}"
                          And c.childId = {childId}
                         ''')
        gift_check = cursor.fetchone()
        return gift_check
      except sqlite3.OperationalError as err:
        print("error", err)
        print()
        temp = "None"
        return temp


def handleInputs():
  method_request = sys.argv[1].upper()
  first = sys.argv[2].title()
  second = sys.argv[3].title()

  if method_request == "ADD":
    santa = SantasBag()
    temp = checkChild(second)
    santa.add_gift(temp[0], first)

  if method_request == "REMOVE":
    santa = SantasBag()
    temp = checkName(first)
    if temp == None:
      print(f"There is no child by the name of {first} in our system.")
      print()
    else:
      gift = checkGift(second, temp[0])
      if gift == None:
        print(f"{temp[1]} doesn't have a {second} on their list. Please try again.")
        print()
      else:
        santa.remove_gift(gift)




class SantasBag():
  def __init__(self):
    self.children = []
    self.gifts = []
    self.delivery_status = []


  # Adds gift to database
  def add_gift(self, childId, gifts):
    with sqlite3.connect(nice_list) as taco:
      cursor = taco.cursor()
      try:
        cursor.execute(
            '''
            Insert Into Gifts
              Values(?, ?, ?, ?, ?, ?, ?)
            ''', (None, gifts, 0, 0, 0, 0, childId)
        )
      except ValueError as err:
        print(f"Error: {err}")
        print()


  # Removes gift from database
  def remove_gift(self, gift):
    giftId = gift[0]
    with sqlite3.connect(nice_list) as taco:
      cursor = taco.cursor()
      try:
        cursor.execute(f'''DELETE from Gifts
                          Where Gifts.GiftId = {giftId}
                        ''')
        print(f"Successfully removed {gift[1]} from child.")
        print()
      except ValueError as err:
        print(f"Delete Error: {err}")
        print()


  def naughty(self, name):
    name = name.title()
    try:
      index = self.children.index(name)
      if self.delivery_status[index][0] == False:
        self.gifts[index] = []
      else:
        print(f"{name} already received their gifts. You will have to put them on next year's naught list.")
        print()
    except ValueError:
      print(f"There is no child with the name {name.title()} in the system.")
      print()


  def deliver_gifts(self, child, month, day, year):
    name = child.title()
    if isinstance(month, int):
      if isinstance(day, int):
        if isinstance(year, int):
          try:
            index = self.children.index(name)
            if len(self.gifts[index]) > 0:
              if self.delivery_status[index][0] == False:
                self.delivery_status[index] = [True, [month, day, year]]
              else:
                print("This child has already recieved their gifts. You can't deliver again until next year.")
                print()
            else:
              print(f"{name} does not have any gifts listed to deliver. Please add gifts and try again.")
              print()
          except ValueError:
            print("There is no child with that name in the system.")
        else:
          raise ValueError("Delivering gifts requires the format of 'Name', month, day, year.")
      else:
        raise ValueError("Delivering gifts requires the format of 'Name', month, day, year.")
    else:
      raise ValueError("Delivering gifts requires the format of 'Name', month, day, year.")


  def all_gifts(self):
    i = 0
    print("All Children Getting Gifts")
    print("__________________________")
    for getting_gifts in self.gifts:
      if len(getting_gifts) > 0:
        print(self.children[i])
        i = i + 1
      else:
        i = i + 1
    print("\n")


  def print_bag(self):
    i = 0
    print("      Gift List      ")
    print("_____________________")
    while i < len(self.children):
      print(f"-----{self.children[i]}-----")
      if len(self.delivery_status[i]) == 1 and len(self.gifts[i]) != 0:
        print(f"(Gifts are pending delivery.)")
      elif len(self.gifts[i]) > 0:
        print(f"(Gifts were delivered on {self.delivery_status[i][1][0]}/{self.delivery_status[i][1][1]}/{self.delivery_status[i][1][2]}.)")
      gifts = self.gifts[i]
      if len(gifts) == 0:
        print(f"No gifts are set to be delivered to {self.children[i]}.")
        print("\n")
      else:
        for gift in gifts:
          print(f"{gift}")
        print("\n")
      i = i + 1


  def toys_for_child(self, child_name):
    name = child_name.title()
    try:
      index = self.children.index(name)
      print(f"--Gifts for {name}--")
      print("__________________")
      if len(self.gifts[index]) > 0:
        for gift in self.gifts[index]:
          print(gift)
      else:
        print(f"{name} is not getting any gifts.")
        print()
    except ValueError:
      print(f"There is no child with the name of {name} in the system.")

if __name__ == "__main__":
  handleInputs()

# santa = SantasBag()

# santa.add_gift("Billy", "ball")
# santa.add_gift("deanna", "car")
# santa.add_gift("deanna", "lights")
# santa.add_gift("billy", "BAT")
# santa.add_gift("joe", "tv", "dvd player", "xbox")
# santa.remove_gift("bob", "radio")
# santa.add_gift("joe", "power strip")
# santa.print_bag()
# santa.all_gifts()
# santa.add_gift("brad", "drill press")
# santa.add_gift("steve", "nintendo")
# santa.remove_gift("deanna", "lights")
# santa.deliver_gifts("joe", "2018/12/01")
# santa.remove_gift("billy", "car")
# santa.remove_gift("deanna", "car")
# santa.deliver_gifts("deanna", 12, 25, 2018)
# santa.print_bag()
# santa.naughty("billy")
# santa.remove_gift("deanna", "cars")
# santa.remove_gift("steve", "nintendo")
# santa.all_gifts()
# santa.print_bag()
# santa.add_gift("deanna", "kit kats")
# santa.add_gift("joe", "car cover")
# santa.print_bag()
# santa.toys_for_child("joe")
# santa.toys_for_child("bubba")


  # import sqlite3
  # import sys

  # print(sys.argv)

  # name_of_db =
  # '/Users/brad..../nam_of_db without .db'

  # def getDataFunc():
  #   with sqlite3.connect(super_db) as conn:
  #     cursor = conn.cursor()

      # for row in cursor.execute('SELECT * FROM Superhero'):
        # print(row
        #

  # ANOTHER WAY
    # cursor.execute('SELECT * FROM Superhero'):
    # supers = cursor.fetchall()


  # GET ONE SUPERHERO
  #def getSuper(super):
  #   with sqlite3.connect(super_db) as conn:
  #     cursor = conn.cursor()
    #   cursor.execute(f'''SELECT s.*, sidekick.Name
    #                     FROM Superhero s
    #                     Join Sidekick side
    #                     ON s.Superhero_Id = side.Superher_id
    #                     Where s.Name = '{super}'
    #                     ''')
    #   super = cursor.fetchone()
    #   print(super)
    #   return super


  #def addSuper(super):
  # with sqlite3.connect(super_db) as taco:
  #   cursor = taco.cursor()
  #
    # try:
    #   cursor.execute(
    #     '''
    #      Insert Into Superhero
    #       Values(?, ?, ?, ?, ?)
    #     ''', (None, super["name"], super["gender"], super["secret"], NOne)
    #   )
    # except sqlite3.OperationalError as err:
    #   print("oops", err)
    # )

  # if __name__ == "__main__":
  #   getSupers()
  #   getSuper(sys.argv[1])
  #   addSuper({
  #     "name": "Captain Derp",
  #     "gender": "Male",
  #     "secret": "Unknown"
  #   })
  #   getSupers()