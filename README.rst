Introduction
============
My solutions to `Advent of Code <https://adventofcode.com/>`_ in Python.
My goals are to find a time efficient solution for each puzzle, to learn new Python features, and to write clean code.
I have targeted to run each puzzle in under 100 ms. This is not always possible, but I try to optimize the solution as much as possible.



Getting Started
===============

Prerequisites
-------------
You'll need Python 3.12 or above and `Poetry <https://python-poetry.org/>`_.

Installing
----------
The Python dependencies are specified in ``pyproject.toml``. To install, simply run:

.. code-block::

	poetry install --no-dev

Downloading the puzzles
-------------------

.. code-block::

	poetry run download_puzzle [OPTIONS]
	
	Options:
  		--year INTEGER		advent of code year
		--day INTEGER		puzzle day. Downloads all if not specified

Example:

.. code-block::

	poetry run download_puzzle --year 2022 --day 2

Running the puzzles
-------------------

.. code-block::

	poetry run solve_puzzle [OPTIONS]
	
	Options:
  		--year INTEGER		advent of code year
		--day INTEGER		puzzle day. Runs all days if not specified
		--part INTEGER		part 1 or 2. Runs both if not specified

Example:

.. code-block::

	poetry run solve_puzzle --year 2022 --day 2 --part 1