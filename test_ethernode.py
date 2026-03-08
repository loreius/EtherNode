# test_ethernode.py
"""
Tests for EtherNode module.
"""

import unittest
from ethernode import EtherNode

class TestEtherNode(unittest.TestCase):
    """Test cases for EtherNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherNode()
        self.assertIsInstance(instance, EtherNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
