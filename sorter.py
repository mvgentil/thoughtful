import unittest

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts a package into a stack based on its volume and mass.

    Args:
        width (float): The width of the item (cm).
        height (float): The height of the item (cm).
        length (float): The length of the item (cm).
        mass (float): The mass of the item (kg).

    Returns:
        str: The name of the stack the item should be placed in.
    """
    MAX_DIMENSION = 150.0
    MAX_VOLUME = 1_000_000.0
    MAX_MASS = 20.0

    volume = width * height * length

    is_bulky = (
        volume >= MAX_VOLUME or
        width >= MAX_DIMENSION or
        height >= MAX_DIMENSION or
        length >= MAX_DIMENSION or
        mass >= MAX_MASS
    )

    is_heavy = mass >= MAX_MASS

    if is_bulky and is_heavy:
        stack = "REJECTED"
    elif is_bulky or is_heavy:
        stack = "SPECIAL"
    else:
        stack = "STANDARD"

    return stack

class TestSorter(unittest.TestCase):
    def test_standard_package(self):
        """Test cases for standard packages."""
        self.assertEqual(sort(50, 50, 50, 5), "STANDARD")
        self.assertEqual(sort(100, 100, 99, 19.9), "STANDARD")

    def test_bulky_package(self):
        """Test cases for bulky packages."""
        self.assertEqual(sort(200, 50, 50, 5), "SPECIAL")
        self.assertEqual(sort(50, 200, 50, 5), "SPECIAL")
        self.assertEqual(sort(50, 50, 200, 5), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 5_000_000), "REJECTED")

    def test_heavy_package(self):
        """Test cases for heavy packages."""
        self.assertEqual(sort(50, 50, 50, 25), "REJECTED")
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED")

    def test_rejected_package(self):
        """Test cases for rejected packages."""
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")


if __name__ == "__main__":
    print("Running tests...")
    unittest.main(verbosity=2)