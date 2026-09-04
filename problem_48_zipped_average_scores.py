"""
Problem 48: Zipped! (Student Average Scores)
--------------------------------------------
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student across all subjects.

Average Score for a student = (Sum of scores obtained in all X subjects by that student) / X

Input Format:
- The first line contains N and X separated by a space (N: students, X: subjects).
- The next X lines contain the space separated marks obtained by students in a particular subject.

Output Format:
- Print the averages of all students on separate lines.
- The averages must be correct up to 1 decimal place.

Sample Input:
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

Sample Output:
90.0
91.0
82.0
90.0
85.5
"""

import sys


def compute_student_averages(n: int, x: int, subject_scores: list[list[float]]) -> list[float]:
    """
    Computes average score for each student using Python's `zip(*matrix)` transpose.

    Approach:
    ---------
    - `subject_scores` is an X x N matrix where each row represents marks in one subject.
    - `zip(*subject_scores)` yields N tuples, where the i-th tuple contains all X marks for student i.
    - The average for each student is `sum(student_marks) / X`.

    Time Complexity:
    ----------------
    - O(N * X): Traverses all scores once.

    Space Complexity:
    -----------------
    - O(N): Stores the resulting averages.
    """
    student_scores = zip(*subject_scores)
    averages = [sum(scores) / x for scores in student_scores]
    return averages


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n, x = map(int, lines[0].split())
    subject_scores = [list(map(float, lines[1 + i].split())) for i in range(x)]
    averages = compute_student_averages(n, x, subject_scores)
    for avg in averages:
        print(f"{avg:.1f}")


if __name__ == "__main__":
    n, x = 5, 3
    sample_scores = [
        [89.0, 90.0, 78.0, 93.0, 80.0],
        [90.0, 91.0, 85.0, 88.0, 86.0],
        [91.0, 92.0, 83.0, 89.0, 90.5],
    ]
    expected_avgs = [90.0, 91.0, 82.0, 90.0, 85.5]
    result_avgs = compute_student_averages(n, x, sample_scores)
    print(f"Students: {n}, Subjects: {x}")
    for i, avg in enumerate(result_avgs, 1):
        print(f"Student {i} Average: {avg:.1f}")
        assert round(avg, 1) == expected_avgs[i - 1], f"Mismatch for student {i}"
    print("All average score tests passed successfully!")
