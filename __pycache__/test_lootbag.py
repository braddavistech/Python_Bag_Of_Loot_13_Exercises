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
    print()


  # Check child exists and if not, create child
  def test_add_child(self):
    santa = SantasBag()
    temp = santa.checkChild("Brad")
    print(f"Test of Adding New Child: {temp}")
    self.assertEqual(temp, (1, "Brad", "NICE"))
    print()


  # Add gift test
  def test_add_gift(self):
    santa = SantasBag()
    temp = santa.checkChild("Tom")
    santa.add_gift(1,"Piano", "NICE", "Brad")
    santa.add_gift(2, "Bear", "NICE", "Tom")
    temp = santa.checkGift("Bear", 2)
    print(f"Test of Addding Gift to Child: {temp}")
    self.assertEqual(temp, (2, "Bear", 0, 2, 2, "Tom", "NICE"))
    print()


  # Removing gifts test
  def test_remove_gift(self):
    santa = SantasBag()
    temp = santa.checkGift("Piano", 1)
    self.assertNotEqual(temp, None)
    santa.remove_gift([1, "Piano"])
    temp = santa.checkGift("Piano", 1)
    print(f"Test of Removing Gift from child: {temp}")
    self.assertEqual(temp, None)
    print()

  # Check name exists
  def test_check_name(self):
    bob = SantasBag()
    temp = bob.checkName("Brad")
    print(f"Test of name exists: {temp}")
    self.assertEqual(temp, (1, "Brad", "NICE"))
    self.assertNotEqual(temp, (2, "Brad", "NICE"))
    print()



if __name__ == "__main__":
  unittest.main()