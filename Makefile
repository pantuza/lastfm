#
# LAST FM LIBRARY Makefile
#

nose_options=--verbose --with-color

# run all tests
test:	
	@clear
	@nosetests tests/*.py ${nose_options}

# run the request tests
test_request:
	@clear
	@nosetests tests/request.py ${nose_options}

# run authentication tests
test_auth:
	@clear
	@nosetests tests/auth.py ${nose_options}

# run artist tests
test_artist:
	@clear
	@nosetests tests/artist.py ${nose_options}

# Run pep8 command line tool for every python file
pep8:
	@clear
	@find . -type f -name "*.py" -exec pep8 '{}' -v \;

# Run pylint into source files
pylint:
	@clear
	@pylint src/*.py --reports=no --include-ids=y

# Install project dependencies
deps: requirements.txt
	@clear
	@pip install -r requirements.txt
