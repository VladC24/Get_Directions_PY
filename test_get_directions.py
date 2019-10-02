import unittest

target = __import__("get_directions")
get_directions =  target.get_directions

class TestGetDirections(unittest.TestCase):

    def test_get_directions(self):
        arguments = ["get_directions.py", "London", "Brighton"]

        self.assertEqual(get_directions(arguments), "https://www.google.co.uk/maps/dir/London/Brighton/")

    def test_error_message(self):
        arguments = ["get_directions.py"]

        self.assertEqual(get_directions(arguments), "Error: Number of locations should be greater than 1 and less than 11")

if __name__ == '__main__':
    unittest.main()