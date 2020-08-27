# Cubing algs

A flexible database for speedsolving algorithms.

## What does it do?

It stores and displays as many algorithms, for as many cases, for as many
algorithm sets, for as many cubes as you want.

## How to install

1. Create a Python virtual environment with `python3 -m venv ${environmen_name}`
2. Clone this repository inside the virtual environment
3. Activate the virtual environment with `source bin/activate`
4. Install required dependencies with `pip install -r requirements.txt`
5. Initialise the database with `python manage.py migrate`
6. Run the development server with `python manage.py runserver`
7. The server should run on port 8000 by default

## How to add puzzles/algorithm sets/cases/algorithms

1. Create a superuser with `python manage.py createsuperuser`
2. Log in to the administrator interface on `127.0.0.1:8000/admin`
