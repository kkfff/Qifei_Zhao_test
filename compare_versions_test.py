
# coding: utf-8

# In[3]:


import unittest
from compare_versions import greater_than

class TestCompVersions(unittest.TestCase):
    def test_values(self):
        # ensure exceptions are raised appropriately on invalid arguments
        self.assertRaises(ValueError, greater_than, ".2.7", "1.4.0")
        self.assertRaises(ValueError, greater_than, "1.2.a7", "1.4.0")
        self.assertRaises(ValueError, greater_than, "1.2/7", "1.4.0")
        
        self.assertRaises(ValueError, greater_than, "1.2.7", ".4.0")
        self.assertRaises(ValueError, greater_than, "1.2.7", "1.4p.0")
        self.assertRaises(ValueError, greater_than, "1.2.7", "1?4.0")
        
    def test_compare(self):
        # ensure version strings are correctly compared
        # the cases where the first version is the same as the second
        self.assertAlmostEqual(greater_than("1.0.5", "1.0.5"), 0)
        self.assertAlmostEqual(greater_than("3.7", "3.7"), 0)
        self.assertAlmostEqual(greater_than("2.6.5.3", "2.6.5.3"), 0)
        
        # the cases where the first version is greater than the second
        self.assertAlmostEqual(greater_than("1.0.5", "1.0.3"), 1)
        self.assertAlmostEqual(greater_than("3.2.5", "1.2.3"), 1)
        self.assertAlmostEqual(greater_than("3.5.3", "3.4.3"), 1)
        self.assertAlmostEqual(greater_than("1.5", "1.2.4"), 1)
        self.assertAlmostEqual(greater_than("2.4.5", "2.2"), 1)
        
        # the cases where the second version is greater than the first
        # just switch the first argument with the second argument on the above cases
        self.assertAlmostEqual(greater_than("1.0.3", "1.0.5"), -1)
        self.assertAlmostEqual(greater_than("1.2.3", "3.2.5"), -1)
        self.assertAlmostEqual(greater_than("3.4.3", "3.5.3"), -1)
        self.assertAlmostEqual(greater_than("1.2.4", "1.5"), -1)
        self.assertAlmostEqual(greater_than("2.2", "2.4.5"), -1)
        

