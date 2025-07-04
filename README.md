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

### Tests

The included tests verify that the sorting logic works as expected.


### Results

The sorting logic can be found in the `sort` function in the `sorter.py` file.

#### Package Distribution

| Stack    | Percentage | Number of Packages |
|:---|:---|:---|
| STANDARD | 53.57%     | 15                 |
| REJECTED | 35.71%     | 10                 |
| SPECIAL  | 10.71%     | 3                  |

#### Stack Statistics

| Stack | Mass (Mean) | Mass (Min) | Mass (Max) | Volume (Mean) | Volume (Min) | Volume (Max) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| REJECTED | 29.5 | 22.0 | 40.0 | 1812025.0 | 1000000.0 | 3375000.0 |
| SPECIAL | 22.0 | 20.0 | 26.0 | 897625.0 | 847875.0 | 990000.0 |
| STANDARD | 11.6 | 0.0 | 18.0 | 287875.0 | 24000.0 | 720000.0 |