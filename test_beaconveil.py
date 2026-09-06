# test_beaconveil.py
"""
Tests for BeaconVeil module.
"""

import unittest
from beaconveil import BeaconVeil

class TestBeaconVeil(unittest.TestCase):
    """Test cases for BeaconVeil class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BeaconVeil()
        self.assertIsInstance(instance, BeaconVeil)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BeaconVeil()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
