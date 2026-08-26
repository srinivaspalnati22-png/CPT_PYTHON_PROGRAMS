"""
Comprehensive Test Runner for Problems 1 to 30
-----------------------------------------------
Executes test suites across all 30 problem modules.
"""

import sys
import subprocess
import glob
import os

def run_all_solutions():
    python_files = sorted(glob.glob("problem_*.py"))
    print(f"Discovered {len(python_files)} problem solution files.\n" + "=" * 60)
    
    passed = 0
    for file in python_files:
        print(f"Running: {file} ...", end=" ")
        result = subprocess.run([sys.executable, file], capture_output=True, text=True)
        if result.returncode == 0:
            print("PASSED [OK]")
            passed += 1
        else:
            print("FAILED [ERR]")
            print(result.stderr)
            
    print("=" * 60)
    print(f"Summary: {passed}/{len(python_files)} problems executed successfully.")

if __name__ == "__main__":
    run_all_solutions()
