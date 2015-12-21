import unittest

def answer(x):
  potential_size = 0
  for step in range(0, x+1):
    potential_size += 7**step
  return potential_size

class TestMinionMethods(unittest.TestCase):

  def test_one(self):
    self.assertEqual(answer(1), 8)
  def test_two(self):
    self.assertEqual(answer(2), 57)
  def test_three(self):
    self.assertEqual(answer(3), 400)

if __name__ == "__main__":
  unittest.main()

