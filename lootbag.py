import sys
import sqlite3

nice_list = '/Users/braddavis/workspace/python/exercises/bagOfLoot/testing/data/bagOfLoot.db'


# Main handler for inputs from CLI
def handleInputs():
  santa = SantasBag()

  if len(sys.argv) == 2:
    method_request = sys.argv[1].upper()

  elif len(sys.argv) == 3:
    method_request = sys.argv[1].upper()
    first = sys.argv[2].title()

  elif len(sys.argv) == 4:
    method_request = sys.argv[1].upper()
    first = sys.argv[2].title()
    second = sys.argv[3].title()

  else:
    print()
    print("*********************************")
    print("********* Format Waring *********")
    print("*********************************")
    print()
    print("You have entered to many variables. Please try again.")
    print()
    print("TO DISPLAY HELP MENU")
    print("python lootbag.py help ")
    print()
    print("*********************************")
    print("*********************************")
    print("*********************************")
    print()

# List all children getting a gift or gifts for specific child
  if method_request == "LS":
    if len(sys.argv) == 2:
      santa.kidsGettingGifts()
    else:
      santa.indivKidGiftList(first)

# Add gift to a child
  if method_request == "ADD":
    temp = santa.checkChild(second)
    santa.add_gift(temp[0], first)

# Remove gift from a child
  if method_request == "REMOVE":
    temp = santa.checkName(first)
    if temp == None:
      print()
      print("**********************************")
      print("******  Gift Removal Alert  ******")
      print("**********************************")
      print()
      print(f"There is no child by the name of {first} in our system.")
      print()
      print("**********************************")
      print("**********************************")
      print("**********************************")
      print()
    else:
      gift = santa.checkGift(second, temp[0])
      if gift == None:
        print()
        print("**********************************")
        print("******  Gift Removal Alert  ******")
        print("**********************************")
        print()
        print(f"{temp[1]} doesn't have a {second} on their list. Please try again.")
        print()
        print("**********************************")
        print("**********************************")
        print("**********************************")
        print()
      else:
        santa.remove_gift(gift)

# Deliver gifts
  if method_request == "DELIVERED":
    if len(sys.argv) < 3:
      print()
      print("**********************************")
      print("********  Delivery Alert  ********")
      print("**********************************")
      print()
      print("You must enter a child's name to mark gifts as delivered.")
      print()
      print("**********************************")
      print("**********************************")
      print("**********************************")
      print()
    else:
      temp = santa.checkName(first)
      if temp == None:
        print()
        print("**********************************")
        print("********  Delivery Alert  ********")
        print("**********************************")
        print()
        print(f"There is no child by the name of {first} in our system.")
        print()
        print("**********************************")
        print("**********************************")
        print("**********************************")
        print()
      else:
        santa.deliverChildsGifts(temp)

# Display help menu
  if method_request == "HELP":
    print()
    print("-----------------------------------")
    print("-----------  Help Menu  -----------")
    print("-----------------------------------")
    print()
    print("- DISPLAY HELP MENU -")
    print("python lootbag.py help")
    print()
    print("- ADD GIFT FOR A CHILD -")
    print("python lootbag.py add (gift name) (child name)")
    print()
    print("- REMOVE GIFT FOR A CHILD -")
    print("python lootbag.py remove (child name) (gift name)")
    print()
    print("- LIST CHILDREN RECIEVING GIFTS -")
    print("python lootbag.py ls")
    print()
    print("- LIST GIFTS A CHILD IS RECIEVING -")
    print("python lootbag.py ls (child name)")
    print()
    print("- DELIVER GIFTS TO A CHILD -")
    print("python lootbag.py delivered (child name)")
    print()
    print("- ADD CHILD TO NAUGHTY LIST AND REMOVE GIFTS -")
    print("python lootbag.py bad (child name)")
    print()
    print("-----------------------------------")
    print("-----------------------------------")
    print("-----------------------------------")
    print()

# Add child to naught list and remove all gifts
  if method_request == "BAD":
    temp = santa.checkChild(first)
    print(temp)
    santa.naughtyList(temp)

