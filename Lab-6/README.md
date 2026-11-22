# SE Lab 6 - Code and Branch Coverage (shopping cart)

Student: Dhruv Rajagopalan, PES1UG24AM086, Section B.

`shopping_cart.py` and the starter `test_shopping_cart.py` are the assigned lab files, copied unchanged from
https://github.com/SETAPESU26/L6_L7_23_shopping_cart (folder "Lab 6"). That repo has no license file; all rights to those two files stay with the course/instructor.

Added in this repo:
- `CodeCoverageTest_shopping_cart_application.py` - tests for code (line) coverage
- `BranchCoverageTest_shopping_cart_application.py` - tests for branch coverage
- terminal screenshots of the coverage runs

Run:
    pip install coverage pytest
    coverage run -m pytest CodeCoverageTest_shopping_cart_application.py && coverage report -m
    coverage run --branch -m pytest BranchCoverageTest_shopping_cart_application.py && coverage report -m
