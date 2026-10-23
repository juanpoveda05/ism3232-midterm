## Terminal Record: Cloudstep Software

## 1. Building the project

Juans-Laptop% history 1
  cd ~/ism3232-midterm
  cd ism3232-midterm
  pwd
  git init
  git branch -m main
  python3 -m venv .venv
  source .venv/bin/activate
  pip install pytest ruff
  pwd
  pip freeze > requirements.txt
  touch business_rules.py main.py commands.md README.md
  mkdir tests
  touch tests/__init__.py tests/test_business_rules.py
  printf ".venv\n__pycache__/|n" > .gitignore
  ls -a
  ls tests
  git status
  printf ".venv/\n__pycache__/\n" > .gitignore
  cat .gitignore
  git add .
  git commit -m "Start midterm: project structure, venv, gitignore"
  git remote add origin https://github.com/juanpoveda05/ism3232-midterm.git
  git push -u origin main
  python3 business_rules.py
  ruff check .
  python -c "from business_rules import *; print(calculate_license_total(35, 12, True))"
  git add business_rules.py
  git commit -m "Add business rules functions"
  git push


## 2. The virtual environment

/mnt/c/Users/juanp/ism3232-midterm/.venv/bin/python3

The path points to the python3 inside the project's .venv/bin folder instead of the system Python, which shows the virtual environment is active.

## 3. The project structure

(.venv) Juans-Laptop% tree -L 2
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

  The __pycache__/ folder is on my computer but not in my GitHub repository, because .gitignore tells Git to ignore it and it holds compiled files that Python rebuilds automatically.

## 4. Every function and test

(.venv) Juans-Laptop% rg 'def'
business_rules.py
15:def calculate_license_cost(seat_price: float, seats: int) -> float:
20:def get_seat_discount(seats: int, education: bool = False) -> float:
29:def calculate_license_total(
41:def needs_contract_review(total: float) -> bool:
46:def gets_trainer(seats: int, total: float) -> bool:
51:def total_licensed(orders: list) -> float:
61:def largest_license(orders: list) -> str:
75:def format_license_line(

main.py
24:def main() -> None:

tests/test_business_rules.py
14:def test_license_cost_is_price_times_seats():
19:def test_discount_is_zero_at_9_seats():
23:def test_discount_is_7_percent_at_10_seats():
28:def test_discount_is_7_percent_at_49_seats_education():
32:def test_discount_is_16_percent_at_50_seats_education():
37:def test_discount_is_7_percent_at_50_seats_not_education():
41:def test_education_changes_license_total():
47:def test_fee_added_when_discounted_cost_is_exactly_400():
51:def test_no_fee_when_discounted_cost_is_400_01():
55:def test_license_total_applies_7_percent_discount():
60:def test_no_contract_review_at_exactly_5000():
64:def test_contract_review_at_5000_01():
69:def test_trainer_at_25_seats_with_low_total():
73:def test_no_trainer_at_24_seats_with_low_total():
78:def test_no_trainer_at_exactly_3000_with_few_seats():
82:def test_trainer_at_3000_01_with_few_seats():
87:def test_total_licensed_adds_two_orders():
95:def test_total_licensed_empty_list_is_zero():
100:def test_largest_license_finds_biggest_order():
108:def test_largest_license_tie_returns_first():
116:def test_largest_license_empty_list_returns_empty_string():
121:def test_format_line_with_no_and_no():
126:def test_format_line_with_yes_and_yes():
131:def test_format_line_shows_two_decimal_places():

business_rules.py defines 8 functions and tests/test_business_rules.py defines 24 tests.

## 5. Which files print

(.venv) Juans-Laptop% rg -l 'print'
main.py
commands.md

main.py is the only Python file that prints (commands.md is listed only because it contains the word "print" in this section), and business_rules.py is not in the list because its functions return values and leave the printing to main.py.


## 6. The commit history

(.venv) Juans-Laptop% git log --oneline
3e908f3 (HEAD -> main, origin/main) Add tests and update requirements
1a8776c Fix module docstring
7aab6a1 Start terminal record
129ff09 Add main.py order report
820ef9e Add business rules functions
9df0486 Start midterm: project structure, venv, gitignore

At this point there were 6 commits.