"""
Problem 33: Finding the Percentage
-----------------------------------
The provided code stub will read in a dictionary containing key/value pairs of
name:[marks] for a list of students. Print the average of the marks array for
the student name provided, showing 2 places after the decimal.

Input Format:
- The first line contains the integer N, the number of students' records.
- The next N lines contain the names and marks obtained by a student, each value separated by a space.
- The final line contains query_name, the name of a student to query.

Constraints:
- 2 <= N <= 10
- 0 <= marks[i] <= 100
- Length of marks arrays = 3

Output Format:
- Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0:
56.00

Sample Input 1:
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample Output 1:
26.50
"""

import sys

def calculate_student_average(student_marks: dict[str, list[float]], query_name: str) -> str:
    """
    Computes the arithmetic mean of marks for a query student and formats to 2 decimal places.

    Approach:
    ---------
    1. Retrieve the list of marks corresponding to `query_name` from the hash map (dict).
    2. Sum the scores and divide by the length of the list.
    3. Format the result string to exactly 2 decimal places using format specifier {:.2f}.

    Time Complexity: O(K) where K is the number of marks (here K = 3, so O(1)).
    Space Complexity: O(1) auxiliary space.
    """
    scores = student_marks[query_name]
    avg = sum(scores) / len(scores)
    return f"{avg:.2f}"


def main():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    
    n = int(input_lines[0].strip())
    student_marks = {}
    
    for i in range(1, n + 1):
        parts = input_lines[i].split()
        name = parts[0]
        scores = list(map(float, parts[1:]))
        student_marks[name] = scores
        
    query_name = input_lines[n + 1].strip()
    print(calculate_student_average(student_marks, query_name))


if __name__ == "__main__":
    records = {
        "Krishna": [67.0, 68.0, 69.0],
        "Arjun": [70.0, 98.0, 63.0],
        "Malika": [52.0, 56.0, 60.0]
    }
    query = "Malika"
    result = calculate_student_average(records, query)
    print(f"Average for '{query}': {result}")

    records_2 = {
        "Harsh": [25.0, 26.5, 28.0],
        "Anurag": [26.0, 28.0, 30.0]
    }
    query_2 = "Harsh"
    result_2 = calculate_student_average(records_2, query_2)
    print(f"Average for '{query_2}': {result_2}")
