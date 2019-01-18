import unittest
import sqlite3
import sys
sys.path.append("../")
from lootbag import SantasBag

data_list = '/Users/braddavis/workspace/python/exercises/bagOfLoot/testing/data/testing.db'

class TestSantasBag(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.santa = SantasBag()
    with sqlite3.connect(data_list) as connectData:
        cursor = connectData.cursor()
        cursor.execute(
          'DELETE from Children'
        )
        cursor.execute(
          'DELETE from Gifts'
        )


  # Create instance of SantasBag test
  def test_instance_SantasBag(self):
    santa = SantasBag()
    print(f"Test of Class Creation: {self}")
    self.assertIsInstance(santa, SantasBag)


  # Check child exists and if not, create child
  def test_add_child(self):
    santa = SantasBag()
    temp = santa.checkChild("Brad")
    print(f"Test of Adding New Child: {temp}")
    self.assertEqual(temp, (1, "Brad", "NICE"))


  # Add gift test
  def test_add_gift(self):
    bob = SantasBag()
    bob.add_gift(1, "Piano", "NICE", "Brad")
    temp = bob.checkGift("Piano", 1)
    print(f"Test of Addding Gift to Child: {temp}")
    # self.assertEqual(bob, ["Piano", "Dress", "Make Up"] )


  # Removing gifts test
  # def test_remove_gift(self):
  #   bob = SantasBag()
  #   bob.add_gift("suzie", "piano", "dress", "make Up")
  #   bob.remove_gift("suzie", "dress")
  #   self.assertEqual(bob.gifts[0], ["Piano", "Make Up"])

  # Removing gifts test
  # def test_deliver_gifts(self):
  #   bob = SantasBag()
  #   bob.add_gift("suzie", "piano", "dress", "make Up")
  #   bob.deliver_gifts("suzie", 12, "Tuesday", 2018)
  #   print(bob.delivery_status)
    # self.assertEqual(bob.gifts[0], ["Piano", "Make Up"])



if __name__ == "__main__":
  unittest.main()