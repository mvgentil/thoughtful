# Package Sorter

This script sorts packages into different stacks based on their dimensions and mass.

## Sorting Logic

The `sort` function categorizes packages as follows:

- **STANDARD**: Packages with dimensions less than 150 cm, volume less than 1,000,000 cm³, and mass less than 20 kg.
- **SPECIAL**: Packages that are either "bulky" (at least one dimension >= 150 cm or volume >= 1,000,000 cm³) or "heavy" (mass >= 20 kg), but not both.
- **REJECTED**: Packages that are both "bulky" and "heavy."

## Usage

Make sure you have Python 3 installed on your system.
To run the included tests, execute the script from your terminal:

```bash
python sorter.py
```

### Example

To use the `sort` function in your own code:

```python
from sorter import sort

# Dimensions (width, height, length) in cm and mass in kg
stack = sort(50, 50, 50, 5)
print(f"The package should be placed in the {stack} stack.")
# Output: The package should be placed in the STANDARD stack.
```
