Last Fm
=======

### Name

###### lastfm

### Description

> Lastfm API library written in Python. Implements Lastfm API methods 
> as described in its [documentation](http://www.last.fm/api)
> You can use this library for Web/Desktop aplications. All the requests
> are using JSON as response format, just because xml is boring :)
> enjoy the library!

### Usage

#### Authentication

###### Get user authentication

```python
from lastfm.src.auth import Auth

# Creates an Auth object not authenticated
auth = Auth()
# generate and returns the url tha you have redirect the 
# user to give permission to your application
auth_url = auth.get_auth_url()

# if the user user give permission to your application, you can
# retrieves his session key
session = auth.get_session()

# You should store this session variable. It will be used to 
# compose all the authenticated requests to the Last FM API
```

###### User already authenticated

```python
from lastfm.src.auth import Auth

# Creates an Auth object authenticated
stored_session = "19c246aa7ebf5d60ezdv6ae33d5c9d0x"
auth = Auth(stored_session)
```

#### Requests

###### Get an artist full information

```python
from lastfm.src.artist import Artist

# Creates an Artist object by its name
artist = Artist("the strokes")

# retrieves artist information
info = artist.get_info()
```

#### Authenticated Requests

###### Gets an Artist tags from user
```python
from lastfm.src.auth import Auth
from lastfm.src.artist import Artist

auth = Auth(stored_session)
artist = Artist("the strokes")

# every authenticated requests you should pass your Auth object 
# than the library makes the magic for you signing the request
tags = artist.get_tags(auth=auth)
```

### Development Status
        The current Library only implements the Artists methods from the
    Last FM API. It's under development, so if you want to contribute, fork me :)

### Contributions

        The library was written using Test Driven Development. If you want to 
    contribute, make shure your code pass on all tests and in the new tests that 
    you could create. 
        Read the DEPENDENCIES file to see wich test libs are used to validate 
    the code. 
        During the development, use the Makefile. Inside it, there are rules to 
    validate the python code with pep8 and pylint tools as well as test rules that
    will run tests for an especific module (artist, auth, etc).
        Create a file named secrets.py where you gonna put your session variable. It 
    will be used by the tests to run authenticated request: 
```python
# -*- coding: utf-8 -*-
mysession = "21c846aa7abf3c6fead46ae43d549dd0"
```
        If will be necessary to add new python libraries to the code, do not forget 
    to add it to requirements.txt file
        Enjoy coding \o/

### Author

###### Written by Gustavo Pantuza

### Reporting Bugs

###### Report lastfm bugs to gustavopantuza@gmail.com
