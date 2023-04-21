import unittest
from solution import open_or_senior
class TestOpenOrSenior(unittest.TestCase):
    
    def test_regular_members(self):
        # Test for regular members who do not qualify as seniors
        data = [[18, 20], [45, 2], [37, 6], [21, 21]]
        expected = ["Open", "Open", "Open", "Open"]
        self.assertEqual(open_or_senior(data), expected)
        
    def test_senior_members(self):
        # Test for senior members who qualify as seniors
        data = [[55, 8], [61, 12], [78, 9]]
        expected = ["Senior", "Senior", "Senior"]
        self.assertEqual(open_or_senior(data), expected)
        
    def test_all_members(self):
        # Test for all members in the input
        data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
        expected = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
        self.assertEqual(open_or_senior(data), expected)
        
if __name__ == '__main__':
    unittest.main()
