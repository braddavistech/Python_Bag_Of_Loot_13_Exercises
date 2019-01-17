import unittest
import sys
sys.path.append("../")
from lootbag import SantasBag

class TestSantasBag(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.santa = SantasBag()


  # Create instance of SantasBag test
  def test_instance_SantasBag(self):
    bob = SantasBag()
    self.assertIsInstance(bob, SantasBag)


  # Add gift test
  def test_add_gift(self):
    bob = SantasBag()
    bob.add_gift("suzie", "piano", "dress", "make Up")
    self.assertEqual(bob.gifts[0], ["Piano", "Dress", "Make Up"] )


  # Removing gifts test
  def test_remove_gift(self):
    bob = SantasBag()
    bob.add_gift("suzie", "piano", "dress", "make Up")
    bob.remove_gift("suzie", "dress")
    self.assertEqual(bob.gifts[0], ["Piano", "Make Up"])

  # Removing gifts test
  def test_deliver_gifts(self):
    bob = SantasBag()
    bob.add_gift("suzie", "piano", "dress", "make Up")
    bob.deliver_gifts("suzie", 12, "Tuesday", 2018)
    print(bob.delivery_status)
    # self.assertEqual(bob.gifts[0], ["Piano", "Make Up"])



if __name__ == "__main__":
  unittest.main()