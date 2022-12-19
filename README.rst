Introduction
============
My solutions to `Advent of Code <https://adventofcode.com/>`_ in Python. Generally, I have only attempted to optimize code to minimize runtime if runtime was long (> 0.1s) in the first place.


Getting Started
===============

Prerequisites
-------------
You'll need Python 3.10 or above and `Poetry <https://python-poetry.org/>`_.

Installing
----------
The Python dependencies are specified in ``pyproject.toml``. To install, simply run:

.. code-block::

	poetry install --no-dev

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

	poetry run solve_puzzle --year 2022 --day=2 --part=1