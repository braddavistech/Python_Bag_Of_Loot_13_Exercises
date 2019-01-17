from lootbag import SantasBag
import sys
import sqlite3

print(sys.argv)

nice_list = '/Users/braddavis/workspace/python/exercises/bagOfLoot/testing/data/nice_list.db'

def handleInputs():
  print(sys.argv[1])
  santa = SantasBag()
  




def getDataFunc():
  with sqlite3.connect(nice_list) as conn:
    cursor = conn.cursor()
  gift_list = cursor.execute('SELECT * FROM Gifts')
  gift_list = cursor.fetchall()
  print(gift_list)

if __name__ == "__main__":
  handleInputs()
