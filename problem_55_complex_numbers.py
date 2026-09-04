"""
Problem 55: Complex Numbers Operations & Class Representation
--------------------------------------------------------------
You are given two complex numbers, and you have to print the result of their
addition, subtraction, multiplication, division and modulus operations.
The real and imaginary parts should be formatted to two decimal places.

Input Format:
- Two lines of input, each containing the real and imaginary part separated by a space.

Output Format:
- C + D
- C - D
- C * D
- C / D
- mod(C)
- mod(D)

Formatting rules:
- Format: A+Bi or A-Bi (where '+' is replaced with '-' when B < 0).
- Pure real numbers (zero imaginary part): A+0.00i
- Pure imaginary numbers (zero real part): 0.00+Bi

Sample Input:
2 1
5 6

Sample Output:
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
"""

import math
import sys


class ComplexNumber:
    """
    Custom complex number class implementing arithmetic and modulus operations.
    """

    def __init__(self, real: float, imag: float):
        self.real = float(real)
        self.imag = float(imag)

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return ComplexNumber(r, i)

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        # (a + bi) / (c + di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
        denom = other.real**2 + other.imag**2
        r = (self.real * other.real + self.imag * other.imag) / denom
        i = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(r, i)

    def mod(self) -> "ComplexNumber":
        magnitude = math.hypot(self.real, self.imag)
        return ComplexNumber(magnitude, 0.0)

    def __str__(self) -> str:
        r = 0.0 if abs(self.real) < 1e-9 else self.real
        i = 0.0 if abs(self.imag) < 1e-9 else self.imag
        sign = "+" if i >= 0 else "-"
        return f"{r:.2f}{sign}{abs(i):.2f}i"


def compute_complex_operations(c: ComplexNumber, d: ComplexNumber) -> list[str]:
    """Computes and formats all 6 requested operations."""
    return [
        str(c + d),
        str(c - d),
        str(c * d),
        str(c / d),
        str(c.mod()),
        str(d.mod()),
    ]


def main():
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        r1, i1 = map(float, lines[0].split())
        r2, i2 = map(float, lines[1].split())
        c = ComplexNumber(r1, i1)
        d = ComplexNumber(r2, i2)
        results = compute_complex_operations(c, d)
        for res in results:
            print(res)


if __name__ == "__main__":
    c = ComplexNumber(2, 1)
    d = ComplexNumber(5, 6)
    expected = [
        "7.00+7.00i",
        "-3.00-5.00i",
        "4.00+17.00i",
        "0.26-0.11i",
        "2.24+0.00i",
        "7.81+0.00i",
    ]
    results = compute_complex_operations(c, d)
    print("Complex Operations Output:")
    for res in results:
        print(res)
    assert results == expected, f"Mismatch: expected {expected}, got {results}"
    print("Complex numbers operations test passed successfully!")
