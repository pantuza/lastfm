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

# run album tests
test_album:
	@clear
	@nosetests tests/album.py ${nose_options}

# run chart tests
test_chart:
	@clear
	@nosetests tests/chart.py ${nose_options}

# run event tests
test_event:
	@clear
	@nosetests tests/event.py ${nose_options}
	
# run geo tests
test_geo:
	@clear
	@nosetests tests/geo.py ${nose_options}

# Run pep8 command line tool for every python file
pep8:
	@clear
	@find . -type f -name "*.py" -exec pep8 '{}' -v \;

# Run pylint into source files
pylint:
	@clear
	@pylint ./{src,tests} --rcfile=pylint.rc

# Run pylint rule with reports on
report:
	@clear
	@pylint src --rcfile=pylint.rc --reports=y | more

# Install project dependencies
deps: requirements.txt
	@clear
	@pip install -r requirements.txt
