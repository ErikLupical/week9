"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestSingletonCounter(unittest.TestCase):
    def test_singleton_instance(self):
        # Create two instances of Counter
        counter1 = Counter()
        counter2 = Counter()

        # Verify that they share the same instance
        self.assertIs(counter1, counter2)

    def test_increment_count(self):
        # Create an instance of Counter
        counter = Counter()

        # Increment the count
        counter.increment()

        # Verify that the count is updated
        self.assertEqual(counter.count, 1)

        # Create another instance (should still be the same singleton)
        another_counter = Counter()

        # Verify that the count is consistent across instances
        self.assertEqual(another_counter.count, 1)


if __name__ == "__main__":
    unittest.main()
