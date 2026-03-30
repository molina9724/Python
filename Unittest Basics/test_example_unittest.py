import unittest


class TestMath(unittest.TestCase):
    def test_add(self):
        """Test addition."""
        self.assertEqual(2 + 2, 4)

    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(5 - 3, 2)


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        """Test uppercasing a string."""
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        """Test isupper returns True only when all chars are uppercase."""
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        """Test splitting a string."""
        self.assertEqual("hello world".split(), ["hello", "world"])
        # check that it fails properly when separator is not a string
        with self.assertRaises(TypeError):
            "hello world".split(3)


# If run as a script: run unittest's CLI main
if __name__ == "__main__":
    unittest.main()
