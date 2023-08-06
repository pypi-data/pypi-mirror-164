# deceit

## introduction

boilerplate requests code for creating simple api clients.  includes
a standard requests retry adapter for retrying errors 429, 502, 503, and 504,
and a base api exceptions class that can be used for api-specific error 
handling.  includes hooks that can be used to add request and response 
logging to a database if needed for debugging / traceability.

named after a group of lapwings.  pax avium.

## usage

```python
from deceit.api_client import ApiClient
from deceit.exceptions import ApiException


class AirflowException(ApiException):
    pass

class AirflowApiClient(ApiClient):
    def __init__(self, *args, default_timeout=None, **kwargs):
        super().__init__(
            *args, base_url='http://localhost:8080/api/v1',
            default_timeout=default_timeout,
            exception_class=AirflowException,
            **kwargs)
        self.session.auth = ('username', 'password')

    def connections(self):
        return self.get('connections')
        
```

## contributing

### prerequisites

* python3.9 or python3.10
* docker-compose
* internet connection

### getting started

standard avian setup using `make`

```bash
cd /path/to/deceit
make setup
make test
```
