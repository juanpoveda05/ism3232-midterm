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



## 3. The project structure

## 4. Every function and test

## 5. Which files print

## 6. The commit history