# ApoJWT
The `apojwt` Package was created with the intention of providing JWT support to In10t's Apogee Services. These services require a hierarchy of permissions that vary arcross all endpoints. As such, this package aims to provide decorators that can be attached with route declarations to ensure a valid JWT with proper permissions is being sent in the request headers. The package is inteded to be used alongside an API framework such as Flask or FastAPI.

---


## ApoJWT Class
The ApoJWT class has the following constructor:
```python
ApoJWT(secret: str, iss: str, admin_audience="admin", algorithm="HS256", token_finder=None)
"""
secret: Secret string used to encode and decode the JWT
iss: Issuer string used for additional security
admin_audience: The name of the audience with admin access. Default admin
algorithm: The algorithm to use when encoding/decoding. Default HS256
token_finder: Function used to retrive the JWT from the http request. Default None
permission_formatter: One Parameter (permission name) function used to format permission names
    Can be used to include request data in the permission name
    Example to include a trial_id - lambda permission_name: f"{permission_name}:{request.json['trial_id']}"
"""
```
### Decorators
```python
ajwt = ApoJWT(secret, iss, token_finder=lambda: ..., permission_formatter=lambda perm: ...)


@ajwt.token_required(auth_header: str)
"""Validates JWT

auth_header: http request header with the key "Authorization"
"""

@ajwt.permission_required(auth_header: str, permission_name: str)
"""Validates JWT and ensures permission_name is among the audience (aud)

permission_name: a permission with a predefined schema
"""
```

### Functions
```python
ajwt = ApoJWT(secret, iss)

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
import os
from apojwt import ApoJWT

secret = os.environ.get("SECRET")
iss = os.environ.get("ISSUER")

""" NOTE: token_finder function is required for decorators """

# fast api
token_finder = lambda authorization=Header(None): authorization.replace("Bearer ", "")

# flask
token_finder = lambda: request.headers["Authorization"].replace("Bearer ", "")

ajwt = ApoJWT(secret, iss=iss, token_finder=token_finder)

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