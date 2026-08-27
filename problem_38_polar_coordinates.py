"""
Problem 38: Polar Coordinates
-----------------------------
You are given a complex number z. Your task is to convert it to polar coordinates.

Polar Coordinates (r, phi):
- r: Distance from origin to z (modulus): r = |z| = sqrt(x^2 + y^2)
- phi: Counterclockwise angle from the positive x-axis (phase/argument): phi = phase(z)

Input Format:
- A single line containing the complex number z.

Constraints:
- Given number is a valid complex number.

Output Format:
- Output two lines:
  - The first line should contain the value of r.
  - The second line should contain the value of phi (in radians).

Sample Input:
1+2j

Sample Output:
2.23606797749979
1.1071487177940904
"""

import sys
import cmath

def convert_to_polar(z_str: str) -> tuple[float, float]:
    """
    Complex to Polar Conversion:
    ----------------------------
    Using Python's built-in `cmath` library:
    - Modulus r: `abs(z)`
    - Phase angle phi: `cmath.phase(z)`
    - Or combined: `cmath.polar(z)` returns `(r, phi)`.

    Time Complexity: O(1) - Elementary arithmetic and trigonometric calculations.
    Space Complexity: O(1) - Constant auxiliary space.
    """
    z = complex(z_str)
    r = abs(z)
    phi = cmath.phase(z)
    return r, phi


def main():
    z_str = sys.stdin.read().strip()
    if z_str:
        r, phi = convert_to_polar(z_str)
        print(r)
        print(phi)


if __name__ == "__main__":
    sample_inputs = ["1+2j", "3+4j", "-1-1j"]
    for inp in sample_inputs:
        r, phi = convert_to_polar(inp)
        print(f"Complex Number: {inp}")
        print(f"  r   (modulus) = {r}")
        print(f"  phi (phase)   = {phi}\n")
