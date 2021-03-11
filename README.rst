Advent of Code
==============
My solutions to `Advent of Code <https://adventofcode.com/>`_ in Python. Generally, I have attempted to write efficient code that minimizes runtime (sometimes at the cost of memory and code length).


Getting Started
===============

Prerequisites
-------------
You'll need Python 3.8 or above and `Poetry <https://python-poetry.org/>`_.

Installing
----------
The Python dependencies are specified in ``pyproject.toml``. To install, simply run:

.. code-block::

	poetry install --no-dev

Running the puzzles
-------------------

.. code-block::

	poetry run puzzle [OPTIONS]
	
	Options:
  		--year INTEGER		advent of code year. default 2020
		--day INTEGER		puzzle day. default 1
		--part INTEGER		part 1 or 2. Runs both if not specified

Example:

.. code-block::

	poetry run puzzle --day=2 --part=1