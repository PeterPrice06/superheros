venv:
	python3 -m venv .venv

install:
	pip install -r requirements
	kaggle datasets download -d claudiodavi/superhero-set -p data/

