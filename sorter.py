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
    # Validate input types
    if not all(isinstance(x, (int, float)) for x in [width, height, length, mass]):
        raise TypeError("All dimensions and mass must be numeric values.")
    # Validate input values
    if any(x < 0 for x in [width, height, length, mass]):
        raise ValueError("Dimensions and mass must be non-negative.")

    # Constants for sorting criteria
    MAX_DIMENSION = 150.0
    MAX_VOLUME = 1_000_000.0
    MAX_MASS = 20.0

    volume = width * height * length

    is_bulky = (
        volume >= MAX_VOLUME or
        width >= MAX_DIMENSION or
        height >= MAX_DIMENSION or
        length >= MAX_DIMENSION
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
        self.assertEqual(sort(100, 100, 90, 19.9), "STANDARD")

    def test_special_bulky_by_volume(self):
        """Test cases for bulky packages by volume."""
        self.assertEqual(sort(100, 100, 100, 5), "SPECIAL")
        self.assertEqual(sort(140, 120, 120, 19), "SPECIAL")

    def test_special_bulky_by_dimension(self):
        """Test cases for bulky packages by dimension."""
        self.assertEqual(sort(200, 50, 50, 5), "SPECIAL")
        self.assertEqual(sort(50, 200, 50, 5), "SPECIAL")
        self.assertEqual(sort(50, 50, 150, 5), "SPECIAL")
        self.assertEqual(sort(40, 160, 40, 19), "SPECIAL")

    def test_special_heavy_package(self):
        """Test cases for heavy packages."""
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
        self.assertEqual(sort(100, 100, 80, 20), "SPECIAL")

    def test_rejected_package(self):
        """Test cases for rejected packages."""
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")
        self.assertEqual(sort(160, 160, 160, 30), "REJECTED")

    def test_invalid_input(self):
        """Test cases for invalid inputs."""
        with self.assertRaises(TypeError):
            sort("100", 50, 50, 5)
        with self.assertRaises(TypeError):
            sort(100, "50", 50, 5)
        with self.assertRaises(TypeError):
            sort(100, 50, "50", 5)
        with self.assertRaises(TypeError):
            sort(100, 50, 50, "5")
    
    def test_negative_input(self):
        """Test cases for negative inputs."""
        with self.assertRaises(ValueError):
            sort(-100, 50, 50, 5)
        with self.assertRaises(ValueError):
            sort(100, -50, 50, 5)
        with self.assertRaises(ValueError):
            sort(100, 50, -50, 5)
        with self.assertRaises(ValueError):
            sort(100, 50, 50, -5)


if __name__ == "__main__":
    print("Running tests...")
    unittest.main(verbosity=2)