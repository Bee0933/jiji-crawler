install:
	# install dependencies
	pip install --upgrade pip &&\
		pip install -r requirements.txt 
format:
	# format python code with black
	black *.py db/*.py logic/*.py 
lint:
	# check code syntaxes
	pylint --disable=R,C *.py db/*.py logic/*.py 
