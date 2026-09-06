# test_veilcompass.py
"""
Tests for VeilCompass module.
"""

import unittest
from veilcompass import VeilCompass

class TestVeilCompass(unittest.TestCase):
    """Test cases for VeilCompass class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VeilCompass()
        self.assertIsInstance(instance, VeilCompass)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VeilCompass()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