class SantasBag():

  # Adds gift to database
  def add_gift(self, childId, gifts):
    with sqlite3.connect(nice_list) as connectData:
      cursor = connectData.cursor()
      try:
        cursor.execute(
            '''
            Insert Into Gifts
              Values(?, ?, ?, ?)
            ''', (None, gifts, 0, childId)
        )
        print()
        print("----------------------------------")
        print("---------  Gift Added  ---------")
        print("----------------------------------")
        print()
        print(f"Successfully added {gifts} to child's list.'")
        print()
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        print()
      except ValueError as err:
        print(f"Error: {err}")
        print()


  # Removes gift from database
  def remove_gift(self, gift):
    giftId = gift[0]
    with sqlite3.connect(nice_list) as connectData:
      cursor = connectData.cursor()
      try:
        cursor.execute(f'''DELETE from Gifts
                          Where Gifts.GiftId = {giftId}
                        ''')
        print()
        print("----------------------------------")
        print("---------  Gift Removed  ---------")
        print("----------------------------------")
        print()
        print(f"Successfully removed {gift[1]} from child's list.'")
        print()
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        print()
      except ValueError as err:
        print(f"Delete Error: {err}")
        print()

  # Checks if child exists and if not, adds to the database
  def checkChild(self, name):
    with sqlite3.connect(nice_list) as connectData:
        cursor = connectData.cursor()
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
            print()
            print(f"--- Created list for {name}.  ----")
            print("----------------------------------")
            print()
            cursor.execute(f'''SELECT *
                          FROM Children c
                          Where c.Name = '{name}'
                          ''')
            child_check = cursor.fetchone()
            return child_check
          return child_check
        except sqlite3.OperationalError as err:
          print("error", err)
          print()


  # Checks if a child exists in db by name
  def checkName(self, name):
    with sqlite3.connect(nice_list) as connectData:
        cursor = connectData.cursor()
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
  def checkGift(self, name, childId):
    with sqlite3.connect(nice_list) as connectData:
        cursor = connectData.cursor()
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


  # Get all children receiving gifts:
  def kidsGettingGifts(self):
    with sqlite3.connect(nice_list) as connectData:
        cursor = connectData.cursor()
        try:
          cursor.execute(f'''select c.Name as "Children Receiving Presents"
                              FROM Gifts g
                              Join Children c
                              On c.ChildId = g.ChildId
                              group by c.Name
                          ''')
          gift_check = cursor.fetchall()
          if len(gift_check) == 0:
            print(gift_check)
            print()
            print("--------------------------------------")
            print("-----  Children Receiving Gifts  -----")
            print("--------------------------------------")
            print()
            print("---  NO CHILDREN RECEIVING GIFTS  ----")
            print()
            print("-----------------------------------")
            print("-----------------------------------")
            print("-----------------------------------")
            print()
          else:
            print()
            print("----------------------------------")
            print("---  Children Receiving Gifts  ---")
            print("----------------------------------")
            print()
            gift_check = list(gift_check)
            for child in gift_check:
              tempName = list(child)
              print(tempName[0])
            print()
            print("-----------------------------------")
            print("-----------------------------------")
            print("-----------------------------------")
            print()
        except sqlite3.OperationalError as err:
          print("error", err)
          print()


  # Get all children receiving gifts:
  def indivKidGiftList(self, name):
    with sqlite3.connect(nice_list) as connectData:
        cursor = connectData.cursor()
        try:
          cursor.execute(f'''select g.Name as "Gifts"
                            FROM Children c
                            Join Gifts g
                            On c.ChildId = g.ChildId
                            where c.Name = '{name}'
                          ''')
          gift_check = cursor.fetchall()
          if len(gift_check) == 0:
            cursor.execute(f'''select *
                            FROM Children c
                            where c.Name = '{name}'
                          ''')
            name_exists = cursor.fetchall()
            if len(name_exists) == 0:
              print()
              print("**********************************")
              print("********  Database Alert  ********")
              print("**********************************")
              print()
              print(f"{name} is not in our database. Please add present for {name} and try again.")
              print()
              print("**********************************")
              print("**********************************")
              print("**********************************")
              print()
            else:
              print()
              print("-----------------------------------")
              print(f"--------- {name}'s Gifts ---------")
              print("-----------------------------------")
              print()
              print("-------  NO GIFTS FOR USER  -------")
              print()
              print("-----------------------------------")
              print("-----------------------------------")
              print("-----------------------------------")
              print()
          else:
            print()
            print("----------------------------------")
            print(f"-------- {name}'s Gifts --------")
            print("----------------------------------")
            print()
            gift_check = list(gift_check)
            for child in gift_check:
              tempName = list(child)
              print(tempName[0])
            print()
            print("-----------------------------------")
            print("-----------------------------------")
            print("-----------------------------------")
            print()
        except sqlite3.OperationalError as err:
          print("error", err)
          print()


  # Get all children receiving gifts:
  def deliverChildsGifts(self, child):
    childId = child[0]
    childName = child[1]
    with sqlite3.connect(nice_list) as connectData:
        cursor = connectData.cursor()
        try:
          cursor.execute(f'''select *
                            From Gifts g
                            where g.ChildId = {childId}
                          ''')
          gift_check = cursor.fetchall()
          if len(gift_check) == 0:
            print()
            print("**********************************")
            print("********  Delivery Alert  ********")
            print("**********************************")
            print()
            print(f"{childName} has no presents that are ready to deliver. Please add present and try again.")
            print()
            print("**********************************")
            print("**********************************")
            print("**********************************")
            print()
          elif gift_check[0][2] == 1:
            print()
            print("**********************************")
            print("********  Delivery Alert  ********")
            print("**********************************")
            print()
            print(f"{childName} has already had their presents delivered. Try again next year.")
            print()
            print("**********************************")
            print("**********************************")
            print("**********************************")
            print()
          else:
            print()
            print("-----------------------------------")
            print("-----  Delivery Confirmation  -----")
            print("-----------------------------------")
            print()
            print()
            print(f"-- Delivered {childName}'s Gifts--")
            for gift in gift_check:
              print(gift[1])
              cursor.execute(f'''UPDATE Gifts
                                SET Delivered = {1}
                                WHERE
                                GiftId = {int(gift[0])};
                            ''')
            print()
            print("-----------------------------------")
            print("-----------------------------------")
            print("-----------------------------------")
            print()
        except sqlite3.OperationalError as err:
          print("error", err)
          print()


  # Remove all gifts from naught kid:
  def naughtyList(self, child):
    name = child[1]
    childId = child[0]
    status = child[2]
    if status == "NAUGHTY":
      print()
      print("**********************************")
      print("********  Naughty Alert  ********")
      print("**********************************")
      print()
      print(f"{name} is already on the Naughty List.")
      print()
      print("**********************************")
      print("**********************************")
      print("**********************************")
      print()
    else:
      with sqlite3.connect(nice_list) as connectData:
          cursor = connectData.cursor()
          cursor.execute(f'''UPDATE Children
                                SET NaughtyOrNice = "NAUGHTY"
                                WHERE
                                ChildId = {childId};
                            ''')
          print()
          print("**********************************")
          print(f"**  {name} is now on Naughty List.**")
          print("**********************************")
          print()
          try:
            cursor.execute(f'''select *
                              From Gifts g
                              where g.ChildId = {childId}
                            ''')
            gift_check = cursor.fetchall()
            if len(gift_check) == 0:
              print(f"* {name} had no gifts on list.  *")
              print()
            else:
              for gift in gift_check:
                print(f"Removed {gift[1]} from list.")
                cursor.execute(f'''DELETE from Gifts
                          Where Gifts.GiftId = {gift[0]}
                        ''')
              print()
              print("**********************************")
            print("**********************************")
            print("**********************************")
            print()
          except sqlite3.OperationalError as err:
            print("error", err)
            print()

if __name__ == "__main__":
  handleInputs()