run:
	python3 main.py

dev: #ctrl c terminal to stop
	watchfiles "python3 main.py" .

install:
	pip3 install -r requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +

test:
	python3 -m pytest