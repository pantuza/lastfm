Last Fm
=======

### Name

###### lastfm

### Description

        Lastfm API library writen in Python. It implements Lastfm API methods 
    as described in its [documentation](http://www.last.fm/api). 

### Usage

- Authentication

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

- Requests

###### Get an artist full information

```python
from lastfm.src.artist import Artist

# Creates an Artist object by its name
artist = Artist("the strokes")

# retrieves artist information
info = artist.get_info()
```

- Authenticated Requests

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

### Author

###### Written by Gustavo Pantuza

### Reporting Bugs

###### Report lastfm bugs to gustavopantuza@gmail.com
