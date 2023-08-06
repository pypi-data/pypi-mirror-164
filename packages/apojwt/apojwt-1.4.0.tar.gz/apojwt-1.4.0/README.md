# ApoJWT
The `apojwt` Package was created with the intention of providing JWT support to In10t's Apogee Microservices. These services require a hierarchy of permissions that vary arcross all endpoints. As such, this package aims to provide decorators that can be attached with route declarations to ensure a valid JWT with proper permissions is being sent in the request headers. The package is inteded to be used alongside an API framework such as Flask or FastAPI.

---


## ApoJWT Class
The ApoJWT class has the following constructor:
```python
ApoJWT(secret: str, iss: str, admin_audience="admin", algorithm="HS256", asynch: bool=False, token_finder=None, permission_formatter=None)
"""
secret: Secret string used to encode and decode the JWT

iss: Issuer string used for additional security

admin_audience: The name of the audience with admin access. Default admin

algorithm: The algorithm to use when encoding/decoding. Default HS256

asynch: Tells ApoJWT to use async decorators instead of the normal (FastAPI needs this True)

token_finder: First-order function used to retrive the JWT from the http request. Default None

permission_formatter: String formatting first-order function that is given permission_name as an argument
    Can be used to format request data in the permission name
"""
```
### Token Finder and Permission Formatter
The token_finder function must be passed to the higher order constructor for token validations to succeed. The permission_formatter is completely optional, but can be used to add additional information to permissions that may only be found in the request body. The functions are executed by this package in the following manner:
```python
token_finder(*args, **kwargs)
permission_formatter(permission_name, *args, **kwargs)
```
where `args` and `kwargs` are the parameters passed to an endpoint declaration.

***Examples***
```python
"""Token Finder: used to locate and return the JWT"""
# FastAPI
token_finder = lambda **kwargs: str(kwargs["authorization"]).replace("Bearer ", "")
ajwt = ("secret", iss="issuer", asynch=True, token_finder=token_finder)
## NOTE: asynch is True for FastAPI

# Flask
token_finder = lambda: request.headers["authorization"].replace("Bearer ", "")
ajwt = ("secret", iss="issuer", token_finder=token_finder)
## NOTE: asynch defaults to False for Flask


"""Permission Formatter: used to apply additional formatting to permission"""
# Example: Append the trial_id found in the request
# FastAPI
def fastapi_permission_formatter(permission_name, *args, **kwargs):
    if "trial_id" in kwargs.keys():
        return f"{permission_name}:{kwargs['trial_id']}"
ajwt = ("secret", iss="issuer", asynch=True, token_finder=..., permission_formatter=fastapi_permission_formatter)

# Flask
def flask_permission_formatter(permission_name):
    if "trial_id" in request.args.keys():
        return f"{permission_name}:{request.args['trial_id']}"
    elif "trial_id" in request.json.keys():
        return f"{permission_name}:{request.json['trial_id']}"
ajwt = ("secret", iss="issuer", asynch=False, token_finder=..., permission_formatter=flask_permission_formatter)
```


### Decorators
Decorators are the main use case of the ApoJWT package. They allow any endpoint to be secured with a single simple line of code
```python
ajwt = ApoJWT(secret, iss, asynch=..., token_finder=lambda: ..., permission_formatter=lambda perm: ...)


@ajwt.token_required
"""Validates JWT"""

@ajwt.permission_required(permission_name: str)
"""Validates JWT and ensures permission_name is among the audience (aud)

permission_name: a permission string
"""
```

### Functions
```python
ajwt = ApoJWT(secret, iss, asynch=..., token_finder=...)

ajwt.create_token(exp: int, aud: list[str]) -> str:
"""Encodes a jwt token with the given secret

exp: Expiration epoch time (as a numeric) of the token
aud: List of permissions (audiences) to assign to the token

JWT will contain the following claims:
    - exp: Expiration Time
    - nbf: Not Before Time
    - iss: Issuer
    - aud: Audience
    - iat: Issued At
"""

ajwt.token_data():
"""Retrieves the additional data stored in the JWT payload"""
```
---
## Usage Examples
### Constructing ApoJWT
```python
"""Token Finder: used to locate and return the JWT"""
# FastAPI
def fastapi_permission_formatter(permission_name, *args, **kwargs):
    if "trial_id" in kwargs.keys():
        return f"{permission_name}:{kwargs['trial_id']}"

fastapi_token_finder = lambda **kwargs: str(kwargs["authorization"]).replace("Bearer ", "")
ajwt = (
    "secret", 
    iss="issuer", 
    asynch=True
    token_finder=fastapi_token_finder
    permission_formatter=fastapi_permission_formatter
)
## NOTE: asynch must be True for FastAPI

# Flask
def flask_permission_formatter(permission_name):
    if "trial_id" in request.args.keys():
        return f"{permission_name}:{request.args['trial_id']}"
    elif "trial_id" in request.json.keys():
        return f"{permission_name}:{request.json['trial_id']}"

flask_token_finder = lambda: request.headers["authorization"].replace("Bearer ", "")
ajwt = (
    "secret", 
    iss="issuer",
    token_finder=flask_token_finder
    permission_formatter=flask_permission_formatter
)
## NOTE: asynch defaults to False

```

### Validating JWT with Decorators
```python
# fast api
@app.get("/some/endpoint")
@ajwt.permission_required("some:permission:name"):
...

# flask
@app.route("/some/endpoint", methods=["GET"])
@ajwt.permission_required("some:permission:name"):
...
```

### Creating a New JWT
```python
"""aud is a list of permissions (audiences) that will be assigned to the new token"""

aud = ["some:permission:name", ...]
exp = exp=datetime.now().timestamp() + timedelta(hours=1)
data = dict(user_id=...)

token = ajwt.create_token(exp=exp, aud=aud, data=data)
```

### Grabbing Token Data
```python
data = ajwt.token_data()
```