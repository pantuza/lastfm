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


 
