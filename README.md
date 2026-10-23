# ISM3232 Midterm: Cloudstep Software

- **Name:** Juan Poveda
- **Version:** EPSILON
- **Date:** October 24, 2026

## What This Program Does

This program figures out how much each customer owes for Cloudstep Software's scheduling app, which is sold by the seat. For every order it calculates the license total with any discount and onboarding fee, and it checks whether the order needs a contract review or gets a dedicated trainer. When you run main.py, it prints a report with one line per order, then a summary with the total, the average, the biggest order, and how many reviews and trainers are needed.

## Business Rules

1. The license cost is just the price per seat times the number of seats.
2. Orders under 10 seats get no discount, 10 to 49 seats get 7% off, and 50 or more seats can get 16% off.
3. Only education customers get the 16% discount, so any other order with 50 or more seats still gets 7%.
4. If the cost after the discount is $400 or less, a $60 onboarding fee gets added.
5. Any license total over $5,000 has to go through a contract review.
6. A customer gets a dedicated trainer if they buy 25 or more seats or their license total is over $3,000.

## How to Run

Clone the repo, set up a virtual environment, install the requirements, and run the program:

cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

## How to Test

With the virtual environment active, run ruff to format and check the code, then run pytest:

ruff format .
ruff check .
pytest -v

## Files in This Repository

- business_rules.py: the eight functions that apply Cloudstep's six business rules, with the rule numbers stored as named constants at the top
- main.py: the list of eight orders, plus the code that prints the order report and the summary lines
- commands.md: my terminal record showing the commands I ran to build and check the project, with their output
- README.md: this file, which explains what the program does and how to run and test it
- requirements.txt: the packages the virtual environment needs (pytest and ruff), made with pip freeze
- .gitignore: tells Git to keep .venv/ and __pycache__/ out of the repository
- tests/__init__.py: an empty file that marks the tests folder as a package so pytest can find the code
- tests/test_business_rules.py: the 24 pytest tests that check every function and both sides of every limit in the rules

## AI Use Statement

I did not use AI for this midterm.