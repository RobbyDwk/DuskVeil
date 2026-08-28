# test_duskveil.py
"""
Tests for DuskVeil module.
"""

import unittest
from duskveil import DuskVeil

class TestDuskVeil(unittest.TestCase):
    """Test cases for DuskVeil class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DuskVeil()
        self.assertIsInstance(instance, DuskVeil)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DuskVeil()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
