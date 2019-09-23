.PHONY: lint test

lint:
	pylint *.py
test:
	python3 -m unittest tests/test_randomfact.py
