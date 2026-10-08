# PLP Python Week 3

This repository contains my Week 3 Python assignment.

## Files

- `grade_reporter.py` - Uses loops and conditional statements to calculate grades, pass/fail counts, and the average score.
- `bug_hunt.py` - Fixes three bugs in a Python program that calculates the sum of numbers from 1 to 5.

## Bug Hunt Reflection

The hardest bug to find was the condition in the while loop because the program could run without showing an error message. I knew something was wrong because the program printed the wrong answer instead of the required answer, 15. By checking the loop condition, I found that `count < 5` stopped the loop before the number 5 could be added, so I changed it to `count <= 5`.
